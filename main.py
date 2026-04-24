import os, glob, json, subprocess, urllib.parse, re, statistics
from pathlib import Path
import streamlit as st
import requests
from sympy import symbols, Eq, solve, sympify

VAULT_DIR = r'C:\Users\Sudeep\OneDrive\Documents\ObsedianNotes\Intent'
VAULT_NAME = 'Intent'
OLLAMA_URL='http://localhost:11434/api/generate'

st.set_page_config(page_title='Obsizen V2', layout='wide', initial_sidebar_state='expanded')

@st.cache_data
def load_notes():
    rows=[]
    for f in glob.glob(os.path.join(VAULT_DIR,'**','*.md'), recursive=True):
        try:
            txt=Path(f).read_text(encoding='utf-8', errors='ignore')
            for chunk in [c.strip() for c in txt.split('\n\n') if c.strip()]:
                rows.append((f,chunk))
        except Exception:
            pass
    return rows

def search_notes(query, notes, k=5):
    words=[w for w in re.findall(r'[A-Za-z]+', query.lower()) if len(w)>2]
    hits=[]
    for f,chunk in notes:
        low=chunk.lower()
        score=sum(3 for w in words if w in low)
        if query.lower() in low:
            score += 8
        if score>0:
            hits.append((score,f,chunk))
    hits.sort(reverse=True)
    return hits[:k]

def open_obsidian(path):
    rel=os.path.relpath(path, VAULT_DIR).replace('\\','/')
    uri=f"obsidian://open?vault={urllib.parse.quote(VAULT_NAME)}&file={urllib.parse.quote(rel)}"
    try:
        os.startfile(uri)
    except Exception:
        subprocess.Popen(['cmd','/c','start','',uri], shell=True)

def try_math(task):
    x=symbols('x')
    t=task.lower()
    nums=[float(n) for n in re.findall(r'-?\d+\.?\d*', task)]
    try:
        if 'x' in task and '=' in task:
            left,right=task.replace('^','**').split('=')
            sol=solve(Eq(sympify(left), sympify(right)), x)
            return f"## Solution\n\nSolve: `{task}`\n\n**Answer:** $x = {sol}$"
        if ('mean' in t or 'average' in t) and nums:
            m=sum(nums)/len(nums)
            return f"## Mean\n\nValues: {nums}\n\n$$\\mu = {m:.4f}$$"
        if 'variance' in t and nums:
            v=statistics.pvariance(nums)
            return f"## Variance\n\nValues: {nums}\n\n$$\\sigma^2 = {v:.4f}$$"
    except Exception:
        return None
    return None

def llm_answer(model, prompt, panel):
    final=''
    r=requests.post(OLLAMA_URL, json={'model':model,'prompt':prompt,'stream':True}, stream=True, timeout=120)
    for line in r.iter_lines():
        if line:
            data=json.loads(line.decode('utf-8'))
            final += data.get('response','')
            panel.markdown('## Answer\n\n'+final)
    return final

notes=load_notes()
with st.sidebar:
    st.title('Obsizen V2')
    model=st.selectbox('Model',['qwen:7b','phi3:mini'])
    generate=st.button('Generate Answer', use_container_width=True)
    clear=st.button('Clear', use_container_width=True)
    answer_panel=st.empty()
if clear:
    st.session_state['ans']=''

st.title('Obsizen V2')
q=st.text_input('Question / Topic')
extra=st.text_area('Details / Full Problem')
selected=[]
if q:
    hits=search_notes(q, notes)
    st.subheader('Relevant Notes')
    for i,(_,f,chunk) in enumerate(hits):
        st.markdown(f"### {Path(f).name}")
        st.caption(str(Path(f).parent))
        st.write(chunk)
        c1,c2=st.columns([1,2])
        if c1.button('Open', key=f'o{i}'):
            open_obsidian(f)
        if c2.checkbox('Use for answer', value=(i<2), key=f'u{i}'):
            selected.append((f,chunk))
        st.divider()

if generate:
    task = extra.strip() if extra.strip() else q.strip()
    solved = try_math(task)
    if solved:
        answer_panel.markdown(solved)
        st.session_state['ans']=solved
    else:
        context='\n\n'.join([f"FILE: {Path(f).name}\n{c}" for f,c in selected[:2]])
        prompt=f"You are Obsizen, a sharp tutor. If the task is mathematical, solve it step by step with formulas and final answer. If conceptual, explain clearly with examples. Use notes only when relevant.\n\nTask:\n{task}\n\nNotes:\n{context}"
        with st.spinner('Thinking...'):
            try:
                ans=llm_answer(model,prompt,answer_panel)
                st.session_state['ans']=ans
            except Exception as e:
                answer_panel.error(str(e))
elif st.session_state.get('ans'):
    answer_panel.markdown(st.session_state['ans'])
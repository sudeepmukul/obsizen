import os, glob, json, subprocess, urllib.parse
from pathlib import Path
import streamlit as st
import requests

VAULT_DIR = r'C:\Users\Sudeep\OneDrive\Documents\ObsedianNotes\Intent'
VAULT_NAME = 'Intent'

st.set_page_config(page_title='Obsizen', layout='wide', initial_sidebar_state='expanded')

st.markdown('''<style>
.block-container{max-width:1200px;padding-top:1rem;padding-bottom:2rem;}
.note{padding:1rem;border:1px solid rgba(255,255,255,.08);border-radius:14px;margin-bottom:1rem;background:rgba(255,255,255,.02)}
</style>''', unsafe_allow_html=True)

@st.cache_data
def load_notes():
    files = glob.glob(os.path.join(VAULT_DIR, '**', '*.md'), recursive=True)
    data=[]
    for f in files:
        try:
            data.append((f, Path(f).read_text(encoding='utf-8', errors='ignore')))
        except:
            pass
    return data

def open_obsidian(path):
    rel = os.path.relpath(path, VAULT_DIR).replace('\\','/')
    uri = f"obsidian://open?vault={urllib.parse.quote(VAULT_NAME)}&file={urllib.parse.quote(rel)}"
    try:
        os.startfile(uri)
    except:
        subprocess.Popen(['cmd','/c','start','',uri], shell=True)

notes = load_notes()

with st.sidebar:
    st.title('Obsizen')
    model = st.selectbox('Model', ['phi3:mini','qwen:7b'])
    generate = st.button('Generate Answer', use_container_width=True)
    answer_panel = st.empty()
    clear = st.button('Clear', use_container_width=True)

if clear:
    st.session_state['answer']=''

st.title('Obsizen')
q = st.text_input('Ask from your notes')
extra = st.text_area('Extra instructions', placeholder='Explain simply, exam style, bullet points...')

selected=[]
if q:
    words=q.lower().split()
    hits=[]
    for f,txt in notes:
        low=txt.lower()
        score=sum(3 for w in words if w in low)+(2 if q.lower() in low else 0)
        if score>0:
            idx=min([low.find(w) for w in words if w in low]+[0])
            snip=txt[max(0,idx-200):idx+700]
            hits.append((score,f,snip))
    hits.sort(reverse=True)

    st.subheader('Relevant Notes')
    for i,(_,f,snip) in enumerate(hits[:6]):
        st.markdown("<div class='note'>", unsafe_allow_html=True)
        st.markdown(f"**{Path(f).name}**")
        st.caption(str(Path(f).parent))
        st.write(snip)
        c1,c2=st.columns([1,2])
        if c1.button('Open', key='open'+str(i)):
            open_obsidian(f)
        use = c2.checkbox('Use for answer', value=(i<2), key='use'+str(i))
        if use:
            selected.append((f,snip))
        st.markdown('</div>', unsafe_allow_html=True)

if generate and q:
    context='\n\n'.join([f"FILE: {Path(f).name}\n{s}" for f,s in selected])
    prompt=f"Answer using ONLY the provided note excerpts. Format the answer with headings, bullet points, numbered lists, and short readable sections. If missing, say not found in notes.\n\nQuestion: {q}\nAdditional Instructions: {extra}\n\nNotes:\n{context}"
    out=answer_panel
    final=''
    try:
        r=requests.post('http://localhost:11434/api/generate', json={'model':model,'prompt':prompt,'stream':True}, stream=True, timeout=120)
        for line in r.iter_lines():
            if line:
                data=json.loads(line.decode('utf-8'))
                final += data.get('response','')
                out.markdown('## Answer\n\n'+final)
        st.session_state['answer']=final
    except Exception as e:
        st.error(str(e))
elif st.session_state.get('answer'):
    answer_panel.markdown('## Answer\n\n' + st.session_state['answer'])

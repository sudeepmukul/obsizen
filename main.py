import os, glob, hashlib, pickle
from pathlib import Path
import streamlit as st
import requests

VAULT_DIR = r'C:\Users\Sudeep\OneDrive\Documents\ObsedianNotes\Intent'

st.set_page_config(page_title='VaultMind AI', layout='wide', initial_sidebar_state='expanded')
st.title('🧠 VaultMind AI')
st.caption('Local AI for your Obsidian notes')

model = st.sidebar.selectbox('Model', ['phi3:mini', 'qwen:7b'])
q = st.text_input('Ask anything about your notes')

@st.cache_data
def load_notes():
    files = glob.glob(os.path.join(VAULT_DIR, '**', '*.md'), recursive=True)
    data=[]
    for f in files:
        try:
            txt = Path(f).read_text(encoding='utf-8', errors='ignore')
            data.append((f,txt))
        except:
            pass
    return data

notes = load_notes()
if q:
    hits = []
    words = q.lower().split()
    for f, txt in notes:
        score = sum(3 for w in words if w in txt.lower()) + (1 if q.lower() in txt.lower() else 0)
        if score > 0:
            hits.append((score, f, txt[:1200]))
    hits.sort(reverse=True)
    top = hits[:3]

    if top:
        context = '\n\n'.join([h[2] for h in top])
        prompt = f"Use the provided notes context to answer clearly and helpfully.\n\nQuestion: {q}\n\nContext:\n{context}"
        try:
            r = requests.post('http://localhost:11434/api/generate', json={"model": model, "prompt": prompt, "stream": False}, timeout=120)
            ans = r.json().get('response', 'No response')
        except Exception as e:
            ans = f'Ollama error: {e}'

        st.subheader('AI Answer')
        st.write(ans)
        st.subheader('Sources')

        for _, f, snip in top:
            with st.expander(Path(f).name):
                st.write(snip)
                c1, c2, c3 = st.columns(3)
                if c1.button('Open', key='o'+f):
                    os.startfile(f)
                if c2.button('Summarize', key='s'+f):
                    st.write(snip[:500])
                if c3.button('Quiz Me', key='q'+f):
                    st.write('1. What is the main idea?')
    else:
        st.info('No matching notes found yet.')

st.sidebar.write('Vault Folder')
st.sidebar.code(VAULT_DIR)

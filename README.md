# Obsizen V2

Obsizen is a local AI assistant built for Obsidian users who want one workspace for:

* Searching notes
* Opening source notes instantly
* Asking conceptual questions
* Solving math/statistics problems
* Getting tutor-style explanations
* Running fully on local models with Ollama

## Vision

Instead of switching between note apps, calculators, and AI tools, Obsizen aims to combine everything into one interface.

## Current Features

### Notes Engine

* Scans your Obsidian vault
* Finds relevant note chunks
* Lets you open notes directly in Obsidian
* Select note context for answers

### Tutor Engine

* Explains concepts clearly
* Gives structured responses
* Uses local LLMs through Ollama
* Supports models like `qwen:7b` and `phi3:mini`

### Math Engine (Early Stage)

* Solves basic algebra equations
* Calculates mean
* Calculates variance
* Designed to expand into a full quantitative engine

## Tech Stack

* Python
* Streamlit
* Ollama
* SymPy
* Obsidian URI integration

## Why Local?

* Private by default
* No cloud dependency
* Uses your own notes
* Works with your own models
* Fully customizable

## Setup

### 1. Install dependencies

```bash
pip install streamlit requests sympy
```

### 2. Install and run Ollama

Make sure Ollama is installed and running.

Example models:

```bash
ollama run qwen:7b
ollama run phi3:mini
```

### 3. Configure vault path

Edit the vault path inside the app:

```python
VAULT_DIR = r"C:\\Path\\To\\Your\\ObsidianVault"
```

### 4. Run the app

```bash
python -m streamlit run obsizen_v2.py
```

## Roadmap

* Better retrieval with embeddings
* Stronger math/statistics engine
* Better UI/UX
* Flashcards and quiz mode
* Study dashboard
* Memory and conversation history
* Faster responses
* Better formatting

## Status

Work in progress. Built through rapid iteration and real-world testing.

## License

MIT (or choose your preferred license)

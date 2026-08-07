<div align="center">


# :) OBSIZEN

### Transform your Obsidian vault into an intelligent AI knowledge companion.

<p>
  <a href="https://github.com/sudeepmukul/obsizen/stargazers">
    <img src="https://img.shields.io/github/stars/sudeepmukul/obsizen?style=for-the-badge&logo=github" />
  </a>
  <a href="https://github.com/sudeepmukul/obsizen/network/members">
    <img src="https://img.shields.io/github/forks/sudeepmukul/obsizen?style=for-the-badge&logo=github" />
  </a>
  <a href="https://github.com/sudeepmukul/obsizen/issues">
    <img src="https://img.shields.io/github/issues/sudeepmukul/obsizen?style=for-the-badge&logo=github" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/sudeepmukul/obsizen?style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/badge/Open%20Source-❤️-red?style=for-the-badge" />
</p>

<p>
  <strong>Your second brain just got a search engine and an AI assistant.</strong>
</p>

[✨ Features](#-features) •
[🏗 Architecture](#-architecture) •
[🚀 Getting Started](#-getting-started) •
[📖 Usage](#-usage) •
[🗺 Roadmap](#-roadmap)

</div>

---

# :O What is OBSIZEN?

**OBSIZEN** is an open-source **Retrieval-Augmented Generation (RAG)** system built specifically for **Obsidian** users.

Instead of manually digging through hundreds or thousands of notes, OBSIZEN turns your vault into an intelligent knowledge companion that can:

* 🔍 Search semantically across your notes
* 📄 Understand filenames and metadata
* 🧩 Combine multiple retrieval strategies
* 🎯 Rerank results for better answers
* 🤖 Generate grounded responses using LLMs

Think of it as:

> **ChatGPT for your Obsidian vault, except it actually knows your notes.**

---

# :D Features

<table>
<tr>
<td width="50%">

### 🔎 Hybrid Retrieval

Combines:

* Vector Search
* BM25 Search
* Filename Search

</td>
<td width="50%">

### 🏷 Metadata Awareness

Understands:

* Tags
* Frontmatter
* File structure
* Document context

</td>
</tr>

<tr>
<td>

### ;) Fast & Efficient

* Incremental indexing
* Cached models
* Reduced startup time

</td>
<td>

### :} Better Answers

* Source deduplication
* CrossEncoder reranking
* Grounded generation

</td>
</tr>
</table>

---

# 📸 Demo

<div align="center">

<img src="./assets/demo.gif" width="90%" alt="OBSIZEN Demo"/>

</div>

---

# 🏗 Architecture

```text
                ┌────────────────┐
                │ Obsidian Vault │
                └────────┬───────┘
                         │
                         ▼
               ┌──────────────────┐
               │ Markdown Loader  │
               └────────┬─────────┘
                        │
                        ▼
          ┌───────────────────────────┐
          │ Markdown Header Chunking  │
          └────────┬──────────────────┘
                   │
                   ▼
          ┌───────────────────────────┐
          │ Embedding Generation      │
          └────────┬──────────────────┘
                   │
                   ▼
             ┌─────────────┐
             │  ChromaDB   │
             └──────┬──────┘
                    │
                    ▼
     ┌───────────────────────────────────┐
     │ Hybrid Retrieval Engine           │
     │ Vector + BM25 + Filename Search   │
     └───────────────────────────────────┘
                    │
                    ▼
          ┌────────────────────┐
          │ Metadata Boosting  │
          └────────┬───────────┘
                   │
                   ▼
         ┌─────────────────────┐
         │ Source Deduplication│
         └────────┬────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │ CrossEncoder Ranker │
         └────────┬────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │   Context Builder   │
         └────────┬────────────┘
                  │
                  ▼
       ┌──────────────────────────┐
       │ DeepSeek via OpenRouter  │
       └───────────┬──────────────┘
                   │
                   ▼
          🌌 Grounded AI Answer
```

---

#  Getting Started

## Clone the Repository

```bash
git clone https://github.com/sudeepmukul/obsizen.git
cd obsizen
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure

Create your environment file:

```env
OPENROUTER_API_KEY=your_api_key
OBSIDIAN_VAULT_PATH=/path/to/your/vault
```

---

# 📖 Usage

## Build the Index

```bash
python src/main.py
```

## Ask Questions

```text
What are my YC ideas?
What did I learn about FastAPI?
Summarize my ML notes.
What projects am I procrastinating on?
```

OBSIZEN retrieves relevant notes, reranks the results, and generates a grounded answer directly from your vault.

---

# ⚙️ Tech Stack

<p align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,react" />

</p>

```text
LangChain
ChromaDB
SentenceTransformers
CrossEncoder
OpenRouter
Python
```

---

# 🗺 Roadmap

* [x] Hybrid Retrieval
* [x] Metadata Retrieval
* [x] Incremental Indexing
* [x] CrossEncoder Reranking
* [ ] Logging System
* [ ] Comprehensive Tests
* [ ] Better Error Handling
* [ ] FastAPI Backend
* [ ] React Web UI
* [ ] Local LLM Support
* [ ] Docker Deployment
* [ ] Obsidian Plugin

---

# 🤝 Contributing

Contributions are welcome and greatly appreciated.

```bash
Fork 
Clone 
Create a Branch 
Commit 
Open a Pull Request 
```

If you have ideas, feature requests, or improvements, open an issue and let's build a better second brain together.

---

# ⭐ Support the Project

If OBSIZEN helped you organize your knowledge and think better:

🌟 Star the repository
🐛 Report bugs
💡 Suggest features
🤝 Contribute code

---

<div align="center">

# 🌌 Built with <3 by Sudeep Mukul & Zency R&D Team

### Transform your notes into an AI-powered second brain.

**If this project helped you, consider giving it a ⭐**

</div>

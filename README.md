# OBSIZEN :)

A Retrieval-Augmented Generation (RAG) system for chatting with an Obsidian knowledge base using LangChain, ChromaDB, Hugging Face embeddings, CUDA acceleration, and DeepSeek via OpenRouter.

## Overview

OBSIZEN transforms an Obsidian vault into a searchable semantic knowledge base.

Instead of manually searching through hundreds of notes, the system:

1. Loads Markdown notes from an Obsidian vault.
2. Splits notes into smaller chunks.
3. Converts chunks into vector embeddings using a Sentence Transformer model.
4. Stores embeddings in ChromaDB.
5. Retrieves relevant note chunks based on semantic similarity.
6. Sends retrieved context to an LLM for grounded answers.

This allows natural language querying of personal notes while reducing hallucinations by restricting responses to information found within the vault.

---

## Architecture

```text
Obsidian Vault
      │
      ▼
Markdown Loader
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
Chroma Vector Database
      │
      ▼
Semantic Retrieval
      │
      ▼
DeepSeek LLM (OpenRouter)
      │
      ▼
Grounded Answer
```

---

## Technologies Used

* Python
* LangChain
* ChromaDB
* Hugging Face Sentence Transformers
* DeepSeek Chat
* OpenRouter API
* NVIDIA CUDA
* Obsidian

---

## Features

### Semantic Search

Unlike traditional keyword search, queries are converted into embeddings and matched based on meaning.

Example:

**Query**

```text
How do generators reduce memory usage?
```

Can successfully retrieve notes containing:

```text
Python generators save RAM by yielding values lazily.
```

even when exact keywords differ.

---

### Retrieval-Augmented Generation (RAG)

The language model does not answer from its training data alone.

Workflow:

1. Search vector database.
2. Retrieve most relevant note chunks.
3. Inject retrieved notes into the prompt.
4. Generate an answer using only retrieved context.

Prompt grounding reduces hallucinations and keeps responses tied to personal notes.

---

### CUDA Acceleration

Embedding generation is accelerated using an NVIDIA RTX 3050 Laptop GPU.

PyTorch CUDA support enables GPU-based embedding computation, significantly reducing indexing time for large Obsidian vaults.

```python
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"}
)
```

---

## Project Structure

```text
OBSIZEN/
│
├── ask.py
├── build_v.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── obsidian_db/
```

---

## Indexing Pipeline

The indexing script:

* Recursively scans Markdown files.
* Loads note contents.
* Splits notes into overlapping chunks.
* Generates vector embeddings.
* Stores embeddings in ChromaDB.

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

Each chunk becomes a searchable vector representation.

---

## Query Pipeline

When a question is asked:

```text
User Question
      │
      ▼
Embedding Generation
      │
      ▼
Vector Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
DeepSeek Response
```

Example:

```text
Ask: What are embeddings?
```

The system retrieves the most relevant notes and uses them as context for the response.

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd OBSIZEN
```

### Create Virtual Environment

```bash
python -m venv myvenv
```

### Activate Environment

Windows:

```bash
myvenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### Build Vector Database

```bash
python build_v.py
```

### Start Chat Interface

```bash
python ask.py
```

---

## Example Session

```text
Ask: What is LangChain?

============================================================
ANSWER
============================================================

LangChain is a framework used for building applications
powered by large language models...

SOURCES:
- AI/LangChain.md
- Projects/RAG.md
```

---

## Future Improvements

* Metadata-aware retrieval
* Hybrid Search (Vector + BM25)
* Reranking models
* Conversational memory
* Markdown-aware chunking
* Multi-vault support
* Local LLM support
* Streamlit/Web UI
* Source citations inside answers

---


This project was built to explore modern Retrieval-Augmented Generation systems and create a practical AI assistant capable of searching and reasoning over a personal Obsidian knowledge base.

It demonstrates core concepts used in production RAG systems, including vector embeddings, semantic retrieval, context injection, and GPU-accelerated indexing.

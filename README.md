# :) OBSIZEN

> Transform your Obsidian vault into an intelligent AI knowledge companion.

OBSIZEN is an open-source Retrieval-Augmented Generation (RAG) system designed specifically for Obsidian users.

It combines semantic search, keyword search, metadata-aware retrieval, and reranking to provide grounded answers from your notes.

---

## :D Features
## Features

- Hybrid Retrieval (Vector + BM25)
- Metadata-Aware Retrieval
- Filename Retrieval
- Source Deduplication
- CrossEncoder Reranking
- Incremental Indexing
- Cached Models for Fast Startup
- Config-Driven Architecture
- OpenRouter Integration

---

## Architecture

```text
Obsidian Vault
      │
      ▼
Markdown Loader
      │
      ▼
Markdown Header Chunking
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB
      │
      ▼
Hybrid Retrieval
(Vector + BM25 + Filename Search)
      │
      ▼
Metadata Boosting
      │
      ▼
Source Deduplication
      │
      ▼
CrossEncoder Reranker
      │
      ▼
Context Builder
      │
      ▼
DeepSeek via OpenRouter
      │
      ▼
Grounded Answer
```
## Usage

Build index:

python src/main.py

Ask questions:

Ask Away!

> What are my YC ideas?
> What did I learn about FastAPI?
> Summarize my ML notes.

Future Roadmap:
Logging 
Tests
Error Handling

FastAPI Backend

React Web UI

Local LLM Support

## Tech Stack
```text
LangChain
ChromaDB
SentenceTransformers
CrossEncoder
OpenRouter
Python
```

## Contribution
Pull requests are welcome.

## License 
MIT License


# OBSIZEN

**Turn your Obsidian vault into a searchable AI knowledge base.**

OBSIZEN is an open-source Retrieval-Augmented Generation (RAG) system that enables natural language interaction with Obsidian notes. It combines semantic search, keyword search, reranking, vector databases, and modern Large Language Models to provide grounded answers directly from your personal knowledge base.

Instead of manually searching through folders, tags, and hundreds of Markdown files, simply ask questions and receive answers backed by your notes.

---

## Features

* Semantic Search over Obsidian notes
* Hybrid Retrieval (Vector Search + BM25)
* Cross-Encoder Reranking
* Retrieval-Augmented Generation (RAG)
* Source-aware responses
* ChromaDB vector storage
* Hugging Face embedding models
* OpenRouter LLM integration
* CUDA acceleration support
* Configurable Obsidian vault paths
* Startup model caching and preloading
* Modular architecture designed for extensibility

---

## Why OBSIZEN?

Traditional note-taking systems excel at storing information.

OBSIZEN focuses on retrieving information.

Instead of asking:

> Where did I save that note?

You can ask:

> What were my startup ideas for Zency?

> Explain Retrieval-Augmented Generation from my notes.

> What projects am I currently working on?

> What did I learn about LangChain?

and receive answers grounded in your own knowledge base.

---

## Architecture

```text
Obsidian Vault
       │
       ▼
Markdown Loader
       │
       ▼
Document Chunking
       │
       ▼
Embedding Generation
       │
       ▼
ChromaDB
       │
       ▼
Semantic Search
       │
       ├───────────────┐
       ▼               ▼
Vector Retrieval   BM25 Retrieval
       │               │
       └───────┬───────┘
               ▼
         Score Fusion
               ▼
   Cross-Encoder Reranker
               ▼
        Context Builder
               ▼
        LLM Generation
               ▼
        Grounded Answer
```

---

## Technology Stack

| Component       | Technology                |
| --------------- | ------------------------- |
| Language        | Python                    |
| Framework       | LangChain                 |
| Vector Database | ChromaDB                  |
| Embeddings      | Hugging Face Transformers |
| Retrieval       | BM25 + Vector Search      |
| Reranking       | Cross-Encoder             |
| LLM Provider    | OpenRouter                |
| Default Model   | DeepSeek Chat             |
| Notes Platform  | Obsidian                  |
| Acceleration    | NVIDIA CUDA               |

---

## Why ObsiZen Is Different

Many personal RAG projects stop at:

```text
Vault
 ↓
Embeddings
 ↓
ChromaDB
 ↓
LLM
```

OBSIZEN goes further by incorporating:

* Hybrid Retrieval
* BM25 Keyword Search
* Semantic Vector Search
* Cross-Encoder Reranking
* Startup Model Caching
* Modular Architecture
* Future Metadata-Aware Retrieval

The goal is to evolve from a simple note chatbot into a high-quality personal knowledge retrieval system.

---

## Project Structure

```text
OBSIZEN/
│
├── src/
│   │
│   ├── main.py
│   │
│   ├── core/
│   │   ├── embeddings.py
│   │   ├── indexing.py
│   │   ├── retrieval.py
│   │   ├── reranker.py
│   │   └── bm25.py
│   │
│   ├── llm/
│   │   └── openrouter.py
│   │
│   ├── ui/
│   │   └── cli.py
│   │
│   └── config.py
│
├── data/
│   ├── obsidian_db/
│   └── chunks.pkl
│
├── NotesSimpleRAG/
│
├── config.yaml
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/obsizen.git

cd obsizen
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

Linux/macOS:

```bash
source myvenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Create a `.env` File

```env
OPENROUTER_API_KEY=your_api_key_here
```

### Configure `config.yaml`

```yaml
vault:
  path: "YOUR_OBSIDIAN_VAULT_PATH"

retrieval:
  top_k: 10

index:
  chunk_size: 800
  chunk_overlap: 100

embedding:
  model: "BAAI/bge-small-en-v1.5"

llm:
  model: "deepseek/deepseek-chat"
```

---

## Usage

Start ObsiZen:

```bash
python src/main.py
```

On first launch:

```text
No index found.
Building index...
```

ObsiZen automatically:

* Loads Markdown notes
* Splits documents into chunks
* Generates embeddings
* Builds ChromaDB
* Creates BM25 indexes

Once initialization completes:

```text
Loading ObsiZen...

ObsiZen Ready!

Ask:
>
```

---

## Example

```text
Ask:
What is Retrieval-Augmented Generation?

Answer:

Retrieval-Augmented Generation (RAG) combines
retrieval systems and Large Language Models
to generate answers grounded in external data.

Sources:
- RAG.md
- LangChain.md
```

---

## Performance Optimizations

Current versions include:

* Embedding model caching
* ChromaDB caching
* BM25 caching
* Reranker caching
* Startup preloading

These optimizations reduce repeated initialization overhead and improve query responsiveness.

---

## Roadmap

### Completed

#### v1.3.1

* Hybrid Retrieval (BM25 + Vector Search)

#### v1.3.2

* Cross-Encoder Reranking

#### v1.3.4

* Embedding Cache
* Chroma Cache
* BM25 Cache
* Reranker Cache
* Startup Preloading

### Upcoming

#### v1.4.0

* Metadata-Aware Retrieval
* Markdown-Aware Chunking
* Source Deduplication
* Improved Entity Retrieval

#### v1.5.0

* FastAPI Backend
* REST API
* Better Integrations

#### v2.0

* Ollama Support
* Local LLM Support
* MCP Integration
* Multi-Vault Search

---

## Contributing

Contributions, ideas, bug reports, and pull requests are welcome.

If you have ideas for improving retrieval quality, chunking strategies, ranking systems, or user experience, feel free to open an issue or submit a pull request.

---

## Disclaimer

OBSIZEN is an educational and experimental project focused on Retrieval-Augmented Generation, semantic search, and personal knowledge management.

Always verify important information directly from your source notes.

---

## License

MIT License

---

Built with Python, curiosity, and a growing obsession with knowledge retrieval.

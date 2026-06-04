# OBSIZEN :)

**Turn your Obsidian vault into a searchable AI knowledge base.**

OBSIZEN is an open-source Retrieval-Augmented Generation (RAG) system that allows you to chat with your Obsidian notes using semantic search, vector embeddings, ChromaDB, and modern Large Language Models.

Instead of manually searching through folders, tags, and hundreds of Markdown files, simply ask questions in natural language and receive grounded answers sourced directly from your notes.

---

## ✨ Features

*  Semantic Search over Obsidian notes
*  Retrieval-Augmented Generation (RAG)
*  Source-aware responses
*  ChromaDB vector storage
*  Hugging Face embedding models
*  OpenRouter + DeepSeek integration
*  CUDA acceleration support
*  Configurable Obsidian vault paths
*  Modular architecture for future expansion

---

## Why OBSIZEN?

Traditional note-taking systems excel at storing information.

OBSIZEN focuses on retrieving information.

Instead of asking:

> "Where did I save that note?"

you can ask:

> "What were my startup ideas for Zency?"
>
> "Explain RAG from my notes."
>
> "What projects am I currently working on?"

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
Chunking
      │
      ▼
Embedding Model
      │
      ▼
ChromaDB
      │
      ▼
Semantic Retrieval
      │
      ▼
LLM Context Injection
      │
      ▼
Grounded Answer
```

---

## Tech Stack

| Component       | Technology                         |
| --------------- | ---------------------------------- |
| Language        | Python                             |
| Framework       | LangChain                          |
| Vector Database | ChromaDB                           |
| Embeddings      | Hugging Face Sentence Transformers |
| LLM Provider    | OpenRouter                         |
| Default Model   | DeepSeek Chat                      |
| Notes Platform  | Obsidian                           |
| Acceleration    | NVIDIA CUDA                        |

---

## Project Structure

```text
OBSIZEN/
│
├── src/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── embeddings.py
│   │   ├── indexing.py
│   │   └── retrieval.py
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
│   └── obsidian_db/
│
├── NotesSimpleRAG/
│
├── config.yaml
├── .env.example
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/obsizen.git

cd obsizen
```

### 2. Create Virtual Environment

```bash
python -m venv myvenv
```

### 3. Activate Environment

Windows:

```bash
myvenv\Scripts\activate
```

Linux / macOS:

```bash
source myvenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Create `.env`

```env
OPENROUTER_API_KEY=your_openrouter_api_key
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

Start OBSIZEN:

```bash
python src/main.py
```

On first run:

```text
No index found.
Building index...
```

OBSIZEN automatically:

* Loads notes
* Creates chunks
* Generates embeddings
* Builds ChromaDB

After indexing:

```text
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
vector retrieval with Large Language Models
to generate answers grounded in external data.

Sources:
📄 RAG.md
📄 LangChain.md
```

---

## Current Roadmap for Future Versions (open to contributions)

### v1.x

* Semantic Search
* ChromaDB Integration
* OpenRouter Support
* Configurable Vaults
* Modular Architecture

### v2.x

* Hybrid Search (BM25 + Vector)
* Reranking Models
* Metadata Filtering
* Improved Citations
* Better Chunking Strategies

### v3.x

* Ollama Support
* Local LLM Support
* MCP Integration
* Research Agent
* Multi-Vault Search

---

## Contributing

Contributions, ideas, bug reports, and pull requests are welcome.

If you find a bug or have an idea for improving retrieval quality, feel free to open an issue.

---

## Disclaimer

OBSIZEN is an educational and experimental project focused on exploring Retrieval-Augmented Generation systems, semantic search, and personal knowledge management.

Always verify important information directly from your notes.

---

## License

MIT License

---

Built with Caffine lol, Python, and a growing obsession with knowledge retrieval.

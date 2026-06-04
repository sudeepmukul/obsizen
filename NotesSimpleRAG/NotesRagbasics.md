# BUILDING VECTOR DB EMBEDDINGS
Import following 
```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
```
-Document Loaders are to load docs and read , Text Loader is to go through text.
-Under langchain_text_splitters we use ## RecursiveCharacterTextSplitter , to cut down huge text into chunks 
-Under langchain_community we import chroma db
-To convert into embeddings or vectors we use HuggingFaceEmbeddings
```
[0.124, -0.522, 0.992, ...]
```
### Give Path to File Location
```python
VAULT_DIR = r"C:\Users\Sudeep\OneDrive\Documents\ObsedianNotes\Intent"
```
### Create a Loader that loads the Embeddings
```python
loader = DirectoryLoader(
	path = VAULT_DIR,
	glob = "**/*.md", #Find every markdown file recursively
	loader_cls=TextLoader,
	loader_kwargs={
		"encoding": "utf-8",  #Obsedian Uses this Text Encoding
		"autodetect_encoding": True #if not utf-8 do other like ANSI etc
	},
	silent_errors=True #if error skip (if this no exist boom program crash)
)
```
### Load the Docs
```python
docs = loader.load()
```
and Count how many are loaded
```python
print(f"Loaded {len(docs)} notes")
```
If no docs found logic
```python
if len(docs) == 0:
    print("No notes found!")
    exit()
```
### Now Split the Text into Chunks
Give it Chunk Size and Overlap
Also You can think of **chunk overlap as a bridge between neighboring chunks**.
Chunk 1 -> Unc is very sus
Chunk 2 -> very sus and non-chalant  <--- See how Text is repeated from Chunk 1 that is Overlap of Chunking
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

```python
chunks = splitter.split_documents(docs)
```

### Load the Embedding Model to store them as Vectors
```python
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

Here 
*384-dimensional embeddings*
Is cool coz its fast , free and opensource , small and has good sematic Search

### Create the Vector DB
```python
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="obsidian_db"
)
```
persist_directory here means it will be stored in "obsedian_db" as in our Disk.
Chunk -> Who is Neymar?
embedding -> 
```python
[0.22, -0.11, ...]
```
This will be Stored in Chroma DB

```
COMPLETE STRUCTURE

Obsidian Vault
      │
      ▼
DirectoryLoader
      │
      ▼
Markdown Files
      │
      ▼
TextLoader
      │
      ▼
Documents
      │
      ▼
Text Splitter
      │
      ▼
Chunks
      │
      ▼
Embedding Model
      │
      ▼
Vectors
      │
      ▼
Chroma DB
```

-----
# RAG SEARCH

Import Stuff
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
```
to import the env file we created. Importing OS is important for it too without that Python Can't do it.

Despite the name "ChatOpenAI" It can be used to chat with many formats under OpenAI Compatible API like OpenRouter where you can use deepseek too etc.

Obviously -> Chroma Db from langchain_community.vectorstores to load saved db from build_vector program above

To Understand Embeddings we took HuggingFaceEmbeddings

Loading the ENV
```python
load_dotenv()
```
### Create Embedding Model
```python
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```
### Load the Chroma DB
```python
db = Chroma(
    persist_directory="obsidian_db",
    embedding_function=embeddings
)
```
Chroma Opens the same DB that we Created in the Above Build_vector Program

### Create A LLM
```python
llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-chat"
)
```

Create a Infinite While Loop or Just Normal
User Input
```python
question = input("\nAsk: ")
```

### Search Chroma DB
```python
docs = db.similarity_search(question, k=3)
```
Using Sematic Similarity Search.
k=3 -> Return top 3 Chunks
### Build Context
```python
context = "\n\n".join(
    [doc.page_content for doc in docs]
)
```
### Give a Good Prompt
```python
prompt = f"""
Answer ONLY using the provided notes.
...
"""
```
### Invoke the LLM Model with Prompt
```python
response = llm.invoke(prompt)
```

### Print the Answer and Get Sources
```python
 print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(response.content)

    print("\nSOURCES:")

    shown = set()
  
    for doc in docs:
        source = doc.metadata.get("source", "Unknown")

        if source not in shown:
            print("-", source)
            shown.add(source)
```

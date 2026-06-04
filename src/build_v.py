from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Your Obsidian Vault
VAULT_DIR = r"C:\Users\Sudeep\OneDrive\Documents\ObsedianNotes\Intent"

print("Loading notes...Wait LOL")

# Load all markdown files
loader = DirectoryLoader(
    path=VAULT_DIR,
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={
        "encoding": "utf-8",
        "autodetect_encoding": True
    },
    silent_errors=True
)

docs = loader.load()

print(f"Loaded {len(docs)} notes")

if len(docs) == 0:
    print("No notes found!")
    exit()

print("Splitting notes into chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating vector database...")

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="obsidian_db"
)

print("\n✅ Index Created Successfully!")
print(f"📄 Notes Loaded : {len(docs)}")
print(f"🧩 Chunks Created : {len(chunks)}")
print("💾 Database Saved : obsidian_db")
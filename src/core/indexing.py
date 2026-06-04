from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from config import CONFIG
from core.embeddings import get_embeddings


def build_index():

    print("Loading notes...LOL")

    loader = DirectoryLoader(
        path=CONFIG["vault"]["path"],
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

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CONFIG["index"]["chunk_size"],
        chunk_overlap=CONFIG["index"]["chunk_overlap"]
    )

    chunks = splitter.split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="data/obsidian_db"
    )

    print("Index built successfully!")

    return db
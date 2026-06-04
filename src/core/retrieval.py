from langchain_community.vectorstores import Chroma

from config import CONFIG
from core.embeddings import get_embeddings


def get_db():

    return Chroma(
        persist_directory="data/obsidian_db",
        embedding_function=get_embeddings()
    )


def retrieve(query):

    db = get_db()

    docs = db.similarity_search(
        query,
        k=CONFIG["retrieval"]["top_k"]
    )

    return docs
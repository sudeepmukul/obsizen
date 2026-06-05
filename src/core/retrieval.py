from langchain_community.vectorstores import Chroma
import pickle

from core.bm25 import BM25Retriever
from config import CONFIG
from core.embeddings import get_embeddings


def get_db():

    return Chroma(
        persist_directory="data/obsidian_db",
        embedding_function=get_embeddings()
    )
def get_bm25():

    with open(
        "data/chunks.pkl",
        "rb"
    ) as f:

        chunks = pickle.load(f)

    return BM25Retriever(
        chunks
    )


def retrieve(query):

    db = get_db()

    bm25 = get_bm25()

    vector_docs = db.similarity_search(
        query,
        k=5
    )

    keyword_docs = bm25.search(
        query,
        k=5
    )

    combined = []

    seen = set()

    for doc in vector_docs + keyword_docs:

        content = doc.page_content

        if content not in seen:

            seen.add(content)

            combined.append(doc)

    return combined[:10]
    '''db = get_db() #Old Semantic Search Only Version - Intent 6/6/26

    docs = db.similarity_search(
        query,
        k=CONFIG["retrieval"]["top_k"]
    )

    return docs'''
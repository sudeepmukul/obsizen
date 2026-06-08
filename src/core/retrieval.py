from langchain_community.vectorstores import Chroma
import pickle

from core.bm25 import BM25Retriever
from config import CONFIG
from core.embeddings import get_embeddings
from core.reranker import Reranker #1.3.2 ADDition hehe
_db = None
_bm25 = None
_reranker = None

def get_db():

    global _db

    if _db is None:

        print("Loading Chroma DB...")

        _db = Chroma(
            persist_directory="data/obsidian_db",
            embedding_function=get_embeddings()
        )

    return _db
def get_bm25():

    global _bm25

    if _bm25 is None:

        print("Loading BM25...")

        with open(
            "data/chunks.pkl",
            "rb"
        ) as f:

            chunks = pickle.load(f)

        _bm25 = BM25Retriever(
            chunks
        )

    return _bm25

def get_reranker():

    global _reranker

    if _reranker is None:

        print("Loading Reranker...")

        _reranker = Reranker()

    return _reranker

def retrieve(query):

    

    bm25 = get_bm25()

    vector_results = vector_search(
    query,
    k=CONFIG["retrieval"]["top_k"]
)

    bm25_results = bm25.search(
    query,
    k=CONFIG["retrieval"]["top_k"]
)

    docs = fuse_results( #v1.3.2 Reranker Addition
    vector_results,
    bm25_results
)

    docs = get_reranker().rerank(
    query,
    docs,
    top_k=4
)

    return docs

def vector_search(query, k=10): #Vector Search Damn bro v1.3.2 Addition

    db = get_db()

    results = db.similarity_search_with_relevance_scores(
        query,
        k=k
    )

    return results

def fuse_results( #Fusion Function Damn bro v1.3.2 Addition
    vector_results,
    bm25_results
):

    scores = {}

    for doc, score in vector_results:

        key = doc.page_content

        scores[key] = {
            "doc": doc,
            "score": score * 2
        }

    for doc, score in bm25_results:

        key = doc.page_content

        if key not in scores:

            scores[key] = {
                "doc": doc,
                "score": score
            }

        else:

            scores[key]["score"] += score

    ranked = sorted(
        scores.values(),
        key=lambda x: x["score"],
        reverse=True
    )
    print("\n=== HYBRID RESULTS ===")

    for i, item in enumerate(ranked[:10]):

        source = item["doc"].metadata.get(
        "source",
        "unknown"
    )

        print(
            f"{i+1}. {source} | "
            f"{round(item['score'], 2)}"
        )
    

    return [
        item["doc"]
        for item in ranked[:10]
    ]
    '''db = get_db() #Old Semantic Search Only Version - Intent 6/6/26

    docs = db.similarity_search(
        query,
        k=CONFIG["retrieval"]["top_k"]
    )

    return docs'''

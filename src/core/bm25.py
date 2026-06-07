from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, docs):

        self.docs = docs

        self.tokenized_docs = [
            doc.page_content.lower().split()
            for doc in docs
        ]

        self.bm25 = BM25Okapi(
            self.tokenized_docs
        )

    def search(self, query, k=5):

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            zip(self.docs, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:k]
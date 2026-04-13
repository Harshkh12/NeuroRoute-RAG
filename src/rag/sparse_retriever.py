from rank_bm25 import BM25Okapi
from langchain_core.documents import Document
from typing import List

class SparseRetriever:
    def __init__(self):
        self.docs: List[Document] = []
        self.bm25 = None

    def build_index(self, documents: List[Document]) -> None:
        """Call this after every document upload."""
        self.docs = documents
        tokenized = [d.page_content.lower().split() for d in documents]
        self.bm25 = BM25Okapi(tokenized)

    def retrieve(self, query: str, top_k: int = 5) -> List[Document]:
        if not self.bm25 or not self.docs:
            return []
        scores = self.bm25.get_scores(query.lower().split())
        ranked = sorted(
            zip(self.docs, scores),
            key=lambda x: x[1],
            reverse=True
        )
        return [doc for doc, score in ranked[:top_k] if score > 0]

# Singleton — imported everywhere
sparse_retriever = SparseRetriever()

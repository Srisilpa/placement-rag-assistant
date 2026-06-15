from src.vectordb.chroma_store import (
    ChromaStore
)


class Retriever:

    def __init__(self):

        self.store = ChromaStore()

    def retrieve(
        self,
        query
    ):

        return self.store.search(
            query=query,
            k=5
        )
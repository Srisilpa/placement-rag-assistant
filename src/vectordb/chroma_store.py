import chromadb


class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="placement_rag"
            )
        )

    def add_documents(
        self,
        chunks
    ):

        ids = [
            f"chunk_{i}"
            for i in range(
                len(chunks)
            )
        ]

        metadata = [
            {
                "chunk_id": i,
                "source": "Placement_RAG_Dataset_Enhanced.pdf"
            }
            for i in range(
                len(chunks)
            )
        ]

        self.collection.add(
            documents=chunks,
            ids=ids,
            metadatas=metadata
        )

    def search(
        self,
        query,
        k=5
    ):

        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )

        return {
            "documents":
                results["documents"][0],
            "metadata":
                results["metadatas"][0]
        }
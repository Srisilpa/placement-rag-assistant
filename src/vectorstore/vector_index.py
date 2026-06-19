from src.vectorstore.chroma_client import get_vectorstore


def search(query):

    db = get_vectorstore()

    print("=" * 50)
    print(
        "Documents in Chroma:",
        db._collection.count()
    )
    print("=" * 50)

    docs = db.similarity_search(
        query,
        k=5
    )

    print(
        "Retrieved:",
        len(docs)
    )

    return docs
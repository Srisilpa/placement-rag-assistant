from src.vectorstore.chroma_client import get_vectorstore

db = get_vectorstore()

print("Documents:", db._collection.count())
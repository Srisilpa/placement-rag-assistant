from src.vectorstore.vector_index import search

def retrieve_docs(query):
    return search(query)
from src.ingestion.loader import load_pdf
from src.ingestion.splitter import split_docs
from src.vectorstore.chroma_client import get_vectorstore


def ingest_pdf(file_path):

    docs = load_pdf(file_path)

    print("Loaded Pages:", len(docs))

    chunks = split_docs(docs)

    print("Created Chunks:", len(chunks))

    db = get_vectorstore()

    db.add_documents(chunks)

    try:
        db.persist()
    except:
        pass

    print(
        "Documents after ingest:",
        db._collection.count()
    )

    return len(chunks)
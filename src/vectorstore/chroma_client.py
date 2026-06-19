from langchain_chroma import Chroma
from src.ingestion.embedder import get_embeddings
from src.core.config import Config

_vectorstore = None


def get_vectorstore():

    global _vectorstore

    if _vectorstore is None:

        _vectorstore = Chroma(
            persist_directory=Config.CHROMA_PATH,
            embedding_function=get_embeddings()
        )

    return _vectorstore
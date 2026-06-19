import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # LLM / API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


    # MySQL
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "placement_db")

    # Vector DB
    CHROMA_PATH = os.getenv("CHROMA_PATH", "data/chroma")

    # Embeddings model
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    GROQ_MODEL = os.getenv("GROQ_MODEL")
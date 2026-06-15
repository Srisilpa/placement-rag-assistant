import sys

from pathlib import Path

project_root = Path(
    __file__
).parent.parent

sys.path.append(
    str(project_root)
)

from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import Chunker
from src.vectordb.chroma_store import ChromaStore


def main():

    loader = PDFLoader()

    text = loader.load_pdf(
        "data/raw/Placement_RAG_Dataset_Enhanced.pdf"
    )

    chunker = Chunker()

    chunks = chunker.split(
        text
    )

    print(
        f"Chunks Created: {len(chunks)}"
    )

    store = ChromaStore()

    store.add_documents(
        chunks
    )

    print(
        "Documents Indexed Successfully"
    )


if __name__ == "__main__":
    main()
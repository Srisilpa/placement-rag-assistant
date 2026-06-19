import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.ingestion.ingest_pipeline import ingest_pdf


pdf_path = "data/pdfs/Placement_RAG_Dataset_Enhanced.pdf"

chunks = ingest_pdf(pdf_path)

print(
    f"Ingestion completed. {chunks} chunks added."
)
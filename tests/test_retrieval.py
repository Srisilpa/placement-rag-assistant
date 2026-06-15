import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.vectordb.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "highest package"
)

print(results)
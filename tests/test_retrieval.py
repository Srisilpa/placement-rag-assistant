import sys
from pathlib import Path

project_root = Path(
    __file__
).parent.parent

sys.path.append(
    str(project_root)
)

from src.vectordb.retriever import Retriever


retriever = Retriever()

results = retriever.retrieve(
    "Which company offers highest package?"
)

for i, result in enumerate(results):

    print("\n")
    print("=" * 50)
    print(f"Result {i+1}")
    print("=" * 50)

    print(result)
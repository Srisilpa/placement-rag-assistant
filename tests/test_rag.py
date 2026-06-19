import sys
from pathlib import Path

project_root = Path(
    __file__
).parent.parent

sys.path.append(
    str(project_root)
)

from src.vectordb.retriever import Retriever
from src.llm.response_generator import ResponseGenerator


question = (
    "Which company offers highest package?"
)

retriever = Retriever()

contexts = retriever.retrieve(
    question
)

generator = ResponseGenerator()

answer = generator.answer(
    question,
    contexts
)

print("\n")
print(answer)
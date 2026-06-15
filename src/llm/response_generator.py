from src.llm.groq_client import (
    GroqClient
)


class ResponseGenerator:

    def __init__(self):

        self.llm = GroqClient()

    def answer(
        self,
        question,
        contexts
    ):

        context = "\n".join(
            contexts
        )

        prompt = f"""
You are a Placement Intelligence Assistant.

Rules:
1. Use ONLY provided context.
2. If information is missing, say so.
3. If conflicting information exists, mention it.
4. Do not assume facts.

Context:
{context}

Question:
{question}

Answer:
"""

        return self.llm.generate(
            prompt
        )
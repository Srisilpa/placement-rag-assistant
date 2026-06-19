from src.llm.groq_client import GroqClient


class ResponseGenerator:

    def __init__(self):

        self.llm = GroqClient()

    def answer(
        self,
        question,
        contexts
    ):

        # Handle different formats safely

        if isinstance(contexts, dict):

            contexts = contexts.get(
                "documents",
                []
            )

        if not contexts:

            return (
                "I don't have enough information "
                "in the placement documents."
            )

        context_text = "\n\n".join(
            [str(chunk) for chunk in contexts]
        )

        prompt = f"""
You are a Placement Intelligence Assistant.

Instructions:

- Answer ONLY from the provided context.
- If information is unavailable, say so.
- If conflicting information exists, explain both values.
- Give concise and accurate answers.
- Mention package values in LPA.
- Use bullet points when appropriate.

CONTEXT:
{context_text}

QUESTION:
{question}

ANSWER:
"""

        return self.llm.generate(
            prompt
        )
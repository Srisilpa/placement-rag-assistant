from langchain_groq import ChatGroq
from src.core.config import Config


llm = ChatGroq(
    groq_api_key=Config.GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0
)


def generate_answer(
    context,
    question
):

    prompt = f"""
You are a placement assistant.

Context:
{context}

Question:
{question}

Answer using only the context.
"""

    response = llm.invoke(prompt)

    return response.content
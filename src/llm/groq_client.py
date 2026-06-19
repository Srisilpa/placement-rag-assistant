import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()


class GroqClient:

    def __init__(self):

        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def generate(self, prompt):

        response = self.llm.invoke(
            prompt
        )

        return response.content

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


class LangChainClient:

    def __init__(self):

        load_dotenv()

        # Obtener las variables de entorno
        api_key = os.getenv("GEMINI_API_KEY")
        model_name = os.getenv("GEMINI_MODEL")

        # Validar las variables
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY no está configurada en el archivo .env"
            )

        if not model_name:
            raise ValueError(
                "GEMINI_MODEL no está configurada en el archivo .env"
            )

        # Inicializar el modelo Gemini
        self.model = ChatGoogleGenerativeAI(
            model=model_name,
            api_key=api_key,
            max_output_tokens=1000
        )

    def generate_response(self, prompt: str) -> str:

        response = self.model.invoke(prompt)

        return response.content

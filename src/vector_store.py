import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

#Se carga las variables de entorno
load_dotenv()

#Recuperamos nuestra API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY no está configurada")

#Configuramos el modelo de embeddings
#esta es una configuracion de un modelo especializado en generar embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    google_api_key = api_key
)

#Definimos dónde almacenaremos nuestra base vectorial
BASE_DIR = Path(__file__).resolve().parent.parent

PERSIST_DIRECTORY = BASE_DIR / "chroma_db"

#Creamos nuestro vectore store
vector_store = Chroma(
    collection_name = "software_knowledge",
    embedding_function = embeddings,
    persist_directory = str(PERSIST_DIRECTORY)
)







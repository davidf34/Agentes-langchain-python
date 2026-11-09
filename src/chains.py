from langchain_core.output_parsers import StrOutputParser

from src.prompts import get_learning_prompt
from src.langchain_client import LangChainClient


def create_learning_chain():
    
    #Obtener la plantilla 
    prompt = get_learning_prompt()

    #obtener el modelo
    client = LangChainClient()

    #Crear el parser
    parser = StrOutputParser()

    #Conectar los componentes
    chain = prompt | client.model | parser

    return chain


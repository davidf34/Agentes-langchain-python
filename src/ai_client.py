import os                            #permite interactuar con funcionalidades del sistema operativo

from dotenv import load_dotenv       #carga las variables definifas en el archivo .env
from google import genai             #contiene las funcionalidades del SDK de Google
from google.genai import types       #contiene las funcionalidades del SDK de Google, esta importacion es mas que todo para que el SDK proporcione tipos y estructuras para configurar las solicitudes



class AIClient:
    #Metodo constructor
    def __init__(self):
        #cargar las variables del archivo .env
        load_dotenv()

        #Obtener las credenciales
        api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL")

        #Verificar que las credenciales estén configuradas
        if not api_key:
            raise ValueError("GEMINI_API_KEY no está configurada en el archivo .env")

        if not self.model:
            raise ValueError("GEMINI_MODEL no está configurada en el archivo .env")

        #Inicializar el cliente de Gemini
        self.client = genai.Client(api_key=api_key)

    def generate_response(
        self, 
        prompt:str,
        system_instruction: str = None, # Significa que el metodo acepta una instruccion de sistema opcional, que puede ser utilizada para guiar la respuesta del modelo.
        temperature: float = 0.2,
        max_output_tokens: int = 1000
        ) -> str:
        
       #Este es el objeto de configuracion que recibe gemini para generar contenido, en este caso se le pasa la instruccion de sistema, la temperatura y el maximo de tokens de salida.
        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=max_output_tokens
        )

        #Enviar la solicitud al modelo de Gemini
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=config #acá se incorpora a la solicitud la configuracion que se definió previamente
        )


        #Obtener el texto generado
        return response.text
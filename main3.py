from src.ai_client import AIClient


def main():
    # Crear una instancia del cliente
    ai = AIClient()

    # Definir nuestro prompt
    prompt = """
    Eres un ingeniero senior especializado en AI Engineering.

    Tu responsabilidad es enseñar conceptos técnicos
    de inteligencia artificial a desarrolladores backend.

    Reglas:
    - Explica los conceptos de forma clara.
    - Utiliza ejemplos prácticos.
    - No inventes información técnica.
    - Si no conoces una respuesta, indícalo.
    """

    # consultar al modelo de Gemini para generar una respuesta
    #response = ai.generate_response(prompt)

    user_prompt = input("\n¿Qué deseas aprender hoy? ")

    response = ai.generate_response(
        prompt=user_prompt,
        system_instruction=prompt,
        temperature=0.5,
        max_output_tokens=1000
    )


    # Mostrar la respuesta generada
    print("\n===== RESPUESTA DEL MODELO =====\n")
    print(response)

if __name__ == "__main__":
    main()
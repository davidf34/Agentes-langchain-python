
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.langchain_client import LangChainClient
from src.agent_tools import (
    multiply_numbers,
    substract_numbers
)

from src.agent_memory import(
    save_user_fact,
    get_user_facts
)


def main():

    client = LangChainClient()
    #Herramientas matematicas y de memoria
    tools = [
        multiply_numbers,
        substract_numbers,
        save_user_fact,
        get_user_facts
    ]

    # 1. Creamos el mecanismo de memoria
    checkpointer = InMemorySaver()

    # 2. Creamos el agente
    agent = create_agent(
        model=client.model,
        tools=tools,
        system_prompt="""
        Eres un asistente personal y matemático.

        Puedes realizar operaciones matemáticas
        utilizando las herramientas disponibles.

        También puedes recordar información del usuario.

        Reglas de memoria:
        - Cuando el usuario comparta un dato personal
          que quiera recordar, utiliza save_user_fact.
        - Cuando el usuario pregunte por información
          que hayas guardado, utiliza get_user_facts.
        - No inventes información sobre el usuario.
        - Si no tienes un dato guardado, dilo claramente.

        Reglas matemáticas:
        - Utiliza las herramientas cuando sean necesarias.
        - No inventes resultados de operaciones.
        - Puedes utilizar varias herramientas
        """,
        checkpointer=checkpointer
    )

    #Identificador de la conversacion
    thread_number = 1

    # 3. Identificador de nuestra conversación
    config = {
        "configurable": {
            "thread_id": f"conversacion_{thread_number}"
        }
    }

    print("===== AGENTE CON MEMORIA DE LARGO PLAZO =====")
    print("Comandos: 'nueva' para cambiar de conversación.")
    print("Escribe 'salir' para terminar.\n")

    while True:

        query = input("Tú: ")

        if query.lower() == "salir":
            break

        #Cambiamos de una conversación sin reiniciar Python
        if query.lower() == "nueva":
            thread_number += 1

            config = {
                "configurable": {
                    "thread_id": f"conversacion_{thread_number}"
                }
            }

            print("\nNueva conversación iniciada.\n")
            continue
            
        result = agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": query}
                ]
            },
            config=config
        )

        # 5. Extraemos la respuesta
        final_message = result["messages"][-1]
        content = final_message.content

        if isinstance(content, list):
            content = "\n".join(
                block["text"]
                for block in content
                if isinstance(block, dict)
                and block.get("type") == "text"
            )

        print(f"\nAgente: {content}\n")


if __name__ == "__main__":
    main()

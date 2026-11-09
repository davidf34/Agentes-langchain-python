
from langchain_core.messages import HumanMessage, ToolMessage

from src.langchain_client import LangChainClient
from src.agent_tools import multiply_numbers


def main():

    # 1. Inicializar el modelo
    client = LangChainClient()

    # 2. Registrar las herramientas
    tools = [multiply_numbers]

    # 3. Crear un mapa de herramientas
    tools_by_name = {
        tool.name: tool for tool in tools
    }

    # 4. Vincular herramientas con Gemini
    model_with_tools = client.model.bind_tools(tools)

    # 5. Enviar pregunta 
    query = "Multiplica 25000 por 48"

    ai_message = model_with_tools.invoke(query)

    # 6. Recuperar solicitudes de herramientas
    tool_calls = ai_message.tool_calls

    if not tool_calls:
        print("Gemini respondió sin solicitar herramientas:")
        print(ai_message.content)
        return

    # 7. Ejecutar herramientas
    tool_messages = []

    for tool_call in tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        selected_tool = tools_by_name[tool_name]

        result = selected_tool.invoke(tool_args)

        print(f"\nHerramienta ejecutada: {tool_name}")
        print(f"Resultado: {result}")

        # 8. Devolver resultado al modelo
        tool_message = ToolMessage(
            content=str(result),
            tool_call_id=tool_call["id"]
        )

        tool_messages.append(tool_message)

    # 9. Enviar historial al modelo
    messages = [
        HumanMessage(content=query),
        ai_message,
        *tool_messages
    ]

    # 10. Obtener respuesta final
    final_response = model_with_tools.invoke(messages)

    print("\n===== RESPUESTA FINAL DE GEMINI =====")
    print(final_response.content)


if __name__ == "__main__":
    main()

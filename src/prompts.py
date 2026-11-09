from langchain_core.prompts import ChatPromptTemplate       #Importamos el componente encargado de crear plantillas en los mensajes

def get_learning_prompt():
    prompt = ChatPromptTemplate.from_messages([ #Se crea una plantilla con diferentes tipos de mensajes, en este caso se definen dos tipos de mensajes: uno del sistema y otro del humano. El mensaje del sistema establece el rol del modelo y las reglas de enseñanza, mientras que el mensaje del humano proporciona la información específica sobre la tecnología, el concepto y el nivel del estudiante.
        (
            "system",
            """
            Eres un instructor senior especializado
            en desarrollo de software y AI Engineering.

            Tu objetivo es enseñar conceptos técnicos
            de forma clara y práctica.

            Adapta tus explicaciones al nivel del estudiante.
            Utiliza ejemplos de código cuando sea necesario.
            """
        ),

        (
            "human",
            """
            Tecnología: {technology}

            Concepto: {topic}

            Nivel del estudiante: {level}

            Explica el concepto y proporciona un ejemplo.
            """
        )
    ])

    return prompt
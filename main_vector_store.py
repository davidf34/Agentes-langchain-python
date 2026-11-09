from langchain_core.documents import Document
from src.vector_store import vector_store

def main():

    #1. Creamos nuestros docs
    documents = [
        Document(
            page_content = """
            Java es un lenguaje de programación orientado a objetos.
            Permite desarrollar aplicaciones empresariales,
            aplicaciones web y sistemas distribuidos.
            """,
            metadata = {
                "source" : "java.md",
                "topic" : "Java"
            }
        ),
        Document(
            page_content = """
            Spring Boot es un framewoek basado en Java
            que permite desarrollar aplicaciones empresariales
            y construir APIs REST de manera eficiente.
            """,
            metadata = {
                "source":"spring_boot,md",
                "topic":"Spring Boot"
            }
        ),
        Document(
            page_content="""
            Las bases de datos relacionales almacenan información
            utilizando tablas, filas y columnas.
            SQL permite consultar y manipular estos datos.
            """,
            metadata = {
                "source":"databases.md",
                "topic":"Databases"
            }
        )

    ]
    #2. Almacenamos los documentos en Chroma
    vector_store.add_documents(
        documents=documents,
        ids = ["java-001", "spring-001", "database-001"]
    )

    print("Documentos almacenados correctamente.")

    #3.Solicitamos una consulta
    query = input("\n¿Qué deseas consultar? ")

    #4. Buscamos los documentos más similares
    results = vector_store.similarity_search_with_score( #busca los docs mas similares semanticamente
        query,
        k=2    #cantidad maxima de documentos que queremos recuperar
    )

    #5.Mostramos los restulados
    print("\n===== RESULTADOS DE BUSQUEDA =======")

    for index, (document, score) in enumerate(results,start=1):
        print(f"\nRestulado {index}")
        print(f"Contenido: {document.page_content}")
        print(f"Metadata: {document.metadata}")
        print(f"Distancia: {score}")

if __name__ == "__main__":
    main()



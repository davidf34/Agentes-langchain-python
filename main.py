from src.chains import create_learning_chain


def main():

    chain = create_learning_chain()

    technology = input("¿Qué tecnología quieres aprender? ")
    topic = input("¿Qué tema quieres estudiar? ")
    level = input("¿Cuál es tu nivel? ")

    response = chain.invoke({

        "technology": technology,
        "topic": topic,
        "level": level

    })

    print("\n===== AI LEARNING ASSISTANT =====\n")
    print(response)


if __name__ == "__main__":
    main()
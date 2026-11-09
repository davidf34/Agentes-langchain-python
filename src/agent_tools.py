from langchain_core.tools import tool

@tool #el decorador convierte la funcion python en una herramienta reconocible por LangChain
def multiply_numbers(a: float, b: float) -> float:
    """
    Multiplica dos números y devuelve el resultado.
    Utiliza esta herramienta cuando el usuario solicite realizar una multiplicación de dos números.
    """
    return a * b


@tool
def substract_numbers(a: float, b: float) -> float:
    """
    Resta dos números y devuelve el resultado.
    Utiliza esta herramienta cuando el usuario solicite realizar una resta de dos números.
    """
    return a - b

@tool
def divide_numbers(a: float, b: float) -> float:
    """
    Divide el primer número entre el segundo
    """

    if b==0:
        return "No se puede dividir entre cero"

    return a/b



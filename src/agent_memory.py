#este archivo se encargará de almacenar y consultar la memoria a largo plazo
from langgraph.store.memory import InMemoryStore
from langchain_core.tools import tool


#1. creamos el almacenamiento
store = InMemoryStore() # Es nuestro almacenamiento, de momento usa RAM, no una BD

#2. Se define el espacio de memoria del user
namespace = ("david","memories") #Es una especie de nombres que permite organizar la info (imaginemos que tenemos una app con 1000 users, no queremos mezclar los recuerdos de unos con los de otros)

@tool
def save_user_fact(fact: str) -> str:
    """
    Guarda un dato importante sobre el usuario
    para poder recordarlo en futuras conversaciones
    """ 

    #Consultamos si ya existe un perfil

    item = store.get(namespace, "profile") #el Key que corresponde a "profile" es el identificador del registro que guardamos dentro del namespace
    #En ese caso se esta realizando un get en donde recupera la informacion guardada pero tambien se puede realizar un put en el cual guarda o actuliza info

    #Esta estructura de namespace, key y value es el mecanismo de almacenamiento documentado por LangGraph 

    if item:
        facts = item.value.get("facts",[])
    else:
        facts = []

    #Evitamos guardar data duplicada
    if fact not in facts:
        facts.append(fact)


    #Guardamos la info actualizada
    store.put(
        namespace,
        "profile",
        {"facts":facts}
    )
    return f"Información guardada correctamente: {fact}"


@tool
def get_user_facts() -> str:
    """
    Consulta los datos que tenemos guardados sobre el usuario
    """

    item = store.get(namespace, "profile")
    

    if not item:
        return "Todavía no hay información guardada."
    
    facts = item.value.get("facts", [])

    # Validamos si la lista está vacía
    if not facts:
        return "Todavía no hay información guardada."

    return "\n".join(f"- {fact}" for fact in facts)





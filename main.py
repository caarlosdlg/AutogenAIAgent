import os
import sys

# Configurar el directorio de caché solo en la raíz del proyecto
project_root = os.path.dirname(__file__)
os.environ["PYTHONPYCACHEPREFIX"] = os.path.join(project_root, "__pycache__")

# Deshabilitar caché en subdirectorios
sys.dont_write_bytecode = True

from core.agent_initializer import initialize_agents
from core.query_handler import handle_user_query

def main():
    print("=== Asistente de Búsqueda de Productos ===")
    print("Ingrese lo que desea buscar (o 'salir' para terminar):")
    
    try:
        assistant, user_proxy = initialize_agents()
    except Exception as e:
        print(e)
        return
    
    while True:
        user_query = input("\nBúsqueda: ")
        
        if user_query.lower() in ["salir", "exit", "q", "quit"]:
            print("¡Hasta pronto!")
            break
        
        handle_user_query(assistant, user_proxy, user_query)
        print("\n¿Desea realizar otra búsqueda?")


if __name__ == "__main__":
    main()

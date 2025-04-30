from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv
from tools.supabase_tool import query_supabase

# Load environment variables from .env file
load_dotenv()

def create_agents():
    """
    Crea y configura los agentes de AutoGen para la búsqueda en la base de datos.
    """
    # Definición formal de la herramienta para consultar la base de datos
    query_tool = {
        "type": "function",
        "function": {
            "name": "query_database",
            "description": "Busca productos en la base de datos por nombre o descripción",
            "parameters": {
                "type": "object",
                "properties": {
                    "query_text": {
                        "type": "string",
                        "description": "El texto de búsqueda para encontrar productos (ej. martillo, sierra, etc.)"
                    }
                },
                "required": ["query_text"]
            }
        }
    }
    
    # Configuración del modelo LLM
    config_list = [{
        "model": "gpt-4o-mini",
        "api_key": os.getenv("PROJ_API_KEY")
    }]
    
    # Crear el asistente con la herramienta configurada explícitamente
    assistant = AssistantAgent(
        name="database_query_agent",
        system_message="""
        Eres un asistente que busca información en una base de datos de productos.
        SIEMPRE debes usar la función query_database para consultar la información en la base de datos.
        NUNCA inventes información que no provenga de la base de datos.
        
        Tu trabajo es:
        1. Analizar lo que busca el usuario
        2. Usar la función query_database para obtener los datos de la base de datos
        3. Presentar la información obtenida de forma clara
        
        Cuando termines, finaliza con "TERMINATE".
        """,
        llm_config={
            "config_list": config_list,
            "tools": [query_tool]  # Especificar la herramienta directamente aquí
        }
    )
    
    # Crear el agente proxy con la función mapeada para ejecución
    user_proxy = UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,  # Reducir la cantidad de respuestas automáticas
        code_execution_config={"use_docker": False},
        function_map={"query_database": query_supabase}  # Mapear la función al método real
    )
    
    return assistant, user_proxy

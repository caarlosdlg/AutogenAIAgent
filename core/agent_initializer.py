from agents.agent_config import create_agents

def initialize_agents():
    """
    Inicializa los agentes assistant y user proxy.
    Retorna:
        Una tupla que contiene el assistant y el user proxy configurado.
    Lanza:
        Exception: Si falla la creación o configuración de los agentes.
    """
    try:
        assistant, user_proxy = create_agents()
        return assistant, user_proxy
    except Exception as e:
        raise Exception(f"Error al inicializar los agentes: {e}")

import autogen

def handle_user_query(assistant, user_proxy, user_query):
    """
    Maneja la consulta del usuario iniciando un chat grupal entre el assistant y el user proxy.
    Argumentos:
        assistant: El agente assistant.
        user_proxy: El agente user proxy.
        user_query: La consulta proporcionada por el usuario.
    """
    try:
        chat_result = autogen.group_chat(
            participants=[assistant, user_proxy],
            message=f"Necesito información sobre: {user_query}. Usa la función query_database para buscar en la base de datos.",
            max_turns=3,  # Limitar a menos intercambios
            is_termination_msg=lambda x: "TERMINATE" in x.get("content", "") if isinstance(x, dict) else "TERMINATE" in x,
        )
        print(f"Resultado del chat: {chat_result}")
    except Exception as e:
        print(f"Error durante la consulta: {str(e)}")

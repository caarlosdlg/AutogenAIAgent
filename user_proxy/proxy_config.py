def configure_user_proxy(user_proxy):
    """
    Configura el user proxy con las opciones necesarias.
    """
    # Aquí puedes agregar configuraciones específicas para el user proxy
    user_proxy.settings = {
        "timeout": 30,  # Configuración de tiempo de espera
        "retry_attempts": 3,  # Número de intentos de reintento
    }
    return user_proxy

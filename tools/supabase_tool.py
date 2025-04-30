from supabase import create_client
import config

def query_supabase(query_text: str) -> str:
    """
    Busca productos en la base de datos Supabase según el término de búsqueda.
    
    Args:
        query_text: Texto de búsqueda.
    
    Returns:
        Resultados de la búsqueda en formato legible.
    """
    print(f"Calling query_supabase tool with arguments\n\"{{\"query\":\"{query_text}\"}}\"")
    
    try:
        # Inicializar el cliente Supabase
        supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
        
        # Realizar la consulta a la base de datos
        # Ajusta el nombre de la tabla según tu configuración específica
        response = supabase.postgrest.from_('products').select('*').ilike('nombre', f'%{query_text}%').execute()
        
        # Procesar y formatear los resultados
        if hasattr(response, 'data'):
            data = response.data
            if data:
                # Mostrar los datos crudos para depuración
                print(f"Tool Result\n{data}")
                
                # Formatear los resultados para presentación
                formatted_results = []
                for item in data:
                    formatted_results.append(f"ID: {item.get('id')}")
                    formatted_results.append(f"Nombre: {item.get('nombre')}")
                    formatted_results.append(f"Precio: ${item.get('precio')}")
                    formatted_results.append(f"Cantidad disponible: {item.get('cantidad')} unidades")
                    formatted_results.append("-" * 30)
                
                return "\n".join(formatted_results)
            else:
                return "No se encontraron productos que coincidan con la búsqueda."
        else:
            return "Error: No se pudo procesar la respuesta de la base de datos."
    except Exception as e:
        error_message = f"Error al consultar la base de datos: {str(e)}"
        print(f"Tool Result\n{error_message}")
        return error_message

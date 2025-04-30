# Agente de Consulta de Base de Datos con AutoGen

Este proyecto implementa un asistente de IA usando AutoGen que puede buscar productos en una base de datos Supabase.

## 📂 Estructura del Proyecto

```
AutogenAIAgent/
├── agents/
│   ├── agent_config.py  # Configuración de agentes AutoGen
├── config/
│   ├── config.py        # Configuración y variables de entorno
│   ├── .env             # Variables de entorno (no se sube al repositorio)
├── tools/
│   ├── supabase_tool.py # Herramienta para consultas a Supabase
├── main.py              # Punto de entrada de la aplicación
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Documentación del proyecto
├── .gitignore           # Archivos ignorados por Git
```

## 📋 Requisitos Previos

- Python 3.8 o superior
- Cuenta en [Supabase](https://supabase.com/)
- Base de datos PostgreSQL con una tabla `products` configurada

## 🚀 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd AutogenAIAgent
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno**:
   Crea un archivo `.env` con las siguientes variables:
   ```
   SUPABASE_URL=tu_url_de_supabase
   SUPABASE_KEY=tu_api_key_de_supabase
   PROJ_API_KEY=tu_api_key_de_openai

   # Configuración de IA
   AI_CONFIG_PATH=agent_config.json
   AI_MODEL=gpt-4o-mini
   AI_TEMPERATURE=0.7
   ```

Reemplaza los valores con tus propias credenciales:
- `SUPABASE_URL`: URL de tu proyecto de Supabase
- `SUPABASE_KEY`: API key de tu proyecto de Supabase
- `PROJ_API_KEY`: API key de OpenAI para acceder a los modelos GPT
- `AI_CONFIG_PATH`: Ruta al archivo de configuración del agente (por defecto: `agent_config.json`)
- `AI_MODEL`: Modelo de IA a utilizar (por defecto: `gpt-4o-mini`)
- `AI_TEMPERATURE`: Parámetro de temperatura para las respuestas de IA (por defecto: `0.7`)

### Estructura de la Base de Datos

Asegúrate de tener una tabla `products` en tu base de datos Supabase con la siguiente estructura:

| Campo    | Tipo      | Descripción                  |
|----------|-----------|------------------------------|
| id       | integer   | Identificador único          |
| nombre   | text      | Nombre del producto          |
| precio   | numeric   | Precio del producto          |
| cantidad | integer   | Cantidad disponible          |

## 🖥️ Uso

Ejecuta el asistente con:
```bash
python main.py
```

Sigue las instrucciones en pantalla para realizar búsquedas en la base de datos.

Una vez iniciado, verás el siguiente mensaje:

```
=== Asistente de Búsqueda de Productos ===
Ingrese lo que desea buscar (o 'salir' para terminar):
```

Ejemplos de consultas:
- "martillo"
- "sierra"
- "destornillador"

Para salir del programa, escribe: "salir", "exit", "q" o "quit".

## 🛠️ Herramientas

- **Supabase**: Base de datos para almacenar productos.
- **AutoGen**: Framework para agentes de IA.

Desarrollado con ❤️ usando [AutoGen](https://github.com/microsoft/autogen) y [Supabase](https://supabase.com/)

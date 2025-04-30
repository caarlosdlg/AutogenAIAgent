import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
PROJ_API_KEY = os.getenv("PROJ_API_KEY")

# Validate required environment variables
if not all([SUPABASE_URL, SUPABASE_KEY, PROJ_API_KEY]):
    raise ValueError("Faltan variables de entorno requeridas")

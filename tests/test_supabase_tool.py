import unittest
from tools.supabase_tool import query_supabase

class TestSupabaseTool(unittest.TestCase):
    def test_query_supabase(self):
        # Simular una consulta válida
        result = query_supabase("martillo")
        self.assertIn("ID:", result)

    def test_query_supabase_no_results(self):
        # Simular una consulta sin resultados
        result = query_supabase("producto_inexistente")
        self.assertEqual(result, "No se encontraron productos que coincidan con la búsqueda.")

if __name__ == "__main__":
    unittest.main()

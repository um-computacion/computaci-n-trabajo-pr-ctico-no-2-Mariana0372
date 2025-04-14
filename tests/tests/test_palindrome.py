# tests/test_palindrome.py
import unittest
from src.palindrome import is_palindrome  # Asegúrate de que esta importación sea correcta

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        """Prueba palíndromos simples de una sola palabra."""
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("somos"))
        self.assertTrue(is_palindrome("1221"))

if __name__ == '__main__':
    unittest.main()

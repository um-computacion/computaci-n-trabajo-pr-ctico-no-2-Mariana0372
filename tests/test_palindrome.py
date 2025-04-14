import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_phrase_palindromes(self):
        """Prueba palíndromos que son frases completas."""
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Yo hago yoga hoy"))
        self.assertTrue(is_palindrome("¿Acaso hubo búhos acá?"))

if __name__ == '__main__':
    unittest.main()
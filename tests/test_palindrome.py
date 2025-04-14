feature/unificar-tests-palindromos

feature/tests-frases-palindromas


main
main
import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
feature/tests-frases-palindromas
    def test_phrase_palindromes(self):
        """Prueba palíndromos que son frases completas."""
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Yo hago yoga hoy"))
        self.assertTrue(is_palindrome("¿Acaso hubo búhos acá?"))
    def test_simple_palindromes(self):
        """Prueba palíndromos simples de una sola palabra."""
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("somos"))
        self.assertTrue(is_palindrome("1221"))
 main

    def test_phrase_palindromes(self):
        """Prueba palíndromos que son frases completas."""
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Yo hago yoga hoy"))
        self.assertTrue(is_palindrome("¿Acaso hubo búhos acá?"))

if __name__ == '__main__':
    unittest.main()

import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_non_palindromes(self):
        """Prueba casos que no son palíndromos."""
        self.assertFalse(is_palindrome("hola"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("universidad"))
        self.assertFalse(is_palindrome("Este no es un palíndromo"))
        self.assertFalse(is_palindrome("TDD es divertido"))

if __name__ == '__main__':
    unittest.main()
# test_palindrome.py

import unittest
from palindrome import is_palindrome  

# Tests para palíndromos simples
class TestPalindromeSimple(unittest.TestCase):

    def test_palindromo(self):
        self.assertTrue(is_palindrome("radar"))

    def test_no_palindromo(self):
        self.assertFalse(is_palindrome("hello"))

# Tests para frases palíndromas
class TestPalindromeFrase(unittest.TestCase):

    def test_palindromo_frase(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_no_palindromo_frase(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))

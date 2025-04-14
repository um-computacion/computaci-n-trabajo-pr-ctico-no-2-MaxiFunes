import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("rotor"))
        self.assertTrue(is_palindrome("deified"))
        self.assertTrue(is_palindrome("civic"))
        self.assertTrue(is_palindrome("radar"))
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))     
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("1"))
        self.assertTrue(is_palindrome("1A2b3B2a1"))
        self.assertFalse(is_palindrome("1A2b3B2a1!"))
        self.assertFalse(is_palindrome("12345"))
        self.assertFalse(is_palindrome("12321!"))
if __name__ == '__main__':
    unittest.main()
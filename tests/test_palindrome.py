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


if __name__ == '__main__':
    unittest.main()
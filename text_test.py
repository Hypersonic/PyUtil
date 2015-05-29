import unittest

from pyutil import text

class TestTextMethods(unittest.TestCase):
    def test_caesar_lowercase(self):
        before = 'abcdefghijklmnopqrstuvwxyz'
        expected =  'bcdefghijklmnopqrstuvwxyza'
        actual = text.caesar(before)
        self.assertEqual(actual, expected)

    def test_caesar_uppercase(self):
        before = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        expected =  'BCDEFGHIJKLMNOPQRSTUVWXYZA'
        actual = text.caesar(before)
        self.assertEqual(actual, expected)

    def test_caesar_mixedcase(self):
        before = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        expected =  'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'
        actual = text.caesar(before)
        self.assertEqual(actual, expected)
        
    def test_caesar_nonletter(self):
        before = '12345'
        expected =  '12345'
        actual = text.caesar(before)
        self.assertEqual(actual, expected)

    def test_caesar_empty(self):
        before = ''
        expected =  ''
        actual = text.caesar(before)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

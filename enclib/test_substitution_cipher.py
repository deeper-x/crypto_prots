import unittest
from enclib import substitution_cipher

class TestSubstitutionCipher(unittest.TestCase):
    def test_substitution_cipher(self):
        ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        expected = list(ltrs)
        subst_cipher = substitution_cipher.generate_key()
        got = list(subst_cipher.keys())

        self.assertEqual(expected, got)
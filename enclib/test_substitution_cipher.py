import unittest
from enclib import substitution_cipher

class TestSubstitutionCipher(unittest.TestCase):
    def test_substitution_cipher_gen_key(self) -> None:
        ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        expected = list(ltrs)
        subst_cipher = substitution_cipher.gen_enc_key()
        got = list(subst_cipher.keys())

        self.assertEqual(expected, got)
        
    def test_substitution_cipher_enc_dec(self) -> None:
        ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        enc_key: dict[str, str] = substitution_cipher.gen_enc_key()
        dec_key: dict[str, str] = substitution_cipher.gen_dec_key(enc_key)
        msg: str = "hello, world"
        
        encrypted: str = substitution_cipher.run(enc_key, msg)
        decrypted: str = substitution_cipher.run(dec_key, encrypted)
        
        self.assertEqual(encrypted, decrypted)
        
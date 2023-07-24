import unittest
from enclib import caesar


class TestCaesar(unittest.TestCase):
    def test_gen_enc_dec(self):
        got = caesar.gen_enc_key(1)
        expected = {
                    'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G',
                    'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M',
                    'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
                    'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y',
                    'Y': 'Z', 'Z': 'a', 'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e',
                    'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
                    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q',
                    'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w',
                    'w': 'x', 'x': 'y', 'y': 'z', 'z': 'A'
                    }
        self.assertEqual(got, expected)

    def test_gen_dec_key(self):
        enc_key = expected = {
                    'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G',
                    'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M',
                    'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
                    'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y',
                    'Y': 'Z', 'Z': 'a', 'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e',
                    'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
                    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q',
                    'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w',
                    'w': 'x', 'x': 'y', 'y': 'z', 'z': 'A'
                    }

        got = caesar.gen_dec_key(enc_key)

        expected = {'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E', 'G': 'F',
                    'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K', 'M': 'L',
                    'N': 'M', 'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q', 'S': 'R',
                    'T': 'S', 'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X',
                    'Z': 'Y', 'a': 'Z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd',
                    'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j',
                    'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p',
                    'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v',
                    'x': 'w', 'y': 'x', 'z': 'y', 'A': 'z'
                    }

        self.assertEqual(got, expected)

    def test_encrypt(self):
        enc_key = {
                    'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G',
                    'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M',
                    'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
                    'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y',
                    'Y': 'Z', 'Z': 'a', 'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e',
                    'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
                    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q',
                    'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w',
                    'w': 'x', 'x': 'y', 'y': 'z', 'z': 'A'
                    }

        got = caesar.run(enc_key, "hello, test")
        expected = "ifmmp, uftu"

        self.assertEqual(got, expected)

    def test_break_it(self):
        expected = ['Gdkkn, Vnqkc!', 'Fcjjm, Umpjb!', 'Ebiil, Tloia!', 'Dahhk, SknhZ!', 'CZggj, RjmgY!', 'BYffi, QilfX!', 'AXeeh, PhkeW!', 'zWddg, OgjdV!', 'yVccf, NficU!', 'xUbbe, MehbT!', 'wTaad, LdgaS!', 'vSZZc, KcfZR!', 'uRYYb, JbeYQ!', 'tQXXa, IadXP!', 'sPWWZ, HZcWO!', 'rOVVY, GYbVN!', 'qNUUX, FXaUM!', 'pMTTW, EWZTL!', 'oLSSV, DVYSK!', 'nKRRU, CUXRJ!', 'mJQQT, BTWQI!', 'lIPPS, ASVPH!', 'kHOOR, zRUOG!', 'jGNNQ, yQTNF!', 'iFMMP, xPSME!']
        got = caesar.break_it("Hello, World!")
        print(got)
        self.assertEqual(expected, got)
        
if __name__ == "__main__":
    unittest.main()

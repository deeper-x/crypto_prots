import unittest
from enclib import stream_cipher


class TestStreamCipher(unittest.TestCase):
    def testEncrypt(self) -> None:
        ks: stream_cipher.Keystream = stream_cipher.Keystream()
        res: bytes = stream_cipher.encrypt(ks, "hello, world")

        self.assertEqual(res, b'\xce\x82\xf8Q]\xaf N\x11\xad@\x91')

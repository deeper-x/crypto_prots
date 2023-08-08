import unittest
from enclib import stream_cipher


class TestStreamCipher(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super(TestStreamCipher, self).__init__(*args, **kwargs)

        self.encr_var: bytes = b'\xfebH\x11\r\xcf\xf0\xce\x81\rP\xd1'
        self.decr_var: str = "hello, world"

    def testEncrypt(self) -> None:
        ks: stream_cipher.Keystream = stream_cipher.Keystream()

        got: bytes = ks.encrypt(self.decr_var.encode())
        expected: bytes = self.encr_var

        self.assertEqual(got, expected)

    def testDecrypt(self) -> None:
        ks: stream_cipher.Keystream = stream_cipher.Keystream()

        got: str = ks.decrypt(self.encr_var)
        expected: str = self.decr_var

        self.assertEqual(got, expected)

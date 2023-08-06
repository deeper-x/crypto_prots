import unittest
from enclib import one_time_pad


class TestOneTimePad(unittest.TestCase):
    def test_encrypt_decrypt(self) -> None:
        en_msg: bytes = "alberto ok".encode()
        lmsg: int = len(en_msg)
        ks: bytes = one_time_pad.get_key_stream(lmsg)

        cipher: bytes = one_time_pad.encrypt(ks, en_msg)
        clean: bytes = one_time_pad.decrypt(cipher, ks)

        self.assertEqual(en_msg, clean)

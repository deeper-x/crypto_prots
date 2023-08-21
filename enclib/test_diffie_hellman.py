import unittest
from enclib import settings
from enclib import diffie_hellman
from typing import cast


class TestDiffieHellman(unittest.TestCase):
    def test_private_keys(self) -> None:
        p = diffie_hellman.get_random_prime(settings.START_RANGE, settings.STOP_RANGE)
        self.assertIsNotNone(p)
        p_int: int = cast(int, p)

        g = diffie_hellman.get_generator(p_int)
        self.assertIsNotNone(g)
        g_int: int = cast(int, g)

        # PUBLIC KEYS
        # alice
        a_token: int = diffie_hellman.gen_random_value(settings.START_RANGE, settings.STOP_RANGE)
        a_pub: int = diffie_hellman.gen_pub_key(a_token, p_int, g_int)
        # bob
        b_token: int = diffie_hellman.gen_random_value(settings.START_RANGE, settings.STOP_RANGE)
        b_pub: int = diffie_hellman.gen_pub_key(b_token, p_int, g_int)

        # PRIVATE KEYS
        # alice
        a_priv: int = diffie_hellman.gen_priv_key(b_pub, a_token, p_int)
        # bob
        b_priv: int = diffie_hellman.gen_priv_key(a_pub, b_token, p_int)

        self.assertEqual(a_priv, b_priv)

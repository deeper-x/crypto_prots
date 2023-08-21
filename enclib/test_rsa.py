from enclib import rsa
import unittest


class TestRSA(unittest.TestCase):
    def test_encrypt_decrypt(self):
        size = 300
        p = rsa.get_prime(size)
        q = rsa.get_prime(size)

        # compute n = q*p
        n = q*p

        # compute lambda
        lambda_n = rsa.lcm(p-1, q-1)

        # compute public exponent
        e = rsa.get_e(lambda_n)

        # solve for d, the equation de ≡ 1 (mod λ(n))
        d = rsa.get_d(e, lambda_n)

        # print("public key", e, n)
        # print("secret key", d)

        # bob message
        m_b = 117
        c = m_b**e % n
        # print("bob sends {msg} which is encrypted as \"{enc}\"".format(msg=m_b, enc=c))

        # alice decrypts
        m_a = c**d % n
        # print("alice decrypts message, which is {msg}".format(msg=m_a))
        self.assertEqual(m_a, m_b)

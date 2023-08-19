from typing import Optional
from enclib import generator
import random


def is_prime(n_in: int) -> bool:
    """Tells if a given number is prime

    Args:
        n_in (int): input number, integer

    Returns:
        bool: True if it's prime, False otherwise
    """

    if n_in == 1:
        return False
    elif n_in > 1:
        for i in range(2, n_in):
            if n_in % i == 0:
                return False
        return True
    else:
        return False


def get_random_prime(start: int, stop: int) -> Optional[int]:
    """Recursive function for generating a random prime number in a given range

    Args:
        in_random (int): range for generating random number

    Returns:
        Optional[int]: prime number. None if not founded
    """

    cur: int = gen_random_value(start, stop)

    if is_prime(cur):
        return cur

    get_random_prime(start, stop)

    return start


def gen_random_value(start: int, stop: int) -> int:
    """generate a random value in a given range

    Args:
        start (int): start range
        stop (int): stop range

    Returns:
        int: random number
    """
    res: int = random.randrange(start, stop)

    return res


def get_generator(p: int) -> Optional[int]:
    """found the generator value, for a given integer p

    Args:
        p (int): integer you want to find the generator value

    Returns:
        Optional[int]: generator value, if any
    """

    seq: generator.Sequence = generator.Sequence(p)

    return seq.g


def gen_pub_key(r: int, p: int, g: int) -> int:
    """generate public key, starting from a random integer used as exponent, a random prime
    number and its generator

    Args:
        r (int): random integer
        p (int): random prime number
        g (int): generator

    Returns:
        int: public key
    """
    res: int = (g**r) % p

    return res


def gen_priv_key(pub_key: int, priv_token: int, prime_num: int) -> int:
    """generate a private key, starting from a public key, a private token and a random
    prime number

    Args:
        pub_key (int): public key
        priv_num (int): private token
        prime_num (int): prime number

    Returns:
        int: private key
    """
    return (pub_key**priv_token) % prime_num

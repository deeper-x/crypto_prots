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


def get_random_prime(in_random: int) -> Optional[int]:
    """Recursive function for generating a random prime number in a given range

    Args:
        in_random (int): range for generating random number

    Returns:
        Optional[int]: prime number. None if not founded
    """

    cur: int = random.randrange(3, in_random)
    if is_prime(cur):
        return cur

    get_random_prime(in_random)

    return None


def get_generator(p: int) -> Optional[int]:
    seq: generator.Sequence = generator.Sequence(p)

    return seq.g

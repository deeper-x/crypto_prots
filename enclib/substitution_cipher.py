import random


def gen_enc_key() -> dict[str, str]:
    ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list_ltrs = list(ltrs)
    key: dict[str, str] = {}

    for i in ltrs:
        key[i] = list_ltrs.pop(random.randint(0, len(list_ltrs)-1))

    return key


def gen_dec_key(enc_key: dict[str, str]) -> dict[str, str]:
    """given the encryption key, returns its decryption key

    Args:
        enc_key (dict[str, str]): encryption key dictionary

    Returns:
        dict[str, str]: decryption key dictionary
    """

    dec_key: dict[str, str] = {}

    for i in enc_key.items():
        dec_key[i[1]] = i[0]

    return dec_key


def run(key: dict[str, str], message: str) -> str:
    """given a clean message, encrypts it based on input key dict. Given an 
       encrypted message, it returns its decrypted version, based on input key

    Args:
        key (dict[str, str]): dictionary with encrypted/clean -> dec/enc
        message (str): clean/encrypted string

    Returns:
        str: encrypted/decrypted message, based on input
    """
    res: str = ""

    for i in message:
        if i in key:
            res += key[i]
        else:
            res += i

    return res


if __name__ == "__main__":
    enc_key: dict[str, str] = gen_enc_key()
    print(enc_key)
    dec_key: dict[str, str] = gen_dec_key(enc_key)
    print(dec_key)

    encrypted: str = run(enc_key, "HELLO, WORLD!")
    print(encrypted)

    decrypted: str = run(dec_key, encrypted)
    print(decrypted)
    """OUTPUT:

    {'A': 'T', 'B': 'Z', 'C': 'X', 'D': 'G', 'E': 'J', 'F': 'C', 'G': 'W',
    'H': 'O', 'I': 'H', 'J': 'N', 'K': 'E', 'L': 'L', 'M': 'U', 'N': 'B',
    'O': 'Y', 'P': 'I', 'Q': 'R', 'R': 'S', 'S': 'Q', 'T': 'F', 'U': 'A',
    'V': 'K', 'W': 'M', 'X': 'V', 'Y': 'P', 'Z': 'D'}
    {'T': 'A', 'Z': 'B', 'X': 'C', 'G': 'D', 'J': 'E', 'C': 'F', 'W': 'G',
    'O': 'H', 'H': 'I', 'N': 'J', 'E': 'K', 'L': 'L', 'U': 'M', 'B': 'N',
    'Y': 'O', 'I': 'P', 'R': 'Q', 'S': 'R', 'Q': 'S', 'F': 'T', 'A': 'U',
    'K': 'V', 'M': 'W', 'V': 'X', 'P': 'Y', 'D': 'Z'}

    OJLLY, MYSLG!
    HELLO, WORLD!
    """

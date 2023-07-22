def gen_enc_key(n: int) -> dict[str, str]:
    """given an input value of shift, it returns a dict mapping
    each alphab-letter to the correspondant key-letter

    Args:
        n (int): the shift value

    Returns:
        dict[str, str]: the resulting dict, where each clean letter
        is linked to its value
    """

    res: dict[str, str] = {}
    counter: int = 0
    alphab: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    for i in alphab:
        nidx: int = (counter + n) % len(alphab)
        res[i] = alphab[nidx]

        counter += 1

    return res


def gen_dec_key(enc_key: dict[str, str]) -> dict[str, str]:
    """given an encryption key in input, it returns its decryption key

    Args:
        enc_key (dict[str, str]): encryption key from where you
        generate decryption key

    Returns:
        dict[str, str]: decryption key
    """

    res: dict[str, str] = {}
    for k in enc_key:
        res[enc_key[k]] = k

    return res


def encrypt(key_dict: dict[str, str], message: str) -> str:
    """given the key and a clean message, returns its ciphered version

    Args:
        key_dict (dict[str, str]): encryption dictionary
        message (str): clean message

    Returns:
        str: ciphered message
    """

    res: str = ""
    for c in message:
        if c in key_dict:
            res += key_dict[c]
        else:
            res += c

    return res



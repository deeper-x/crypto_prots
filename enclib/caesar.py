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


def run(key_dict: dict[str, str], message: str) -> str:
    """given the encryption key and a clean message, returns its ciphered
    version. Given a decription key and a ciphered message, returns the
    decrypted message

    Args:
        key_dict (dict[str, str]): encryption dict | decryption dict
        message (str): clean message if used for encryption, enc message if
        used for decryption

    Returns:
        str: ciphered message for decryption, clean message for decryption
    """

    res: str = ""
    for c in message:
        if c in key_dict:
            res += key_dict[c]
        else:
            res += c

    return res


def break_it(enc_str: str) -> list[str]:
    """given an input ciphere message, it returns all possible
    decrypted messages

    Args:
        enc_str (str): encrypted message

    Returns:
        list: list of all possible solutions, for the given space
    """

    res = []
    for i in range(1, 26):
        key_enc_break: dict[str, str] = gen_enc_key(i)
        key_dec_break: dict[str, str] = gen_dec_key(key_enc_break)
        dec_break: str = run(key_dec_break, enc_str)
        res.append(dec_break)

    return res

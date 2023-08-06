import random


def gen_key_stream(size: int) -> bytes:
    """generate a key stream of a given size

    Args:
        size (int): fixed size of key

    Returns:
        bytes: one time pad key, as an array of bytes
    """

    res = bytes(random.randrange(0, size) for i in range(0, size))

    return res


def xor(one: bytes, two: bytes) -> bytes:
    """given two input bytes lists, it performs xor over them

    Args:
        one (bytes): bytes list one
        two (bytes): bytes list two

    Returns:
        bytes: XOR bytes list
    """
    mlen: int = min(len(one), len(two))

    return bytes([one[i] ^ two[i] for i in range(mlen)])


def encrypt(key_stream: bytes, en_msg: bytes) -> bytes:
    """given an encoded message, it encrypts based on input key stream

    Args:
        key_stream (bytes): input key stream for encryption
        en_msg (bytes): UTF-8 encoded message to encrypt

    Raises:
        Exception: when key stream and encoded message of different lengths  

    Returns:
        bytes: encrypted bytes
    """
    res: bytes = bytes(0)

    try:
        lks: int = len(key_stream)
        lmsg: int = len(en_msg)

        if lks != lmsg:
            err_msg: str = "key_stream's wrong length: {lks} instead of {lmsg}".format(
                lks=lks,
                lmsg=lmsg
            )

            raise Exception(err_msg)

        res = xor(key_stream, en_msg)

        return res

    except Exception as err:
        print("Error: {err}".format(err=err))
        return res


def decrypt(cipher: bytes, key_stream: bytes) -> bytes:
    """given a cipher and a key stream, it returns the decoded bytes

    Args:
        cipher (bytes): input cipher to decrypt
        key_stream (bytes): key stream used for decryption

    Returns:
        bytes: decrypted bytes
    """
    res: bytes = bytes(0)
    try:
        lks: int = len(cipher)
        lmsg: int = len(key_stream)

        if lks != lmsg:
            err_msg: str = "key_stream's wrong length: {lks} insteaf of {lmsg}".format(
                lks=lks,
                lmsg=lmsg,
            )

            raise Exception(err_msg)

        return xor(cipher, key_stream)

    except Exception as err:
        print("Error: {err}".format(err=err))
        return res

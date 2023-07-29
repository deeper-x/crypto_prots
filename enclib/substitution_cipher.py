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
    """given a clean message, encrypts it based on input key dict. Given an encrypted message, it returns its decrypted version, based on input key

    Args:
        key (dict[str, str]): dictionary with encrypted/clean -> decrypted/encrypted
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


def decrypt(enc_key: dict[str, str], message: str) -> str:
    """given an ciphered message, decrypts it based on input key dict

    Args:
        enc_key (dict[str, str]): encryption key
        message (str): ciphered message

    Returns:
        str: clean message
    """

    res: str = ""
        
    dec_key: dict[str, str] = gen_dec_key(enc_key)

    
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
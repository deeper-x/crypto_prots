from enclib.caesar import encrypt, gen_enc_key, gen_dec_key

if __name__ == "__main__":
    key_dict = gen_enc_key(7)

    print(key_dict)
    enc = encrypt(key_dict, "Hello, World!")
    print(enc)

    dec_dict: dict[str, str] = gen_dec_key(key_dict)
    dec = encrypt(dec_dict, enc)

    print(dec)

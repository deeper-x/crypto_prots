from enclib import caesar

if __name__ == "__main__":
    # 1 - caesar cipher
    key_dict: dict[str, str] = caesar.gen_enc_key(7)
    print(key_dict)

    enc: str = caesar.run(key_dict, "Hello, World!")
    print(enc)

    dec_dict: dict[str, str] = caesar.gen_dec_key(key_dict)
    dec: str = caesar.run(dec_dict, enc)
    print(dec)

    res_break: list[str] = caesar.break_it(enc)
    print(res_break)

    # OUTPUT:
    #     {
    #      'A': 'H', 'B': 'I', 'C': 'J', 'D': 'K', 'E': 'L',
    #      'F': 'M', 'G': 'N',
    #      'H': 'O', 'I': 'P', 'J': 'Q', 'K': 'R', 'L': 'S',
    #      'M': 'T', 'N': 'U',
    #      'O': 'V', 'P': 'W', 'Q': 'X', 'R': 'Y', 'S': 'Z',
    #      'T': 'a', 'U': 'b',
    #      'V': 'c', 'W': 'd', 'X': 'e', 'Y': 'f', 'Z': 'g',
    #      'a': 'h', 'b': 'i',
    #      'c': 'j', 'd': 'k', 'e': 'l', 'f': 'm', 'g': 'n',
    #      'h': 'o', 'i': 'p',
    #      'j': 'q', 'k': 'r', 'l': 's', 'm': 't', 'n': 'u',
    #      'o': 'v', 'p': 'w',
    #      'q': 'x', 'r': 'y', 's': 'z', 't': 'A', 'u': 'B',
    #      'v': 'C', 'w': 'D',
    #      'x': 'E', 'y': 'F', 'z': 'G'
    #      }

    #     Olssv, dvysk!
    #     Hello, World!

    #    ['Nkrru, cuxrj!', 'Mjqqt, btwqi!', 'Lipps, asvph!', 'Khoor, Zruog!',
    #     'Jgnnq, Yqtnf!', 'Ifmmp, Xpsme!', 'Hello, World!', 'Gdkkn, Vnqkc!',
    #     'Fcjjm, Umpjb!', 'Ebiil, Tloia!', 'Dahhk, SknhZ!', 'CZggj, RjmgY!',
    #     'BYffi, QilfX!', 'AXeeh, PhkeW!', 'zWddg, OgjdV!', 'yVccf, NficU!',
    #     'xUbbe, MehbT!', 'wTaad, LdgaS!', 'vSZZc, KcfZR!', 'uRYYb, JbeYQ!',
    #     'tQXXa, IadXP!', 'sPWWZ, HZcWO!', 'rOVVY, GYbVN!', 'qNUUX, FXaUM!',
    #     'pMTTW, EWZTL!']

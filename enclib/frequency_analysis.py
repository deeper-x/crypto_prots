from collections import defaultdict
from typing import Dict


def run(msg: str) -> Dict[str, float]:
    """Given an encrypted ciphered message, it computes frequency analisys,
    returning detailed report (letter=%frequency)

    Args:
        msg (str): ciphered msg

    Returns:
        str: frequency analisys
    """

    alphab: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    container: defaultdict[str, float] = defaultdict(int)
    tot_letters = 0

    for i in msg:
        if i in alphab:
            tot_letters += 1
            container[i] += 1

    for i in container:
        container[i] = container[i] / tot_letters

    return container


if __name__ == "__main__":
    cipher: str = """DRO BOCMEO WSCCSYX GSVV ECO K ROVSMYZDOB,
    KBBSFSXQ KD XYYX DYWYBBYG.
    LO BOKNI DY LBOKU YED KC CYYX
    KC IYE ROKB DRBOO
    LVKCDC YX K GRSCDVO.
    S'VV LO GOKBSXQ K BON KBWLKXN."""

    print(run(cipher))


# OUTPUT:
# defaultdict(<class 'int'>, {
    # 'D': 0.06818181818181818,
    # 'R': 0.03787878787878788,
    # 'O': 0.12121212121212122,
    # 'B': 0.09848484848484848,
    # 'C': 0.07575757575757576,
    # 'M': 0.015151515151515152,
    # 'E': 0.030303030303030304,
    # 'W': 0.022727272727272728,
    # 'S': 0.06818181818181818,
    # 'Y': 0.09848484848484848,
    # 'X': 0.06060606060606061,
    # 'G': 0.030303030303030304,
    # 'V': 0.05303030303030303,
    # 'K': 0.10606060606060606,
    # 'Z': 0.007575757575757576,
    # 'F': 0.007575757575757576,
    # 'Q': 0.015151515151515152,
    # 'L': 0.03787878787878788,
    # 'N': 0.022727272727272728,
    # 'I': 0.015151515151515152,
    # 'U': 0.007575757575757576})

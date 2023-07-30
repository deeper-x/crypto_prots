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
# Result:
# D 0.0682  R 0.0379  O 0.1212  B 0.0985
# C 0.0758  M 0.0152  E 0.0303  W 0.0227
# S 0.0682  Y 0.0985  X 0.0606  G 0.0303
# V 0.0530  K 0.1061  Z 0.0076  F 0.0076
# Q 0.0152  L 0.0379  N 0.0227  I 0.0152
# U 0.0076

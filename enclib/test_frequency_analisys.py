import unittest
from typing import Dict
from enclib import frequency_analysis


class TestFrequencyAnalisys(unittest.TestCase):
    def test_run_analisys(self) -> None:
        cipher: str = """DRO BOCMEO WSCCSYX GSVV ECO K ROVSMYZDOB,
KBBSFSXQ KD XYYX DYWYBBYG.
LO BOKNI DY LBOKU YED KC CYYX
KC IYE ROKB DRBOO
LVKCDC YX K GRSCDVO.
S'VV LO GOKBSXQ K BON KBWLKXN."""

        expected: Dict[str, float] = {
            'D': 0.06818181818181818,
            'R': 0.03787878787878788,
            'O': 0.12121212121212122,
            'B': 0.09848484848484848,
            'C': 0.07575757575757576,
            'M': 0.015151515151515152,
            'E': 0.030303030303030304,
            'W': 0.022727272727272728,
            'S': 0.06818181818181818,
            'Y': 0.09848484848484848,
            'X': 0.06060606060606061,
            'G': 0.030303030303030304,
            'V': 0.05303030303030303,
            'K': 0.10606060606060606,
            'Z': 0.007575757575757576,
            'F': 0.007575757575757576,
            'Q': 0.015151515151515152,
            'L': 0.03787878787878788,
            'N': 0.022727272727272728,
            'I': 0.015151515151515152,
            'U': 0.007575757575757576
        }

        got: Dict[str, float] = frequency_analysis.run(cipher)
        self.maxDiff = None
        self.assertEqual(expected, got)

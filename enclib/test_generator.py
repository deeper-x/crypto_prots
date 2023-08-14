from typing import Optional
import unittest

from enclib import generator


class TestGenerator(unittest.TestCase):
    def selfAssertGet(self) -> None:
        # cg: Generator = Generator(7, 3)
        # print(cg.get_sequence())

        cg: generator.Sequence = generator.Sequence(7, 3)
        expected: list[int] = [1, 3, 2, 6, 4, 5]
        got: Optional[list[int]] = cg.get()

        self.assertEqual(expected, got)

from typing import Optional
import unittest

from enclib import generator


class TestGenerator(unittest.TestCase):
    def test_get_valid(self) -> None:
        cg: generator.Sequence = generator.Sequence(7, 3)
        expected: list[int] = [1, 3, 2, 6, 4, 5]
        got: Optional[list[int]] = cg.get()

        self.assertEqual(expected, got)

    def test_get_None(self) -> None:
        cg: generator.Sequence = generator.Sequence(100, 2)
        expected: None = None
        got: Optional[list[int]] = cg.get()

        self.assertEqual(expected, got)

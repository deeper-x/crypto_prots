from typing import Optional
import unittest

from enclib import generator


class TestGenerator(unittest.TestCase):
    def test_valid(self) -> None:
        cg: generator.Sequence = generator.Sequence(7)
        # result is [1, 3, 2, 6, 4, 5]
        expected: bool = True
        got: bool = cg.is_valid()

        self.assertEqual(expected, got)

    def test_non_valid(self) -> None:
        cg: generator.Sequence = generator.Sequence(129)
        expected: bool = False
        got: bool = cg.is_valid()

        self.assertEqual(expected, got)

    def test_get(self) -> None:
        cg: generator.Sequence = generator.Sequence(7)
        expected: list[int] = [1, 3, 2, 6, 4, 5]
        got: Optional[list[int]] = cg.get()

        self.assertEqual(expected, got)

    def test_get_generator(self) -> None:
        cg: generator.Sequence = generator.Sequence(7)
        expected: Optional[int] = 3
        got: Optional[int] = cg.g

        self.assertEqual(expected, got)

    def test_get_None(self) -> None:
        cg: generator.Sequence = generator.Sequence(100)
        expected: None = None
        got: Optional[list[int]] = cg.get()

        self.assertEqual(expected, got)

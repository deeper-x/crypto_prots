from typing import Optional


class Sequence():
    def __init__(self, p: int, g: int) -> None:
        self.__p: int = p
        self.__g: int = g
        self.__res: list[int] = []

    def get(self) -> Optional[list[int]]:
        """generate a sequence starting from g, modulus p

        Returns:
            list[int]: generator sequence
        """

        for i in range(self.__p-1):
            self.__res.append(self.__g**i % self.__p)

        if self.__is_valid():
            return self.__res

        return None

    def __is_valid(self) -> bool:
        """given an input sequence, checks if it's a valid generator's result.

        Returns:
            bool: True if is a generator's sequence, False otherwise
        """

        res: bool = False
        check_set: set[int] = set()

        # each sequence's element is added to a set, if the element is between
        # 0 and the maximum possible value of the list
        # e.g: [1, 4, 5, 2, 3], or [1, 3, 2] or [1, 4, 5, 2, 3]
        # So, in_seq is considered valid only if built on a valid succession of
        # incremental numbers, with step 1
        for i in self.__res:
            if i > 0 and i <= len(self.__res):
                check_set.add(i)

        if len(check_set) == len(self.__res):
            res = True

        return res

from typing import Optional


class Sequence():
    def __init__(self, p: int) -> None:
        self.__p: int = p
        self.__g: Optional[int]

        # searching for generator g, which is < p, if any
        for g in range(self.__p):
            self.__g = g
            self.__res: list[int] = []

            for i in range(self.__p-1):
                self.__res.append(g**i % self.__p)

            # as soon as you find it, exit
            if self.is_valid():
                break

    @property
    def g(self) -> Optional[int]:
        return self.__g

    def get(self) -> Optional[list[int]]:
        """generate a sequence starting from g, modulus p

        Returns:
            list[int]: generator sequence
        """

        if self.is_valid():
            return self.__res

        return None

    def is_valid(self) -> bool:
        """given an input sequence, checks if it's a valid generator's result.

        Returns:
            bool: True if is a generator's sequence, False otherwise
        """

        res: bool = False
        check_set: set = set()

        # use a set in order to check if it's a valid generator sequence
        # input:    [1, 3, 2, 6, 4, 5]
        # set:      (1, 3, 2, 6, 4, 5)
        for i in self.__res:
            if i > 0 and i <= len(self.__res):
                check_set.add(i)

        if len(check_set) == len(self.__res):
            res = True

        return res

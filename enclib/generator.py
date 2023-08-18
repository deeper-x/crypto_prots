from typing import Optional


class Sequence():
    def __init__(self, p: int, g: int) -> None:
        self.__p: int = p
        self.__g: int = g
        self.__res: list[int] = []
        for i in range(self.__p-1):
            self.__res.append(self.__g**i % self.__p)

    def get(self) -> Optional[list[int]]:
        """generate a sequence starting from g, modulus p

        Returns:
            list[int]: generator sequence
        """

        if self.__is_valid():
            return self.__res

        return None

    def __is_valid(self) -> bool:
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


if __name__ == "__main__":
    c: Sequence = Sequence(7, 3)
    print(c.get())

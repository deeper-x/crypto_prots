class Keystream():
    """class for pseudorandom generation of a keystream cipher sequence.
    Based on LCG (Linear Congruential Generator) algorithm,
    expressed as ANSI C implementation `Xn+1 ≡ (A⋅Xn + C) mod M`
    where:
    X: the sequence of pseudorandom values
    n: 1
    A: 1103515245
    M: 2**31
    C: 2345
    """

    __A: int = 1103515245
    __M: int = 2**31
    __C: int = 2345
    __next: int

    def __init__(self, next: int = 1) -> None:
        """initialize pseudorandom sequence, with seed=1.

        Args:
            next (int, optional): Seeding value. Defaults to 1, as of ANSI specs for LCG.
        """

        self.__next = next

    def __get_next_x(self) -> int:
        """get next value of sequence in x, as of in `Xn+1 ≡ (A⋅Xn + C) mod M`.
        Everything is `modulus 256` in order to be 1-byte (0->255 values) fully compliant

        Returns:
            int: next value in sequence
        """

        self.__next = ((self.__next * self.__A + self.__C) % self.__M) % 256
        return self.__next

    def __xor_stream(self, in_stream: bytes) -> bytes:
        """performs xor on input stream, based on a given LCG sequence

        Args:
            in_stream (bytes): input stream to decrypt/encrypt

        Returns:
            bytes: xor result on input stream / pseudorandom sequence
        """

        return bytes(in_stream[i] ^ self.__get_next_x() for i in range(len(in_stream)))

    def encrypt(self, utf8_msg: bytes) -> bytes:
        """given an input message, performs XOR encryption byte-by-byte

        Args:
            msg (bytes): clean message in bytes

        Returns:
            bytes: encrypted message, in bytes
        """

        return self.__xor_stream(utf8_msg)

    def decrypt(self, utf8_msg: bytes) -> str:
        """decrypts message

        Args:
            utf8_msg (bytes): input cipher bytes

        Returns:
            str: decrypted string
        """

        return self.__xor_stream(utf8_msg).decode()

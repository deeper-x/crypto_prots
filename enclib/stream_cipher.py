class Keystream():
    def __init__(self, next: int = 1) -> None:
        self._next = next

    def _rand(self) -> int:
        self._next = (self._next * 1103515245 + 12345) % 2**31

        return self._next

    def get_key_byte(self) -> int:
        return self._rand() % 256


def encrypt(key: Keystream, message: str):
    enc_message: bytes = message.encode()

    return bytes(enc_message[i] ^ key.get_key_byte() for i in range(len(message)))

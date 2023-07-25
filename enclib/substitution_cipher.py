import random

def generate_key() -> dict[str, str]:
    ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list_ltrs = list(ltrs)
    key: dict[str, str] = {}
    
    for i in ltrs:
        key[i] = list_ltrs.pop(random.randint(0, len(list_ltrs)-1))
        
    return key


if __name__ == "__main__":
    key: dict[str, str] = generate_key()
    print(key.keys())    
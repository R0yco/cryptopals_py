from itertools import cycle
def reapeating_xor_encrypt(plaintext: bytes, key: bytes) -> bytes:
    key_cycle = cycle(key)
    return bytes([byte ^ key_cycle.__next__() for byte in plaintext])


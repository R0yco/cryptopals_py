def fixed_xor(a: bytes, b: bytes) -> bytes:
    return bytes([a[i] ^ b[i] for i in range(((len(a) if len(a) <= len(b) else len(b))))])


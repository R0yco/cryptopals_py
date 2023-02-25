from ex_1_2 import fixed_xor
def main():
    dis = hamming_distance(b"this is a test",b"wokka wokka!!!")
    print(dis)

def hamming_distance(blob1: bytes, blob2: bytes)-> int:
    # dist = 0
    # longer_blob = blob1 if len(blob1) >= len(blob2) else blob2
    # for i in range(len(longer_blob)):
    #     dist += abs(hamming_weight_byte(blob1[i]) - hamming_weight_byte(blob2[i]))
    # return dist 
    return hamming_weight(fixed_xor(blob1, blob2))
def hamming_weight(blob: bytes) -> int:
    return sum([hamming_weight_byte(byte) for byte in blob])

def hamming_weight_byte(byte) -> int:
    return bin(byte).count('1')


if __name__ == "__main__":
    main()

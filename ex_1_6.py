from collections.abc import Iterable
import itertools
from ex_1_2 import fixed_xor
from ex_1_3 import break_single_byte_xor_cipher
import math
import itertools
import base64
def main():
    with open ("ex_1_6_input.txt", 'r') as input_file:
        ciphertext = base64.b64decode(input_file.read())
    blocksize = guess_best_blocksize(ciphertext)
    print(f"[+] the guessed blocksize is {blocksize}")
    transposed_cipherblocks = get_transposed_blocks(ciphertext, blocksize)
    transposed_plainblocks = [break_single_byte_xor_cipher(transposed_cipherblocks[i]) for i in range(len(transposed_cipherblocks))]
    print(merge_plaintext(transposed_plainblocks))


def merge_plaintext(plaintext_blocks: bytes)-> bytes:
    plaintext = b""
    index = 0
    for i in range(len(plaintext_blocks[0])):
        for j in range(len(plaintext_blocks)):
            try:
                plaintext += chr(plaintext_blocks[j][i]).encode('ascii')
            except:
                return plaintext

    return plaintext

def guess_best_blocksize(ciphertext: bytes)-> int:
    max_blocksize = 40
    blocksize_scores = dict()
    for bs in range(3, max_blocksize):
        avg_pair_dist = 0.0
        trimmed_ciphertext = ciphertext[0: len(ciphertext) - len(ciphertext) % bs]
        blocks = split_to_blocks(trimmed_ciphertext, bs)
        block_pairs = list(itertools.combinations(blocks, 2))
        avg_pair_dist = (sum([hamming_distance(pair[0],pair[1]) for pair in block_pairs]) / len(block_pairs)) - 3 *bs
        blocksize_scores[bs] = avg_pair_dist

    return min(blocksize_scores, key=blocksize_scores.get)

def get_transposed_blocks(ciphertext: bytes, blocksize: int) -> list[bytes]:
    blocks = split_to_blocks(ciphertext, blocksize)
    transposed_blocks = [bytearray(b"") for _ in range(blocksize)]
    index = 0
    for block in blocks:
        for byte in block:
            transposed_blocks[index % blocksize].append(byte)
            index+=1 
    return [bytes(block) for block in transposed_blocks]

    

def split_to_blocks(blob: bytes, blocksize: int) -> Iterable:
    for i in range(0, len(blob), blocksize):
        yield blob[i: i+blocksize]

def hamming_distance(blob1: bytes, blob2: bytes)-> int:
    return hamming_weight(fixed_xor(blob1, blob2))

def hamming_weight(blob: bytes) -> int:
    return sum([hamming_weight_byte(byte) for byte in blob])

def hamming_weight_byte(byte) -> int:
    return bin(byte).count('1')

if __name__ == "__main__":
    main()

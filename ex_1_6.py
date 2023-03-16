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
    transposed_blocks = get_transposed_blocks(ciphertext, blocksize)
    print(break_single_byte_xor_cipher(transposed_blocks[0]))

def guess_best_blocksize(ciphertext: bytes)-> int:
    max_blocksize = int(math.floor(len(ciphertext) / 2))
    lowest_avg = 9999.9
    lowest_blocksize = 1
    for bs in range(3, max_blocksize):
        avg_pair_dist = 0.0
        trimmed_ciphertext = ciphertext[0: len(ciphertext) - len(ciphertext) % bs]
        blocks = split_to_blocks(trimmed_ciphertext, bs)
        block_pairs = list(itertools.combinations(blocks, 2))
        avg_pair_dist = sum([hamming_distance(pair[0],pair[1]) for pair in block_pairs]) / len(block_pairs)
        if avg_pair_dist < lowest_avg:
             lowest_avg = avg_pair_dist
             lowest_blocksize = bs
    return lowest_blocksize 

def get_transposed_blocks(ciphertext: bytes, blocksize: int) -> list[bytes]:
    blocks = split_to_blocks(ciphertext, blocksize)
    transposed_blocks = [bytearray(b"") for _ in range(blocksize)]
    # index_looper = itertools.cycle(range(blocksize)) 
    index = 0
    for block in blocks:
        for byte in block:
            transposed_blocks[index % blocksize].append(byte)
            index+=1 

    return [bytes(block) for block in transposed_blocks]

    # transposed_rounded_blocks = [bytes(i) for i in zip(*blocks)]
    # disperse reminding items
    

def split_to_blocks(blob: bytes, blocksize: int) -> Iterable:
    for i in range(0, len(blob), blocksize):
        yield blob[i: i+blocksize]

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

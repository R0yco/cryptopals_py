from Cryptodome.Cipher import AES
from base64 import b64decode

from ex_1_2 import fixed_xor

BLOCKSIZE = 16
IV = bytes(BLOCKSIZE)
KEY = b'YELLOW SUBMARINE'

def ecb_decrypt_block(ciphertext_block):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.decrypt(ciphertext_block)

def cbc_decrypt(ciphertext: bytes) -> bytes:
    prev_block = IV
    plaintext = b''
    for block_idx in range(0, len(ciphertext), BLOCKSIZE):
        cipher_block = ciphertext[block_idx:block_idx+BLOCKSIZE]

        plain_block = ecb_decrypt_block(cipher_block)
        xored_plain_block = fixed_xor(plain_block, prev_block)

        prev_block = cipher_block
        plaintext += xored_plain_block
    return plaintext

        

if __name__ == "__main__":
    decoded_ciphertext =b64decode(open("ex_2_10_input.txt","r").read())
    #print(decoded_ciphertext)
    print(cbc_decrypt(decoded_ciphertext))
    

from Cryptodome.Cipher import AES
import os
import random

def encryption_oracle(plaintext):
    mode = AES.MODE_ECB if random.randint(0,1) == 1 else AES.MODE_CBC
    cipher = AES.new(generate_random_aes_key(), mode)
    padded_plaintext = pad_plaintext(plaintext)
    return cipher.encrypt(padded_plaintext)

def pad_plaintext
def generate_random_aes_key():
    return os.urandom(16)

from Cryptodome.Cipher import AES
from base64 import b64decode
key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)

with open("ex_1_7_input.txt","rb") as ciphertext_file:
    encoded_ciphertext = ciphertext_file.read()
    ciphertext = b64decode(encoded_ciphertext)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)

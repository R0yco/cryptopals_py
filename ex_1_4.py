from ex_1_3 import find_best_key, devise_score
import codecs

best_overall_score = -999
best_score_key = -1
xor_encrypted_ciphertext = b''

for possible_ciphertext in [bytes.fromhex(line.strip()) for line in open("ex_1_4.txt")]:
    # get the possible ciphertext in byte format

    best_key = find_best_key(possible_ciphertext)
    best_plaintext = bytes([b ^ best_key for b in possible_ciphertext])
    best_plaintext_score = devise_score(best_plaintext)
    if best_plaintext_score > best_overall_score:
        best_overall_score = best_plaintext_score
        best_score_key = best_key
        xor_encrypted_ciphertext = possible_ciphertext


print(f"the ciphertext that was xor-encrypted is {codecs.encode(xor_encrypted_ciphertext,'hex').decode('ascii')}, it was encrypted with the key {best_score_key}, and the resulting plaintext is :")
print(bytes([b ^ best_score_key for b in xor_encrypted_ciphertext]))
print(f"[+] the score it received is {best_overall_score}")







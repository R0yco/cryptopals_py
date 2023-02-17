from collections import Counter
PRINTABLE_RANGE = list(range(32,128))
UPPERCASE_RANGE = range(65, 91)
LOWERCASE_RANGE = range(97, 123)
ENGLISH_LETTER_FREQUENCIES = {
        'E': 11.1607, 'M': 3.0129,
        'A': 8.4966,  'H': 3.0034,
        'R': 7.5809,  'G': 2.4705,
        'I': 7.5448,  'B': 2.0720,
        'O': 7.1635,  'F': 1.8121,
        'T': 6.9509,  'Y': 1.7779,
        'N': 6.6544,  'W': 1.2899,
        'S': 5.7351,  'K': 1.1016,
        'L': 5.4893,  'V': 1.0074, 
        'C': 4.5388,  'X': 0.2902, 
        'U': 3.6308,  'Z': 0.2722,
        'D': 3.3844,  'J': 0.1965,
        'P': 3.1671,  'Q': 0.1962
}

def break_single_byte_xor_cipher(ciphertext: bytes):
    # iterate over possible xor-keys
    best_key = find_best_key(ciphertext)
    plaintext = bytes([b ^ best_key for b in ciphertext])
    return plaintext

def find_best_key(ciphertext: bytes) -> int:
    max_score = 0
    best_key = 0
    for key in range(1,256):
        possible_plaintext = bytes([i ^ key for i in ciphertext])
        plaintext_score = devise_score(possible_plaintext)
        if plaintext_score > max_score:
            max_score = plaintext_score
            best_key = key

    return best_key

def devise_score(possible_plaintext: bytes) -> int:
    score = 0
    # if not printable_count_equals_len(possible_plaintext):
    #     score = -1
    #     return score # we don't want anything with wierd bytes in it
    #
    if english_frequency_check(possible_plaintext):
        score += 40

    if has_spaces(possible_plaintext):
        score += 30

    score += single_letter_frequency_check(possible_plaintext)

    space_ratio = calculate_space_ratio(possible_plaintext)
    if space_ratio > 0.05:
        score += 20

    lower_to_upper_ratio = calculate_lower_to_upper_ratio(possible_plaintext)
    if lower_to_upper_ratio > 2:
        score += 50
    score += calculate_unprobable_char_score(possible_plaintext)
    return score


def printable_count_equals_len(possible_plaintext: bytes) -> bool:
    printable_count = len(list(filter(lambda byte: byte in PRINTABLE_RANGE, possible_plaintext)))
    return printable_count == len(possible_plaintext) 

def calculate_unprobable_char_score(possible_plaintext: bytes) -> int:
    score = 0
    unprobable_chars = b'[]{}$@\\/^-=%|_<>`~'
    for c in possible_plaintext:
        if c in unprobable_chars:
            score -= 15
    return score

def english_frequency_check(possible_plaintext: bytes) -> bool:
    english_letter_count = len(list(filter(lambda byte: byte in LOWERCASE_RANGE or byte in UPPERCASE_RANGE, possible_plaintext)))
    english_letter_freq = english_letter_count / len(possible_plaintext)
    return english_letter_freq >= 0.77

def has_spaces(possible_plaintext: bytes) -> bool:
    return 32 in possible_plaintext

def calculate_space_ratio(possible_plaintext: bytes) -> float:
    return possible_plaintext.count(32) / len(possible_plaintext)

def single_letter_frequency_check(possible_plaintext: bytes) -> int:
    score = 0
    for byte in possible_plaintext:
        score += round(ENGLISH_LETTER_FREQUENCIES.get(chr(byte).upper(),0))
    # frequency_score = 0
    # possible_plaintext_lowercase_only = [a for a in bytes(str(possible_plaintext, 'ascii').lower(), 'ascii') if a in LOWERCASE_RANGE]
    # ideal_letter_freq_array = list({ord(k.lower()): v for k, v in sorted(ENGLISH_LETTER_FREQUENCIES.items(), key=lambda item: item[1], reverse=True)}.keys())
    # letter_freq = {letter: 100* count / len(possible_plaintext_lowercase_only) for letter, count in Counter(possible_plaintext_lowercase_only).items()}
    # letter_freq_array = list({k: v for k, v in sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)}.keys())
    # for letter in range(0,26):
    #     try:
    #         index_of_letter = letter_freq_array.index(letter+97)
    #     except ValueError:
    #         index_of_letter = -1
    #     ideal_index_of_letter = ideal_letter_freq_array.index(letter+97)
    #     if index_of_letter == -1 and ideal_index_of_letter <=5:
    #         frequency_score -= 9 # the suspected plain doesn't have a common letter in it
    #     elif abs(index_of_letter - ideal_index_of_letter) < 10:
    #         frequency_score += 5 # frequencies kinda make sense
    # 
    return score

def calculate_lower_to_upper_ratio(possible_plaintext: bytes) -> float:
    lower_count = len(list(filter(lambda b: b in LOWERCASE_RANGE, possible_plaintext)))
    upper_count = len(list(filter(lambda b: b in UPPERCASE_RANGE, possible_plaintext)))
    try:
        ratio = lower_count / upper_count
    except ZeroDivisionError:
        ratio = lower_count

    return ratio


from Cryptography.math_algorithms import gcd, find_multiplicative_inverse

letters = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}


def caesar_cipher(message, key=1, encrypt=True):
    global letters

    return_message = ""
    for letter in message:
        i = letters[letter]
        if encrypt:
            i += key
        else:
            i -= key
        i = i % 26
        return_message += list(letters.keys())[list(letters.values()).index(i)]

    return return_message


def affine_cipher(message, key=(9, 2), encrypt=True):
    global letters

    assert gcd(key[0], 26) == 1, "The alpha argument of the key must be relatively prime with 26"

    return_message = ""
    for letter in message:
        i = letters[letter]
        if encrypt:
            i = key[0]*i + key[1]
        else:
            inverse = find_multiplicative_inverse(key[0], 26)
            i = inverse*(i - key[1])
        i = i % 26
        return_message += list(letters.keys())[list(letters.values()).index(i)]

    return return_message


def vigenere_cipher(message):
    pass
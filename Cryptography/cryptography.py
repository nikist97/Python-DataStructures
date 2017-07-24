"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from Cryptography.MathAlgorithms import gcd, find_multiplicative_inverse

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
        i %= 26
        return_message += list(letters.keys())[list(letters.values()).index(i)]

    return return_message


def vigenere_cipher(message, key="codes", encrypt=True):
    global letters

    num_key = tuple([letters[k] for k in key])

    return_message = ""

    for letter_index in range(0, len(message)):
        i = letters[message[letter_index]]
        displacement = num_key[letter_index % len(num_key)]
        if encrypt:
            i += displacement
        else:
            i -= displacement
        i %= 26

        return_message += list(letters.keys())[list(letters.values()).index(i)]

    return return_message

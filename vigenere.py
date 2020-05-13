#########################################################################
# Name: Alyse Jones
# Date: Due 3/30/20
# Program: Program that mathematically implements the Vigenere cipher
# Execution in command line: python vigenere.py -e "key"
#                            python vigenere.py -d "key"
#########################################################################

from sys import stdin, stdout, argv
import string

# reference (A-Z, 0-25)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# plaintext to ciphertext
def encrypt(plaintext, key):
    # initialize ciphertext string and key position
    ciphertext = ""
    keyPos = 0
    # ignore / remove spaces in the key
    key = key.replace(" ", "")
    # convert key to all uppercase so lowercase letters can be identified
    key = key.upper()

    # iterate through the characters in plaintext
    for t in plaintext:
        # find index (or position) of plaintext character within ALPHABET
        text_index = ALPHABET.find(t.upper())
        # case for t.upper() found
        if text_index != -1:
            # find index (or position) of key character within ALPHABET
            key_index = ALPHABET.find(key[keyPos])
            # Ci + Ki
            index = text_index + key_index
            # find index of new character
            index = index % len(ALPHABET)
            # ensure letter case is maintained
            if t.isupper():
                ciphertext += ALPHABET[index]
            elif t.islower():
                ciphertext += ALPHABET[index].lower()
            keyPos += 1
            if keyPos == len(key):
                keyPos = 0
        # case for t.upper() not found (character not in ALPHABET)
        else:
            ciphertext += t
    return ciphertext

def decrypt(ciphertext, key):
    # initialize plaintext string and key position
    plaintext = ""
    keyPos = 0
    # ignore / remove spaces in the key
    key = key.replace(" ", "")
    # convert key to all uppercase so lowercase letters can be identified
    key = key.upper()

    # iterate through the characters in ciphertext
    for t in ciphertext:
        # find index (or position) of ciphertext character within ALPHABET
        text_index = ALPHABET.find(t.upper())
        # case for t.upper() found
        if text_index != -1:
            # find index (or position) of key character within ALPHABET
            key_index = ALPHABET.find(key[keyPos])
            # Ci + Ki
            index = 26 + text_index - key_index
            # find index of new character
            index = index % len(ALPHABET)
            # ensure letter case is maintained
            if t.isupper():
                plaintext += ALPHABET[index]
            elif t.islower():
                plaintext += ALPHABET[index].lower()
            keyPos += 1
            if keyPos == len(key):
                keyPos = 0
        # cose for t.upper() not found (character not in ALPHABET)
        else:
            plaintext += t
    return plaintext

# error handling for input (try the following if there is input, except if no input)
try:
    # argv[1] = -e or -d
    mode = argv[1]
    # argv[2] = key of interest
    key = argv[2]

    # standard input
    text = stdin.read().rstrip("\n")

    # encrypt mode
    if (mode == "-e"):
        ciphertext = encrypt(text, key)
        print ciphertext
    # decrypt mode
    elif (mode == "-d"):
        plaintext = decrypt(text, key)
        print plaintext
except:
    print 'INPUT ERROR!\nEncryption or Decryption mode needed. Type -e for encryption or -d for decryption.\nA key is also needed. Please type a key.\nExample: python vigenere.py -e mykey'

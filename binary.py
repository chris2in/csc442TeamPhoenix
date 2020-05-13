#########################################################################
# Name: Alyse Jones
# Date: Due 3/30/20
# Program: Program to decode binary encoded messages
# Execution in command line: python binary.py < file.txt
#########################################################################

from sys import stdin

def decode(binary, n):
    text = ""
    i = 0
    # isolate single bytes
    while (i < len(binary)):
        byte = binary[i:i+n]
        # decodes every bit string as an integer
        byte = int(byte, 2)
        # convert bytes to text
        text += chr(byte)
        # ascii 8 = backspace
        if byte == 8:
            # truncating 2 off the string text because you have to remove
            # both the backspace and the character you were trying to remove
            text = text[:-2]
        i += n
    return text

# read input from text files
binary = stdin.read().rstrip("\n")

# 7-bit
#if (len(binary) % 7 == 0):
# CHALLLENGE CHANGE: only allowed 7-bit since 8-bit didn't output right
text = decode(binary,7)
print text
# 8-bit
#if (len(binary) % 8 == 0):
#print "8-bit:"
#text2 = decode(binary,8)
#print text2


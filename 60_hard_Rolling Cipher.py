"""
Rolling Cipher
Write a function that accepts a string and an n and returns a cipher by rolling each character forward (n > 0) or backward (n < 0) n times.

Note: Think of the letters as a connected loop, so rolling a backwards once will yield z, and rolling z forward once will yield a. If you roll 26 times in either direction, you should end up back where you started.

Examples
rolling_cipher("abcd", 1) ➞ "bcde"

rolling_cipher("abcd", -1) ➞ "zabc"

rolling_cipher("abcd", 3) ➞ "defg"

rolling_cipher("abcd", 26) ➞ "abcd"
Notes
All letters are lower cased.
No spacing.
Each character is rotated the same number of times.
"""

import numpy as np
import string

def rolling_cipher(txt, n):

    return ''.join(np.roll(list(string.ascii_lowercase), -n)[:4])

    # lets = 'abcdefghijklmnopqrstuvwxyz'
    # result = []
    #
    # for char in txt:
    #     result.append(lets[(lets.index(char)+n)%26])
    # return ''.join(result)


    # if n > 0:
    #     while n > 26:
    #         if n > 26:
    #             n -= 26
    #
    # elif n < 0:
    #     while n < 26:
    #         if n < 26:
    #             n += 26
    # if n > 26:
    #     while n > 26:
    #         if n > 26:
    #             n -= 26
    #
    # alphabet = string.ascii_lowercase
    #
    # start_index = alphabet.index(txt[0])
    # end_index = alphabet.index(txt[-1])
    #
    # start_index = start_index + n
    # end_index = end_index + n
    #
    # if 0 < n < 26:
    #
    #     if end_index <= 25:
    #         result = alphabet[start_index:end_index+1]
    #         return result
    #     elif end_index >= 26:
    #         end_index -= 26
    #         result = alphabet[start_index] + alphabet[:end_index+1]
    #         return result
    # elif n % 26 == 0:
    #     return txt

print(rolling_cipher("abcd", 1))
print(rolling_cipher("abcd", -1))
print(rolling_cipher("abcd", 3))
print(rolling_cipher("abcd", 25))
print(rolling_cipher("abcd", 26))
print(rolling_cipher("abcd", 27))
print(rolling_cipher("abcd", 0))




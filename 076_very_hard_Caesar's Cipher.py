"""
Caesar's Cipher
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor). It should return an encrypted string.

Examples
caesar_cipher("middle-Outz", 2) ➞ "okffng-Qwvb"

# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# -    -
# O -> Q
# u -> w
# t -> v
# z -> b

caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5)
➞ "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

caesar_cipher("A friend in need is a friend indeed", 20)
➞ "U zlcyhx ch hyyx cm u zlcyhx chxyyx"
Notes
All test input will be a valid ASCII string.
"""

# v3
from string import ascii_lowercase as up, ascii_uppercase as low

def caesar_cipher(s, k):

    k %= 26
    return s.translate(str.maketrans(up + low, ''.join((up[k:], up[:k], low[k:], low[:k]))))


# v2
# from string import ascii_lowercase as abc
#
# def caesar_cipher(s, k):
#     k = k % 26
#     # print(k)
#     alph = abc + abc.upper()
#     # print(alph)
#     shifted = abc[k:] + abc[:k] + (abc[k:] + abc[:k]).upper()
#     # print(shifted)
#     table = s.maketrans(alph, shifted)
#     # print(table)
#     return s.translate(table)





# AlPHABET = "abcdefghijklmnopqrstuvwxyz"

# v1
# def caesar_cipher(s, k):
#
#     result = ""
#     for letter in s:
#         if letter.isalpha():
#             if letter.isupper():
#                 result += AlPHABET[(AlPHABET.index(letter.lower()) + k) % 26].upper()
#             else:
#                 result += AlPHABET[(AlPHABET.index(letter) + k) % 26]
#         else:
#             result += letter
#     return result


print(caesar_cipher("middle-Outz", 2))
print(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5))
print(caesar_cipher("A friend in need is a friend indeed", 20))
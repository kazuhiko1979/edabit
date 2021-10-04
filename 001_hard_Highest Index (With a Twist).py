"""
Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max(), nor reassign a value to the alphabet list is allowed.

Examples
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"

Notes
sorted() is not best practice.
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def alphabet_index(alphabet, string):

    big = 0
    for i in string.lower():
        if alphabet.index(i) + 1 > big:
            big = alphabet.index(i)
    return str(big+1) + alphabet[big]



#     alphabet = {key: value for value, key in enumerate(alphabet)}
#     list = ([alphabet[s] for s in string.lower() if s in alphabet.keys()])
#
#     max = list[0]
#
#     for x in list:
#         if x > max:
#             max = x
#
#     return str(max + 1) + get_key(max, alphabet)
#
#
# def get_key(val, alphabet):
#
#     for key, value in alphabet.items():
#         if val == value:
#             return key



print(alphabet_index(alphabet, "Oscar"))
print(alphabet_index(alphabet, "Lucas"))
print(alphabet_index(alphabet, "Marko"))




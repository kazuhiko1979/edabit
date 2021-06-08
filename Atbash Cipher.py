"""
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
"""


def atbash(txt):

    lookup_upper_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

    lookup_lower_table = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                  'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                  'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                  'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                  'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

    cipher = ''

    for letter in txt:
        if letter.isupper() and letter.isalpha():
            cipher += lookup_upper_table[letter]

        elif letter.islower() and letter.isalpha():
            cipher += lookup_lower_table[letter]

        elif letter == ' ':
            cipher += ' '

        else:
            cipher += letter

    return cipher


print(atbash("apple"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))





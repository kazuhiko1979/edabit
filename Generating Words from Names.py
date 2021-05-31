"""
Write a function that returns True if a given name can generate an array of words.

Examples
anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True

anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True

anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
# Not all letters are used

anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
# "s" does not exist in the original name
Notes
Each letter in the name may only be used once.
All letters in the name must be used.
"""


def anagram(name, words):

    name = sorted(name.replace(' ', '').lower())
    words = sorted(','.join(words).replace(',', '').lower())

    return name == words

print(anagram("Justin Bieber", ["injures", "ebb", "it"]))
print(anagram("Natalie Portman", ["ornamental", "pita"]))
print(anagram("Chris Pratt", ["chirps", "rat"]))
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]))
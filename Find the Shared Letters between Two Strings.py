"""
Given two strings, return a string containing only the letters shared between the two.

Examples
shared_letters("house", "home") ➞ "eho"
shared_letters("Micky", "mouse") ➞ "m"
shared_letters("house", "villa") ➞ ""
Notes
If none of the letters are shared, return an empty string.
The function should be case insensitive (e.g. comparing A and a should return a).
Sort the resulting string alphabetically before returning it.
"""


def shared_letters(a, b):

    if set(a.lower()) & set(b.lower()):
        common = set(a.lower()) & set(b.lower())
        common = ''.join(sorted(common))
    else:
        return ""

    return common

print(shared_letters("house", "home"))
print(shared_letters("Micky", "mouse"))
print(shared_letters("house", "villa"))

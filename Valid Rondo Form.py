"""
Rondo Form is a type of musical structure, in which there is a recurring theme/refrain, notated as A. Here are the rules for valid rondo forms:

Rondo forms always start and end with an A section.
In between the A sections, there should be contrasting sections notated as B, then C, then D, etc... No letter should be skipped.
There shouldn't be any repeats in the sequence (such as ABBACCA).
Create a function which validates whether a given string is a valid Rondo Form.

Examples
valid_rondo("ABACADAEAFAGAHAIAJA") ➞ True

valid_rondo("ABA") ➞ True

valid_rondo("ABBACCA") ➞ False

valid_rondo("ACAC") ➞ False

valid_rondo("A") ➞ False
Notes
Inputs will be given as all uppercase.
For the purposes of this challenge, accept ABA as valid Rondo forms.
"""


def valid_rondo(s):

    a_set_list = (set([i for i in (s[0::2])]))
    not_a_list = ([j for j in (s[1::2])])

    if s == "A":
        return False

    return s[0] == s[-1] and a_set_list == {'A'} and "A" not in not_a_list


print(valid_rondo("ABACADAEAFAGAHAIAJA"))
print(valid_rondo("ABBACCA"))
print(valid_rondo("ACAC"))
print(valid_rondo("A"))

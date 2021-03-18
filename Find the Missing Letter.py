"""
Create a function that takes a list of increasing letters and return the missing letter.

Examples
missing_letter(["a", "b", "c", "e", "f", "g"]) ➞ "d"
missing_letter(["O", "Q", "R", "S"]) ➞ "P"
missing_letter(["t", "u", "v", "w", "x", "z"]) ➞ "y"
missing_letter(["m", "o"]) ➞ "n"
Notes
Tests will always have exactly one letter missing.
The length of the test list will always be at least two.
Tests will be in one particular case (upper or lower but never both).
"""
def missing_letter(lst):

    mis_lst = [ord(ch) for ch in lst]
    no_mis_lst = [i for i in range(mis_lst[0], mis_lst[-1])]
    result = list(set(no_mis_lst) - set(mis_lst))
    for i in result:
        return chr(i)

print(missing_letter(["a", "b", "c", "e", "f", "g"]))
print(missing_letter(["O", "Q", "R", "S"]))
print(missing_letter(["t", "u", "v", "w", "x", "z"]))


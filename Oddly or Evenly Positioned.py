"""
Create a function that returns the characters from a list or string r on odd or even positions,
depending on the specifier s. The specifier will be "odd" for items on
odd positions  (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).

Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd")
➞ ["A", "B", "T", "A", "I", "Y"]

"""

# r = [2, 4, 6, 8, 10]
r = "EDABIT"
# r = ["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"]

def char_at_pos(r, s):

    # if type(r) == str:
    #     r_copy = list(r)

    if s == "odd":
        return r[0::2]

    if s == "even":
        return r[1::2]


print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "even"))
print(char_at_pos("EDABIT", "odd"))
print(char_at_pos(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"], "odd"))



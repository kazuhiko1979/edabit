"""
Create a function that takes a string as an argument and returns True if each letter in the string is surrounded by a plus sign. Return False otherwise.

Examples
plus_sign("+f+d+c+#+f+") ➞ True

plus_sign("+d+=3=+s+") ➞ True

plus_sign("f++d+g+8+") ➞ False

plus_sign("+s+7+fg+r+8+") ➞ False
Notes
For clarity, each letter must have a plus sign on both sides.
"""

def plus_sign(txt):

    txt = [i for i in txt]

    if txt[0] == "+":
        for i in txt:
            if i.isalpha():
                if txt[txt.index(i) - 1] == "+":
                    if txt[txt.index(i) + 1] == "+":
                        continue
                return False
        return True
    else:
        return False

print(plus_sign("+f+d+c+#+f+"))
print(plus_sign("+d+=3=+s+"))
print(plus_sign("+d+k+##f+"))
print(plus_sign("+s+7+fg+r+8+"))
print(plus_sign("+d+i+#+c+"))
print(plus_sign("a+"))

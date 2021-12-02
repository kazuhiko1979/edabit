"""
The Fifth Argument
Create a function (named fifth) that takes some arguments and returns the type of the fifth argument. In case the arguments were less than 5, return "Not enough arguments".

Examples
fifth(1, 2, 3, 4, 5) ➞ int

fifth("a", 2, 3, [1, 2, 3], "five") ➞ str

fifth() ➞ "Not enough arguments"
Notes
Don't get confused between zero-indexing and one-indexing.
"""

def fifth(*args):

    if len(args) < 5:
        return "Not enought arguments"

    for key, value in enumerate(list(args)):
        if key == 4:
            return type(value)

print(fifth(1, 2, 3, 4, 5))
print(fifth("a", 2, 3, [1, 2, 3], "five"))
print(fifth(1,2,3,4,'5'))


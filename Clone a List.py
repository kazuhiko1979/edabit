"""
he Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended. Can you fix the code?

Examples
clone([1, 1]) ➞ [1, 1, [1, 1]]
clone([1, 2, 3]) ➞ [1, 2, 3, [1, 2, 3]]
clone(["x", "y"]) ➞ ["x", "y", ["x", "y"]]
"""


def clone(lst):

    clone_list = [i for i in lst]
    clone_list.append(lst)

    return clone_list

print(clone([1, 1]))
print(clone([1, 2, 3]))
print(clone(["x", "y"]))
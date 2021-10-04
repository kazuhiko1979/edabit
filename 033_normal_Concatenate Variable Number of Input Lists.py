"""
Create a function that concatenates n input lists, where n is variable.

Examples
concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]

concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]
Notes
Lists should be concatenated in order of the arguments.
"""
from itertools import chain

def concat(*args):

    return sum(args, [])

    # res = list(chain.from_iterable(args))
    # return res

print(concat([1, 2, 3], [4, 5], [6, 7]))
print(concat([1], [2], [3], [4], [5], [6], [7]))
print(concat([1, 2], [3, 4]))
print(concat([4, 4, 4, 4, 4]))
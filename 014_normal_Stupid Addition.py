"""
Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.

Examples
stupid_addition(1, 2) ➞ "12"

stupid_addition("1", "2") ➞ 3

stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers.
"""


def stupid_addition(a, b):

    # Good answer
    if type(a) == type(b):
        if type(a) == int:
            return str(a) + str(b)
        return int(a) + int(b)

    # My answer

    # c = []
    #
    # c.append(a)
    # c.append(b)
    #
    # int_list = []
    # str_list = []
    #
    # for i in c:
    #     if type(i) is int:
    #         int_list.append(i)
    #     if type(i) is str:
    #         str_list.append(i)
    #
    # if len(int_list) > 1:
    #     return ''.join(([str(i) for i in int_list]))
    # if len(str_list) > 1:
    #     return sum([int(i) for i in str_list])
    # else:
    #     return None

print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))



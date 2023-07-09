"""
Fix the Right Answer
Create a function that takes a string and returns the right answer.

Examples
post_fix("2 2 +") ➞ 4

post_fix("2 2 /") ➞ 1

post_fix("8 4 / 9 * 3 1 * /") ➞ 54
Notes
The operators + - * / may be supported.
Output always returns an integer.
"""

def post_fix(expr):

    operators = '+-*/'

    numbers_list = [i for i in expr if i.isnumeric()]
    operators_list = [x for x in expr if x in operators]

    max_length = max(len(lst) for lst in [numbers_list, operators_list])
    result = []

    for i in range(max_length):
        for lst in [numbers_list, operators_list]:
            if i < len(lst):
                result.append(lst[i])
    return eval(''.join(result))


print(post_fix("8 4 / 9 * 3 1 * /"))


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


# import re
#
# def post_fix(expr):
#
#     numbers = re.findall('\d\d?', expr)
#     operators = re.findall('[\+\-\*\/]', expr)
#     result = eval(''.join([j for i in zip(numbers, operators) for j in i] + [numbers[-1]]))
#     return result


    # operators = '+-*/'
    # numbers_list = [i for i in expr.split() if i.isnumeric()]
    # operators_list = [x for x in expr.split() if x in operators]
    #
    max_length = max(len(lst) for lst in [numbers_list, operators_list])
    result = []

    for i in range(max_length):
        for lst in [numbers_list, operators_list]:
            if i < len(lst):
                result.append(lst[i])
    return eval(''.join(result))

print(post_fix("2 2 +"))
print(post_fix("2 2 /"))
print(post_fix("5 6 * 2 1 + /"))
print(post_fix("10 10 * 10 /"))
print(post_fix("8 4 / 9 * 3 1 * /"))
print(post_fix("1 1 + 2 2 + -"))


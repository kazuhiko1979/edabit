"""
Check if a String is a Mathematical Expression
Create a function that takes an input (e.g. "5 + 4") and returns True if it's a mathematical expression or False if not.

Examples
math_expr("4 + 5") ➞ True

math_expr("4*6") ➞ True

math_expr("4*no") ➞ False
Notes
Should only work with the following operations: +, -, *, /, %
You don't need to test for floats.
int1 and int2 will only be from 0-9.
"""

def math_expr(expr):

    return all([ch in '0123456789 +-*/%' for ch in expr])

    # try:
    #     return isinstance(eval(expr), (int, float))
    # except NameError:
    #     return False


    # try:
    #     eval(expr)
    #     return True
    # except:
    #     return False


    # number = expr[0] + expr[-1]
    # if number:
    #     for x in range(len(number)):
    #         expr = expr.replace(number[x], "")
    #     input = ''.join(expr.split())
    #
    #     if number[0].isdigit() and number[-1].isdigit():
    #         if ''.join(input.split()) in "+-*/%":
    #             return True
    # return False

print(math_expr("4 + 5"))
print(math_expr("4 * 5"))
print(math_expr("3*6"))
print(math_expr("4 - 5"))
print(math_expr("6 % 7"))
print(math_expr("a - b"))
print(math_expr("a - 2"))
print(math_expr("nope"))

"""
Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.

Examples
solve_for_exp(4, 1024) ➞ 5

solve_for_exp(2, 1024) ➞ 10

solve_for_exp(9, 3486784401) ➞ 10
Notes
a is raised to the power of what in order to equal b?
"""

# import math
# print(math.log(1024, 4))

def solve_for_exp(x, b):
    if b < x:
        return 0
    return 1 + solve_for_exp(x, b/x)


print(solve_for_exp(4, 1024))
print(solve_for_exp(2, 1024))
print(solve_for_exp(9, 3486784401))

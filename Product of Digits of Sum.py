"""
Create a function that takes numbers as arguments, adds them together, and returns the product of digits until the answer is only 1 digit long.

Examples
sum_dig_prod(16, 28) ➞ 6
# 16 + 28 = 44
# 4 * 4 =  16
# 1 * 6 = 6

sum_dig_prod(0) ➞ 0

sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2
Notes
The input of the function is at least one number.
"""
import numpy as np

def sum_dig_prod(*args):

    x = sum(args)
    while x > 10:
        x = np.prod([int(i) for i in str(x)])
    return x

print(sum_dig_prod(16, 28))

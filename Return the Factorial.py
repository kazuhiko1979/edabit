"""Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
Examples
factorial(3) ➞ 6
factorial(5) ➞ 120
factorial(13) ➞ 6227020800
Notes
Assume all inputs are greater than or equal to 0.
"""
import math

def factorial(num: int) -> int:

    return math.factorial(num)


if __name__ == '__main__':
    print(factorial(13))



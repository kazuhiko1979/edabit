"""
Write a function that calculates the factorial
of a number recursively.

Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
"""
def factorial(n):
    # if n == 0:
    #     return 1
    # for i in range(1, n):
    #     n = n*i
    # return n
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))
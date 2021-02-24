"""
Create a function that, given a number, returns the corresponding value of that index in the Fibonacci series.

The Fibonacci Sequence is the series of numbers:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding the two numbers before it:

The 2 is found by adding the two numbers before it (1+1).
The 3 is found by adding the two numbers before it (1+2).
The 5 is (2+3), and so on!
Examples
fibonacci(3) ➞ 3
fibonacci(7) ➞ 21
fibonacci(12) ➞ 233
"""


def fibonacci(num):

    if num <= 1:
        return 1
    else:

        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(12))
"""
n mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1:

Fibonacci Sequence

and

Fibonacci Sequence 2

for n > 1

The beginning of the sequence is thus:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
The function fastFib(num) returns the fibonacci number Fn, of the given num as an argument.

Examples
fib_fast(5) ➞ 5

fib_fast(10) ➞ 55

fib_fast(20) ➞ 6765

fib_fast(50) ➞ 12586269025
"""

def fib_fast(num):

    a = 0
    b = 1

    if num == 1:
        return a
    elif num == 2:
        return b
    else:
        for i in range(num - 1):
            a, b = b, a + b
    return b

print(fib_fast(10))





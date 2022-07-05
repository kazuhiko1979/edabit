"""
Recursion: Fibonacci Numbers
Fibonacci numbers are created in the following way:

F(0) = 0
F(1) = 1
...
F(n) = F(n-2) + F(n-1)
Write a function that calculates the nth Fibonacci number.

Examples
fib(0) ➞ 0

fib(1) ➞ 1

fib(2) ➞ 1

fib(8) ➞ 21
"""

def fib(n):

    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(8))
print(fib(12))

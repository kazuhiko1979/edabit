"""
Recursion: GCD
Write a function that calculates the GCD (Greatest Common Divisor) of two numbers recursively.

Examples
gcd(10, 20) ➞ 10

gcd(1, 3) ➞ 1

gcd(5, 7) ➞ 1

gcd(2, 6) ➞ 2
"""

def gcd(a, b):

    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

print(gcd(10, 20))
print(gcd(2, 6))
print(gcd(50, 5))

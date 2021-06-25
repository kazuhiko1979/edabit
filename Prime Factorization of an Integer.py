"""
Create a function that returns a list containing the prime factors of whatever integer is passed to it.

Examples
prime_factors(20) ➞ [2, 2, 5]

prime_factors(100) ➞ [2, 2, 5, 5]

prime_factors(8912234) ➞ [2, 47, 94811]
Notes
Implement your solution using trial division.
Your solution should not require recursion.
"""


def prime_factors(n):

    i = 2
    prime_factors = []

    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        prime_factors.append(n)

    return prime_factors


print(prime_factors(8912234))
print(prime_factors(20))








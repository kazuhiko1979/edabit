"""
Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

Examples
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

is_prime(primes, 3) ➞ "yes"

is_prime(primes, 4) ➞ "no"

is_prime(primes, 67) ➞ "yes"

is_prime(primes, 36) ➞ "no"
"""


def is_prime(prime, elem):

    low = 0
    high = len(prime) - 1

    while low <= high:

        middle = (low + high) // 2

        if prime[middle] == elem:
            return "yes"
        elif prime[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return "no"

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(is_prime(prime, 3))
print(is_prime(prime, 4))
print(is_prime(prime, 67))
print(is_prime(prime, 36))


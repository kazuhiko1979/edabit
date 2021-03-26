"""
Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit imposed by Edabit.

Sieve of Eratosthenes

Examples
prime(7) ➞ True
prime(56963) ➞ True
prime(5151512515524) ➞ False
"""

def prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


print(prime(7))
print(prime(5))
print(prime(12))
print(prime(777771))
print(prime(207971))
print(prime(100000074281))
print(prime(100000074282))
print(prime(777777777777777))
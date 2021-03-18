"""
Create a function that returns True if there's at least one prime number in the given range (n1 to n2 (inclusive)), False otherwise.

Examples
prime_in_range(10, 15) ➞ True
# Prime numbers in range: 11, 13

prime_in_range(62, 66) ➞ False
# No prime numbers in range.

prime_in_range(3, 5) ➞ True
# Prime numbers in range: 3, 5
"""


def prime_in_range(n1, n2):
    a = []
    for i in range(n1, n2 + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else: a.append(i)

    return len(a) != 0


print(prime_in_range(10, 15))
print(prime_in_range(62, 66))
print(prime_in_range(3, 5))


"""
Create a function that finds how many prime numbers there are, up to the given integer.

Examples
prime_numbers(10) ➞ 4
# 2, 3, 5 and 7

prime_numbers(20) ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19

prime_numbers(30) ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
"""


def prime_numbers(num):
    a = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            a.append(i)

    return len(a)


print(prime_numbers(10))
print(prime_numbers(20))
print(prime_numbers(30))
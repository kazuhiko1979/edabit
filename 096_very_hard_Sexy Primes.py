"""
Sexy Primes
Sexy primes are primes that differ by 6.

For example, (5, 11) comprise a sexy prime pair, while (5, 11, 17) comprise a set of sexy prime triplets.

Create a function that takes two numbers as argument, the set length n (2 for pairs, 3 for triplets), and the limit. Return a list of sorted tuples of sexy primes up to (but excluding) the limit.

Examples
sexy_primes(2, 100) ➞ [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29), (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73), (73, 79), (83, 89)]

sexy_primes(3, 100) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79)]

sexy_primes(3, 250) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79), (97, 103, 109), (101, 107, 113), (151, 157, 163), (167, 173, 179), (227, 233, 239)]
"""


def sexy_primes(n, limit):

    primes = [x for x in range(2, limit) if all(x % y for y in range(2, x // 2))]

    sexy = []
    sub_result = []

    for x in primes:
        for y in primes[1:]:
            if x + 6 == y:
                sub_result.append(x)
                sub_result.append(y)
                sexy.append(sub_result)
                sub_result = []

    if set([len(i) for i in sexy]) == {n}:
        return [tuple(s) for s in sexy]
    else:
        for s in sexy:
            for p in primes:
                if s[-1] + 6 == p:
                    s.append(p)
                    if len(s) == n:
                        break

        return [tuple(i) for i in sexy if len(i) == n]


print(sexy_primes(2, 100))
print(sexy_primes(3, 100))
print(sexy_primes(2, 300))



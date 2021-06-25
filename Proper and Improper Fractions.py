"""
Mubashir was reading about Proper and Improper Fractions on Wikipedia. He concluded that if n is the numerator and d is the denominator of a given fraction, the fraction can be called as Proper Fraction if and only if GCD(n,d)==1.

For example 5/16 is a proper fraction, while 6/16 is an improper fraction, as both 6 and 16 are divisible by 2, thus the fraction can be reduced to 3/8.

Create a function that takes a denominator number d and returns the total number of proper fractions which can be built using d as a denominator.

See below example for given denominator d = 15:

proper_fractions(15) ➞ 8

# A total of 8 different proper fractions are possible between 0 and 1
# 1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.
Examples
proper_fractions(1) ➞ 0

proper_fractions(2) ➞ 1

proper_fractions(5) ➞ 4

proper_fractions(25) ➞ 20
"""


def proper_fractions(d):
    if d == 1:
        return 0
    res = d
    i = 2
    while i * i <=d:
        if d % i == 0:
            while d % i == 0:
                d /= i
            res -= res / i
        i += 1
    if d > 1:
        res -= res / d

    return int(res)


print(proper_fractions(5))
print(proper_fractions(25))

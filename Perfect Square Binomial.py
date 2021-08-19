"""
A perfect square binomial is a trinomial that when factored gives you the square of a binomial. For example, the trinomial x²+2x+1 is a perfect square binomial because it factors to (x+1)².

Three integers (a, b, and c) are randomly (and independently) chosen between 1 and n (inclusive) where n is an integer greater than one. Create a function that takes a number n as an argument and returns the number of triplets (a, b, c) such that ax²+bx+c is a perfect square binomial.

Examples
perfect_square(6) ➞ 3

perfect_square(30) ➞ 21

perfect_square(100) ➞ 81
Notes
Trinomials like 2x²+4x+2=2(x+1)² are not considered to be perfect square binomials but trinomials like 4x²+8x+4=(2x+2)² are (in this challenge).
"""

def perfect_square(n):

    lst = []

    for i in range(1, n+1):
        if i**2 <= n:
            lst.append(i)

    cnt = 0
    for a in lst:
        for b in lst:
            if 2*a*b <= n:
                cnt += 1

    return cnt


print(perfect_square(30))
print(perfect_square(100))
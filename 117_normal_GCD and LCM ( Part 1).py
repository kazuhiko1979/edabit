"""
GCD and LCM ( Part 1)
Create a function that takes two numbers as arguments and returns the Greatest Common Divisor (GCD) of the two numbers.

Examples
gcd(3, 5) ➞ 1

gcd(14, 28) ➞ 14

gcd(4, 18) ➞ 2
Notes
The GCD is the highest number that can divide both arguments without a remainder.
"""

def gcd(a,b):

    # return a if b == 0 else gcd(b, a % b)


    # while b:
    #     a, b = b, a % b
    # return a


    # divs = []
    # for i in range(1, min(a, b) + 1):
    #     if a % i == 0 and b % i == 0:
    #         divs.append(i)
    # return max(divs)


    lst = []
    if a == b:
        return a
    else:
        for i in range(1, abs(a-b)+1):
            if a % i == 0 and b % i == 0:
                lst.append(i)
        return max(lst)


    # while a != b:
    #     if a > b:
    #         a = a - b
    #     else:
    #         b = b - a
    # return a

print(gcd(3, 5))
print(gcd(14, 28))
print(gcd(4, 18))


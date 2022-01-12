"""
Logarithms - Basic
A logarithm is kind of like reverse exponents. There is a base and a number in a logarithm. The point of a logarithm is to find out what power you have to raise the base to get the number next to the base. For example:

log base 5 of 25 = x
This is the same thing as saying 5 to the xth power is 25, which is 2 (so x would be 2). Using this example, your function must take the 5 and 25 and somehow get 2.

Examples
logarithm(5, 25) ➞ 2

logarithm(2, 64) ➞ 6

logarithm(2, 4) ➞ 2
Notes
All inputs and their associated outputs are integers.
Return "Invalid" for inputs outside of domain.
"""
import math

def logarithm(base, num):

    # try:
    #     return math.log(num, base)
    # except: return 'Invalid'

    if base < 2 or num < 2:
        return 'Invalid'

    ans = 1
    prod = base
    while prod!=num:
        prod*= base
        ans += 1
    return ans


    # count = 0
    # total = 1
    #
    # if base <= 0 or num <= 0:
    #     return 'invalid'
    #
    # while total < num:
    #     total = total * base
    #     count += 1
    #
    #     if total == num:
    #         return count

print(logarithm(5, 25))
print(logarithm(5, 9765625))
print(logarithm(0,	len("How")))
print(logarithm(-1,len("Are")))
print(logarithm(		len("you"), 0))
print(logarithm(		len("doing"), -1))
print(logarithm(		len("today?"), -15))



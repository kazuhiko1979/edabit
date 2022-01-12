"""
Find Greatest Common Divisor of N Numbers
Create a function that takes a list of numbers and returns the greatest common factor of those numbers.

Examples
gcd([84, 70, 42, 56]) ➞ 14

gcd([19, 38, 76, 133]) ➞ 19

gcd([120, 300, 95, 425, 625]) ➞ 5
Notes
The GCD is the largest factor that divides all numbers in the list.
"""

def gcd(lst):




    # get_gcd = lambda x,y: x if y==0 else get_gcd(y, x%y)
    # result = lst[0]
    #
    # for n in lst[1:]:
    #     result = get_gcd(result, n)
    # return result






# from functools import reduce
#
# def gcdhelper(x, y):
#
#     return gcdhelper(y, x % y) if y else x
#
# def gcd(lst):
#
#     return reduce(gcdhelper, lst)


# def find_gcd(x, y):
#
#     while(y):
#         x, y = y, x % y
#
#     return x
#
# def gcd(lst):
#
#     num1 = lst[0]
#     num2 = lst[1]
#
#     gcd = find_gcd(num1, num2)
#
#     for i in range(2, len(lst)):
#         gcd = find_gcd(gcd, lst[i])
#
#     return gcd

print(gcd([84, 70, 42, 56]))
print(gcd([19, 38, 76, 133]))
print(gcd([120, 300, 95, 425, 625]))


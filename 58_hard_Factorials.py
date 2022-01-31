"""
Factorials
Create a function that filters out factorials from a list. A factorial is a number that can be represented in the following manner:

n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
Recursively, this can be represented as:

n! = n * (n-1)!
Examples
filter_factorials([1, 2, 3, 4, 5, 6, 7]) ➞ [1, 2, 6]

filter_factorials([1, 4, 120]) ➞ [1, 120]

filter_factorials([8, 9, 10]) ➞ []
"""

import math

def filter_factorials(lst):

    factorials =[1]
    n = max(lst)
    temp = 1
    for i in range(1, n+1):
        temp *= i
        factorials.append(temp)
    return [i for i in lst if i in factorials]



#     return [i for i in lst if is_factorial(i)]
#
# def is_factorial(n):
#     t = 1
#     for i in range(1, n*2):
#         t *= i
#         if t == n:
#             return True
#         if t > n:
#             return False




    # math.factorial利用の場合
    # temp = [math.factorial(i) for i in range(lst[0], lst[-1])]
    # return [x for x in temp if x in lst]


print(filter_factorials([1, 2, 3, 4, 5, 6, 7]))
# print(filter_factorials([1, 4, 120]))
# print(filter_factorials([8, 9, 10]))
# print(filter_factorials([1, 8, 9, 10]))





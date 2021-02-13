"""
Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in functions max() and sorted() are prohibited.

Examples
largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
largest_even([1, 3, 5, 7]) ➞ -1
largest_even([0, 19, 18973623]) ➞ 0
"""
from typing import List


def largest_even(lst: List):

    # even_list = []
    #
    # for i in lst:
    #     if i % 2 == 0:
    #         even_list.append(i)
    #         max_numbers = int(even_list[0])
    #         if max_numbers == 0:
    #             return "0"
    #         for i in range(1, len(even_list)):
    #             if max_numbers < int(even_list[i]):
    #                 number = even_list[i]
    #             return number
    #
    # return -1

    res = -1
    for x in lst:
        if not x % 2 and x > res:
            res = x
    return res

print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1, 3, 5, 7]))
print(largest_even([0, 19, 18973623]))
print(largest_even([10, -1, 22, -1, 2]))
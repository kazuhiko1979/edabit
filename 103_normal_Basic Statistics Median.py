"""
Basic Statistics: Median
The median of a group of numbers is the middle number when the group is sorted. If the size of the group is even, the median is the average of the middle two numbers. Given a sorted list of numbers, return the median (rounded to one decimal place if the median isn't an integer).

Examples
median([1, 2, 4, 5, 6, 8, 8, 8, 10]) ➞ 6

median([2, 2, 6, 8, 8, 10, 10]) ➞ 8

median([1, 2, 2, 4, 7, 8, 9, 10]) ➞ 5.5
"""
import math
import statistics

def median(lst):

    # m = len(lst) // 2
    # return (lst[-(m+1)] + lst[m]) / 2

    # return statistics.median(lst)

    m = len(lst) // 2
    return lst[m] if len(lst) % 2 else (lst[m-1]+lst[m]) / 2


    # if len(lst) % 2 != 0:
    #     return lst[math.floor(len(lst) / 2)]
    # else:
    #     return (lst[int(len(lst)/2-1)] + lst[int(len(lst)/2):][0]) / 2

print(median([1, 2, 4, 5, 6, 8, 8, 8, 10]))
print(median([2, 2, 6, 8, 8, 10, 10]))
print(median([1, 2, 2, 4, 7, 8, 9, 10]))
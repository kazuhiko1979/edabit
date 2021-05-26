"""
Given a list of numbers, create a function that removes 25% from every number in the list except the smallest number, and adds the total amount removed to the smallest number.

Examples
show_the_love([4, 1, 4]) ➞ [3, 3, 3]

show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]

show_the_love([2, 100]) ➞ [27, 75]
Notes
There will only be one smallest number in a given list.
"""


def show_the_love(lst):


    num_75p = [i * 0.75 for i in lst]

    num_25p = [i - (i * 0.75) for i in lst]

    min_num_25p = min(num_25p)
    min_index = num_25p.index(min_num_25p)
    num_25p.pop(num_25p.index(min_num_25p))

    num_75p[min_index] = min(num_75p) + min_num_25p + sum(num_25p)

    return num_75p

print(show_the_love([16, 10, 8]))
print(show_the_love([4, 1, 4]))
print(show_the_love([2, 100]))









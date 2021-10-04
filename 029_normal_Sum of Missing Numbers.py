"""
Create a function that returns the sum of missing numbers from the given list.

Examples
sum_missing_numbers([4, 3, 8, 1, 2]) ➞ 18
# 5 + 6 + 7 = 18

sum_missing_numbers([17, 16, 15, 10, 11, 12]) ➞ 27
# 13 + 14 = 27

sum_missing_numbers([1, 2, 3, 4, 5]) ➞ 0
# No Missing Numbers (i.e. all numbers in [1, 5] are present in the list)
Notes
The numerical range to consider when searching for the missing numbers in the list is the
sequence of consecutive numbers between the minimum and maximum of the numbers (inclusive).
"""

def sum_missing_numbers(lst):

    master_lst = ([i for i in range(min(lst), max(lst)+1)])
    return sum(list(set(master_lst) - set(lst)))

print(sum_missing_numbers([4, 3, 8, 1, 2]))
print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
print(sum_missing_numbers([1, 2, 3, 4, 5]))






"""
Write a function that takes a list of two numbers and determines if the sum of the digits in each number are equal to each other.

Examples
is_equal([105, 42]) ➞ True
# 1 + 0 + 5 = 6
# 4 + 2 = 6

is_equal([21, 35]) ➞ False

is_equal([0, 0]) ➞ True
"""

def is_equal(lst):

    # return sum(map(int, str(lst[0]))) == sum(map(int, str(lst[1])))

    # return sum([int(i) for i in str(lst[0])]) == sum([int(i) for i in str(lst[1])])



print(is_equal([105, 42]))
print(is_equal([21, 35]))
print(is_equal([0, 0]))
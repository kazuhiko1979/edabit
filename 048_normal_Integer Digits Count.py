"""
Create a function that counts the integer's number of digits.

Examples
count(318) ➞ 3

count(-92563) ➞ 5

count(4666) ➞ 4

count(-314890) ➞ 6

count(654321) ➞ 6

count(638476) ➞ 6
Notes
Solve this without using strings.
Alternatively, you can solve this via a recursive approach.
"""
def count(n):
    if abs(n) < 10:
        return 1
    return count(abs(n)//10) + 1



# from math import log10
#
# def count(n):
#
#     n_count = 0
#     n = abs(n)
#
#     if n == 0:
#         return 1
#     b = int(log10(n)) + 1
#
#     num_list = [(n // (10 ** i)) % 10 for i in reversed(range(b))]
#
#     for j in num_list:
#         if j >= 0:
#             n_count += 1
#     return n_count

print(count(0))
print(count(318))
print(count(-92563))
print(count(4666))
print(count(-314890))

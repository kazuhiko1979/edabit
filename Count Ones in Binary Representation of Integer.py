"""
Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.

Examples
count_ones(0) ➞ 0
count_ones(100) ➞ 3
count_ones(999) ➞ 8
"""
def count_ones(num):

    num = bin(num)
    count = num.count('1')
    return count


print(count_ones(0))
print(count_ones(12))
print(count_ones(100))
print(count_ones(999))




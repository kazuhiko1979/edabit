"""
Write a function that returns True if every consecutive sequence of ones is followed by a consecutive sequence of zeroes of the same length.

Examples
same_length("110011100010") ➞ True

same_length("101010110") ➞ False

same_length("111100001100") ➞ True

same_length("111") ➞ False
"""

def same_length(txt):

    split_one = [a for a in txt.split("0") if a !='']
    split_zero = [a for a in txt.split("1") if a != '']
    one_count = [i.count('1') for i in split_one]
    zero_count = [i.count('0') for i in split_zero]

    return one_count == zero_count

print(same_length("110011100010"))
print(same_length("101010110"))
print(same_length("111"))
print(same_length('1001'))
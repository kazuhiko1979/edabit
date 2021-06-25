"""
Create a function which counts how many lone 1s appear in a given number. Lone means the number doesn't appear twice or more in a row.

Examples
count_lone_ones(101) ➞ 2

count_lone_ones(1191) ➞ 1

count_lone_ones(1111) ➞ 0

count_lone_ones(462) ➞ 0
Notes
Tests will include positive whole numbers only.
"""
# s = '11231212111'
# s = '1111'
# s = '462'
# s = '1191'
# s = '101'
# s = '12131415161718191'
# s = '1'
# s = '0'
# s = '11101'
import re


def count_lone_ones(n):

    return re.sub("11+", "", str(n)).count("1")
    # n = str(n)
    # length = len(str(n))
    # count = 0

    # print(length)
    # print(set(n))
    # print(n)

    # if length == 1:
    #     if n == '1':
    #         count = 1
    #
    # # if length > 1:
    #     #
    #     # if n[-1] == '1' and n[-2] == '1' and not set(n) == '1':
    #     #     count -= 1
    #     # else:
    #     #     count += 1
    #
    # for i in range(0, length):
    #     if n[i] == '1' and n[i - 1] != '1':
    #         count += 1
    #




    # if n[-1] == '1' and n[-2] != '1':
        #     count += 1


    #
    # if len(n) > 1:

    #     if n[-1] == '1' and n[-2] == '1' and set(n) == '1':
    #         count -= 1
    #     if n[0] == '1' and n[1] != '1':
    #         count += 1


    # return count

print(count_lone_ones(101))
print(count_lone_ones(1191))
print(count_lone_ones(1111))
print(count_lone_ones(11101))
print(count_lone_ones(462))
print(count_lone_ones(12131415161718191))
print(count_lone_ones(11231212111))
print(count_lone_ones(1))
print(count_lone_ones(0))
"""
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
"""


def rearranged_difference(num):

    count = [0 for x in range(10)]

    string = str(num)

    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1

    max_num = 0
    multiplier = 1

    for i in range(10):
        while count[i] > 0:
            max_num = max_num + (i * multiplier)
            count[i] = count[i] - 1
            multiplier = multiplier * 10

    return max_num - int(str(max_num)[::-1])

print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))



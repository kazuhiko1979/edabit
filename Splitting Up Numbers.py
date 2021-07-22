"""
Create a function that takes a number num and returns each place value in the number.

Examples
num_split(39) ➞ [30, 9]

num_split(-434) ➞ [-400, -30, -4]

num_split(100) ➞ [100, 0, 0]
"""


def num_split(num):

    lst = [int(i) for i in str(abs(num))]

    tmp = [value * (10 ** key) for key, value in enumerate(reversed(lst))]
    result = list(reversed(tmp))

    if num < 0:
        return [i * -1 for i in result]

    return result


print(num_split(39))
print(num_split(-434))
print(num_split(100))



"""
Create a function that returns the mean of all digits.

Examples
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6
Notes
The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be an integer.
"""

import statistics

def mean(num):

    num = [int(i) for i in str(num)]
    return statistics.mean(num)
    #
    # num = [int(i) for i in str(num)]
    # return sum(num) / len(num)


print(mean(42))
print(mean(12345))
print(mean(666))



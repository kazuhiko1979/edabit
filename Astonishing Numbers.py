"""
In this challenge, you have to establish if a given integer is an Astonishing number. An Astonishing number is an integer that, when partitioned into two parts a (left) and b (right), is equal to the sum of the consecutive numbers from a up to b (if a is lower than b), or from b up to a (if a is greater than b).

Given a positive integer num, implement a function that returns:

The string "AB-Astonishing" if num is an Astonishing number and the partition a is lower than b.
The string "BA-Astonishing" if num is an Astonishing number and the partition a is greater than b.
False if num is not an Astonishing number.
Examples
is_astonishing(15) ➞ "AB-Astonishing"
# There is only one possible partition: a = 1 and b = 5
# Sum from a up to b: 1 + 2 + 3 + 4 + 5 = 15
# It's Astonishing and partition a is lower than partition b

is_astonishing(4020) ➞ False
# There are three possible partitions
# Partition 1: a = 4 and b = 020 = 20 (leading zeros are not considered)
# Sum from a up to b: 4 + 5 + 6 + ... + 20 = 204
# Partition 2: a = 40 and b = 20
# Sum from b up to a: 20 + 21 + 22 + ... + 40 = 630
#Partition 3: a = 402 and b = 0
# Sum from b to a: 0 + 1 + 2 + ... + 402 = 81003
# It's not Astonishing

is_astonishing(2002077) ➞ "BA-Astonishing"
# There are six possible partitions
# Partition 1: a = 2 and b = 002077 = 2077 (leading zeros are not considered)
# Sum from a up to b: 2 + 3 + 4 + ... + 2077 = 2158002
# Partition 2: a = 20 and b = 02077 = 2077
# Sum from a up to b: 20 + 21 + 22 + ... + 2077 = 2157813
# Partition 3: a = 200 and b = 2077
# Sum from a up to b: 200 + 201 + 202 + ... + 2077 = 2138103
# Partition 4: a = 2002 and b = 077 = 77
# Sum from b up to a: 77 + 78 + 79 + ... + 2002 = 2002077
# It's Astonishing and partition a is greater than partition b
Notes
Leading zeros in the b partition are not considered (see examples #2 and #3).
A valid partition has at least a number into it, and this number can be also 0 (see example #2).
You can expect positive integers greater than 9 as input (a single-digit number can't be partitioned).
"""


def get_sum(a, b):

    return b * (b + 1) // 2 - a * (a - 1) // 2


def is_astonishing(num):

    n = str(num)
    for i in range(1, len(n)):
        a, b = int(n[:i]), int(n[i:])
        if a < b and num == get_sum(a, b):
            return "AB-Astonishing"
        if b < a and num == get_sum(b, a):
            return "BA-Astonishing"
    return False





    # if count < len(str(num)):
    #     # if int(str(num)[count + 1:]):
    #
    #     a = int(str(num)[0:count + 1])
    #     b = int(str(num)[count + 1:])
    #
    #     # else:
    #     #     return False
    #
    # if a < b:
    #     total = int((a + b) * (b - a + 1) / 2)
    #     print(total)
    # else:
    #     return "BA-Astonishing"
    #
    # return is_astonishing(num, count+1)


# a = int(str(num)[0:count+1])
        # b = int(str(num)[count+1:])


    #     print(a, b)
    #


print(is_astonishing(15))
print(is_astonishing(2002077))
print(is_astonishing(190))
print(is_astonishing(23136928519))





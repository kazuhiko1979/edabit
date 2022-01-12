"""
Round to Closest N
Create a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.

Examples
round_number(33, 25) ➞ 25

round_number(46, 7) ➞ 49

round_number(133, 14) ➞ 140
Notes
n will always be a positive number.
"""

def round_number(num, n):

    k = num // n
    if num % n >= n/2:
        return n*(k+1)
    else:
        return n*k


    # rem = num % n
    # if rem < n - rem:
    #     return num - rem
    #
    # return num + n - rem

    # temp_n = n
    #
    # while temp_n <= num:
    #     temp_n = temp_n + n
    # if abs(temp_n - num) < abs(num - (temp_n - n)):
    #     return temp_n
    # if abs(temp_n - num) > abs(num - (temp_n - n)):
    #     return temp_n - n
    # elif abs(temp_n - num) == abs(num - (temp_n - n)):
    #     return temp_n




    # smallNumbyDiv = math.floor(num / n) * n
    # largerNumbyDiv = math.ceil(num / n) * n
    #
    # if abs(num - smallNumbyDiv) < abs(num - largerNumbyDiv):
    #     return smallNumbyDiv
    # if abs(num - smallNumbyDiv) > abs(num - largerNumbyDiv):
    #     return largerNumbyDiv
    # elif abs(num - smallNumbyDiv) == abs(num - largerNumbyDiv):
    #     return largerNumbyDiv


print(round_number(34, 25))
print(round_number(54, 8))
print(round_number(65, 10))
print(round_number(6247, 163))
print(round_number(532, 12))
print(round_number(642234, 1523))

"""
Starting with either 3 or 5 and given these operations:

add 5
multiply by 3
You should say if it is possible to reach the target number n.

Examples
only_5_and_3(14) ➞ True
# 14 = 3*3 + 5

only_5_and_3(25) ➞ True
# 25 = 5+5+5+5+5

only_5_and_3(7) ➞ False
# There exists no path to the target number 7
Notes
You can solve this problem by recursion or algebra.
"""


def only_5_and_3(n):

    if n == 3 or n == 5:
        return True
    if n < 3:
        return False

    return only_5_and_3(n - 5) or only_5_and_3(n / 3)



    # if n % 5 == 0:
    #     return True
    # if 3 > n:
    #     return False
    #
    # num_index = len(str(n))
    #
    # if num_index < 5:
    #     max_range = 10
    # else:
    #     max_range = 50
    #
    # lst_3 = [3 ** i for i in range(1, max_range)]
    # lst_5 = [5 * i for i in range(1, max_range)]
    #
    # for k in lst_5:
    #     if k == n:
    #         return True
    #     if n <= k:
    #         tmp_5 = n - k
    #         if tmp_5 % 3 == 0:
    #             return True
    #         else:
    #             return False
    #
    # for j in lst_3:
    #     if j == n:
    #         return True
    #     if n <= j:
    #         tmp_5 = n - j
    #         if tmp_5 % 5 == 0:
    #             return True
    #         else:
    #             return False




# print(only_5_and_3(14))
# print(only_5_and_3(25))
# print(only_5_and_3(7))
# print(only_5_and_3(2))
print(only_5_and_3(43))

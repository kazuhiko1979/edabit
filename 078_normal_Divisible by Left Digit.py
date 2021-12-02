"""
Divisible by Left Digit?
Create a function that takes a number n and checks if each digit is divisible by the digit on its left. Return a boolean array depending on the condition checks.

Examples
divisible_by_left(73312) ➞ [False, False, True, False, True]
# no element left to 7 = False
# 3/7 = False
# 3/3 = True
# 1/3 = False
# 2/1 = True

divisible_by_left(1) ➞ [False]

divisible_by_left(635) ➞ [False, False, False]
Notes
The array should always start with False as there is no digit to the left of the first digit.
"""

def divisible_by_left(num):

    nums = list(map(int, str(num)))
    return [False] + [False if not i else (j / i).is_integer() for i, j in zip(nums, nums[1:])]


    # res = []
    # i = 1
    # numList = list(map(int, str(num)))
    #
    # res.append(False)
    #
    # while i < len(numList):
    #
    #     try:
    #         ans = numList[i] / numList[i-1]
    #     except ZeroDivisionError:
    #         res.append(False)
    #     else:
    #         if ans.is_integer():
    #             res.append(True)
    #         else:
    #             res.append(False)
    #     i += 1
    # return res

print(divisible_by_left(73312))
print(divisible_by_left(2026))


"""
Mod 10 Algorithm
Create a function that takes a number and checks whethers the given number is a valid credit card number using Luhn Algorithm.
The return value is boolean.

Examples
valid_credit_card(4111111111111111) ➞ True
# Visa Card

valid_credit_card(6451623895684318) ➞ False
# Not a valid credit card number.

valid_credit_card(6451623895684318) ➞ False
Notes
American Express/VISA/Discover/Diner Club may be the credit card type.
"""
import numpy as np

def valid_credit_card(number):

    # v2
    # a = [int(i) for i in str(number)[::-1]]
    # for digit in range(1,len(a)):
    #     if digit % 2 != 0:
    #         a[digit] = a[digit] * 2
    #         if a[digit] > 9:
    #             a[digit] -= 9
    # if 9*(sum(a[:-1])) % 10 == a[-1]:
    #     return True
    # return False

    # v3
    total = 0
    digits = [int(i) for i in str(number)[::-1]]
    # print(digits)
    check = digits.pop(0)

    for idx, i in enumerate(digits):
        if idx % 2:
            total += i
        else:
            total += i*2 if i < 5 else i*2 - 9

    return (9*total) % 10 == check



    # number = list(str(number))
    # # print(number[:-1])
    # temp_number = len(number[:-1])
    #
    # one_two = []
    # for i in range(0, temp_number):
    #     if i % 2 == 0:
    #       one_two.append(1)
    #     else:
    #       one_two.append(2)
    # # print(one_two)
    #
    # total = []
    #
    # for a, b in zip(number[:-1], one_two):
    #     if len(str(int(a) * b)) == 2:
    #         total.append(int(str(int(a) * b)[0]) + int(str(int(a) * b)[1]))
    #     else:
    #         total.append(int(a) * b)
    # print(sum(total))
    #
    # x = np.mod(sum(total), 10)
    x = 10 - x
    # print(x)
    # return number[-1] == str(x)


print(valid_credit_card(2111111111121111))
print(valid_credit_card(4111111111111111))
print(valid_credit_card(5500000000000004))
print(valid_credit_card(378282246310005))
print(valid_credit_card(7777777777777777))
print(valid_credit_card(6011000000000004))
print(valid_credit_card(6451623895684318))



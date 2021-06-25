"""
Given an integer, return a new integer according to the rules below:

Split the number into groups of two digit numbers. If the number has an odd number of digits, return "invalid".
For each group of two digit numbers, concatenate the last digit to a new string the same number of times as the value of the first digit.
Return the result as an integer.
look_and_say(3132) ➞ 111222

# By reading the number digit by digit, you get three "1" and three "2".
# Therefore, you put three ones and three two's together.
# Remember to return an integer.
Examples
look_and_say(95) ➞ 555555555

look_and_say(1213141516171819) ➞ 23456789

look_and_say(120520) ➞ 200

look_and_say(231) ➞ "invalid"
Notes
Note that the number 0 can be included (see example #3).
"""
#
# n = str(95)
# n = str(3132)
# n = str(313317)
# n = str(1213141516171819)

def look_and_say(n):

    n = str(n)

    if len(n) % 2 != 0:
        return 'invalid'

    # My ansaer:
    # n_list = [i for i in range(int(len(n)))]
    #
    # tmp_i = [i for i in n_list[1::2]]
    # tmp_j = [j for j in n_list[0::2]]
    #
    # result = int(''.join([n[i] * int(n[j]) for i, j in zip(tmp_i, tmp_j)]))
    # return result
    #
    # Best answer
    return int(''.join(int(n[i]) * n[i + 1] for i in range(0, len(n), 2)))


print(look_and_say(1213141516171819))
print(look_and_say(95))
print(look_and_say(120520))
print(look_and_say(231))
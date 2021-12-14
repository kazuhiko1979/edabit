"""
Smallest Square Ending
In a letter to Lord Bowden in 1837, Charles Babbage asked, "What is the smallest positive integer whose square ends in 269,696?". He thought the answer was 99,736 whose square is 9,947,269,696. Was he right?

Write a function that takes a positive integer n and returns the smallest number whose square ends with n. One small twist, if n == 269696 return "Babbage was correct!" if the smallest number whose square ends with 269,696 is 99,736, otherwise return "Babbage was incorrect!".

Examples
babbage(25) ➞ 5

babbage(161) ➞ 119
# 119 * 119 == 14,161
# Ends with 161

babbage(269696) ➞ "Babbage was {?}!"
# Replace {?} with the word "correct" or "incorrect".
Notes
n will always be a positive integer n > 0.
Make sure your solution is efficient enough to pass the tests within a 12 second time limit.
"""


def babbage(n):



    # for i in range(1, n+1):
    #     if n == 269696:
    #
    #         return "Babbage was {}!".format("correct" if str(i**2).endswith(str(n)) else "incorrect")
    #     else:
    #         if str(i**2).endswith(str(n)):
    #             return i



    # if n == 269696:
    #     return "Babbage was incorrect!"
    #
    # square = []
    # for i in range(n, 0, -1):
    #     square.append(i * i)
    # square = sorted(square)
    #
    # index_list = []
    #
    # for i in square:
    #     if str(n) in str(i):
    #         index_list.append(i)
    # min_square = min(index_list)
    # return square.index(min_square) + 1


print(babbage(25))
print(babbage(481))
print(babbage(161))
print(babbage(990025))
print(babbage(327369))

print(babbage(33765625))
print(babbage(314062500))

print(babbage(269696))

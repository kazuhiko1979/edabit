"""
In BlackJack, cards are counted with -1, 0, 1 values:

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the list of cards provided.

Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1
count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6
count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
Notes
String inputs will always be upper case.
You do not need to consider case sensitivity.
If the argument is empty, return 0.
No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
"""
def count(deck):

    # plus_one_list = [2, 3, 4, 5, 6]
    # zero_list = [7, 8, 9]
    # minus_zero_list = [10, "J", "Q", "K", "A"]

    plus_one_str = '23456'
    zero_str = '789'
    minus_zero_str = '10JQKA'

    # result_plus = []
    # result_minus = []
    # for i in deck:
    #     if i in plus_one_list:
    #         result_plus.append(i)
    # for i in deck:
    #     if i in zero_list:
    #         break
    # for x in deck:
    #     if x in minus_zero_list:
    #         result_minus.append(x)
    # return int(len(result_plus) - int(len(result_minus)))

    return sum([1 if str(i) in plus_one_str else -1 if str(i) in minus_zero_str else 0 for i in deck])




print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
print(count(["A", "A", "K", "Q", "Q", "J"]))
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))


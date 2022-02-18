"""
Poker Flush?
Create a function that takes in two lists and determines whether there exists a flush.

The first list represents the 5 cards dealt on the table.
The second list represents the 2 cards in your hand.
Notation: card number and suit (abbreviated as S = Spades, H = Hearts, D = Diamonds, C = Clubs) separated by an underscore.

Examples
check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) ➞ True // diamond flush

check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) ➞ True // spade flush

check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) ➞ False
Notes
Hint: If there aren't at least 3 cards of the same suit on the table, there is zero chance of there being a flush.
"""


def check_flush(table, hand):

    # total = [i[-1] for i in table] + [i[-1] for i in hand]
    # return any(total.count(i) >= 5 for i in total)


    # temp = {}
    # table = table + hand
    #
    # for x in [i[-1] for i in table]:
    #     if x in temp:
    #         temp[x] += 1
    #     else:
    #         temp[x] = 1
    #
    # return max(temp.values()) >= 5



print(check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]))
# print(check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]))
# print(check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]))
# print(check_flush(['8_H', '10_H', '10_D', 'J_H', '10_S'], ['5_D', 'Q_H']))











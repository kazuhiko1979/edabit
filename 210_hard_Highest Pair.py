"""
Highest Pair
You will be given a collection of five cards (representing a player's hand in poker). If your hand contains at least one pair, return a list of two elements: True and the card number of the highest pair (trivial if there only exists a single pair). Else, return False.

Examples
highest_pair(["A", "A", "Q", "Q", "6" ]) ➞ [True, "A"]

highest_pair(["J", "6", "3", "10", "8"]) ➞ False

highest_pair(["K", "7", "3", "9", "3"]) ➞ [True, 3]

highest_pair(["K", "9", "10", "J", "Q"]) ➞ False

highest_pair(["3", "5", "5", "5", "5"]) ➞ [True, 5]
Notes
Hands with three or more of the same card still count as containing a pair (see the last example).
"""
# v3
def highest_pair(cards):

	pairs = [c for c in set(cards) if cards.count(c) >= 2]
	return [True, max(pairs, key='23456789JQKA'.index)] if pairs else False

# v2
# def highest_pair(cards):
#
# 	order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# 	cards = sorted(cards, key=lambda x: order.index(x))
# 	cards = [x for x in cards if cards.count(x) >= 2]
# 	return [True, cards[-1]] if cards else False

# v1
# points = {
# 	"A": 14,
# 	"K": 13,
# 	"Q": 12,
# 	"J": 11,
# 	"10": 10,
# 	"9": 9,
# 	"8": 8,
# 	"7": 7,
# 	"6": 6,
# 	"5": 5,
# 	"4": 4,
# 	"3": 3,
# 	"2": 2,
# 	}
#
# def highest_pair(lst):
#
# 	res = [(a, b) for idx, a in enumerate(lst) for b in lst[idx + 1:]]
# 	pairs = list(set([i for i, j in res if i == j]))
#
# 	if not pairs:
# 		return False
# 	if len(pairs) < 2:
# 		return [True, pairs[0]]
# 	else:
# 		if points[pairs[0]] > points[pairs[1]]:
# 			return [True, pairs[0]]
# 		else:
# 			return [True, pairs[1]]


print(highest_pair(["A", "A", "Q", "Q", "6"]))
print(highest_pair(['A', 'K', 'Q', 'J', '10']))
print(highest_pair(['A', 'K', 'K', 'K', 'Q']))
print(highest_pair(['A', '3', '3', '4', '4']))
print(highest_pair(['A', 'K', 'Q', 'Q', '5']))



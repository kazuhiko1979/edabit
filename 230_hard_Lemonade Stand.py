"""
Lemonade Stand
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Return True if and only if you can provide every customer with correct change.

Examples
lemonade([5, 5, 5, 10, 20]) ➞ True

lemonade([5, 5, 10, 10, 20]) ➞ False

lemonade([10, 10]) ➞ False

lemonade([5, 5, 10]) ➞ True
Notes
You don't have any change in hand at first.
bills is an integer list.
bills[i] will be either 5, 10, or 20.
"""

# v2
def lemonade(lst):

	change = 0

	for i in lst:
		change -= i - 5
		if change < 0:
			return False
		change += 5
	return True


# v 1
# def lemonade(lst):
#
# 	exchange = {"5": 0, "10": 0, "20": 0}
#
# 	for i in lst:
# 		if i == 5:
# 			exchange[str(i)] += 1
# 		if i == 10:
# 			exchange[str(i)] += 1
# 			exchange["5"] -= 1
# 		if i == 20:
# 			exchange[str(i)] += 1
# 			exchange["5"] -= 1
# 			exchange["10"] -= 1
#
# 	return min(exchange.values()) >= 0

print(lemonade([5, 5, 5, 10, 20]))
print(lemonade([5, 5, 10, 10, 20]))
print(lemonade([10, 10]))
print(lemonade([5, 5, 10]))
print(lemonade([5, 5, 5, 5, 10, 5, 10, 10, 10, 20]))
print(lemonade([5, 10, 5, 5, 5, 20, 5, 10, 5, 5, 10, 20]))
print(lemonade([5, 10, 5, 5, 5, 20, 5, 10, 20, 5, 10, 20, 10]))

"""
Sherlock and Squares
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value describing a range of integers. Sherlock must determine the number of square integers within that range, inclusive of the endpoints (note that a square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25, 36, 49).

For example, the range is a=24 and b=49, inclusive. There are three square integers in the range: 25, 36 and 49.

Complete the squares function that returns an integer representing the number of square integers in the inclusive range from a to b.

Examples
squares(3, 9) ➞ 2

squares(17, 24) ➞ 0

squares(1, 1000000000) ➞ 31622
"""
import math

def squares(a, b):

	return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a))) + 1

	# cnt = 0
	#
	# for i in range(a, b+1):
	# 	j = 1
	# 	while j * j <= i:
	# 		if j * j == i:
	# 			cnt += 1
	# 		j = j + 1
	# 	i = i + 1
	# return cnt

print(squares(3, 9))
print(squares(17, 24))
print(squares(433, 100000))
# print(squares(1, 1000000000))
# print(squares(89784519, 103811134))








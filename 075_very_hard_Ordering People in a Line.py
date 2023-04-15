"""
Ordering People in a Line
Create a function that takes in the size of the line and the number of people waiting and places people in an S-shape ordering. The demonstration below will make it clear:

# Ordering numbers 1-15 in a [5,3] space.

order_people([5, 3], 15) ➞ [
  [1, 2, 3],
  [6, 5, 4],
  [7, 8, 9],
  [12, 11, 10],
  [13, 14, 15]
]
If there is extra room, leave those spots blank with a 0 filler.

# Ordering numbers 1-5 in a [4, 3] space.

order_people([4, 3], 5) ➞ [
  [1, 2, 3],
  [0, 5, 4],
  [0, 0, 0],
  [0, 0, 0]
]
If there are too many people for the given dimensions, return "overcrowded".

order_people([4, 3], 20) ➞ "overcrowded"
Examples
order_people([3, 3], 8) ➞ [
  [1, 2, 3],
  [6, 5, 4],
  [7, 8, 0]
]

order_people([2, 4], 5) ➞ [
  [1, 2, 3, 4],
  [0, 0, 0, 5]
]

order_people([2, 4], 10) ➞ "overcrowded"
Notes
Always start the ordering on the upper-left corner.
If the S-shape concept doesn't make sense, try writing down some of these examples on a piece of paper and tracing a pencil through the numbers in order.
"""
# v2


# v1
# def order_people(size, num_people):
#
# 	grid = [[0 for j in range(size[1])] for i in range(size[0])]
#
# 	try:
# 		for k in range(num_people):
# 			row, col = divmod(k, size[1])
# 			if row % 2 == 0:
# 				grid[row][col] = k + 1
# 			else:
# 				grid[row][size[1] - col - 1] = k + 1
# 	except IndexError:
# 		return "overcrowded"
#
# 	return grid


print(order_people([5, 3], 15))
print(order_people([3, 3], 8))

print(order_people([2, 4], 10))
# def order_people(lst, people):
#
# 	output_list = []
#
# 	for i in range(0, len(lst), people):
# 		output_list.append(lst[i: i + people])
# 	return output_list
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range_size = 3
# sublists = order_people(my_list, range_size)
# print(sublists)

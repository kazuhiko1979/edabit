"""
Pascal's Triangle
The goal of this challenge is to return Pascal's triangle up to number 29. Pascal's triangle is the sum of the two upper corners.

   1 1
  1 2 1
 1 3 3 1

# There will always be the 1 in the first
# place and the row in the second.
Pascal's Triangle

Create a function that returns a row from Pascal's triangle. To find the row and column you can use n!/(k!*(n-k)!) where n is the row down and k is the column.

Examples
pascals_triangle(1) ➞ "1 1"

pascals_triangle(4) ➞ "1 4 6 4 1"

pascals_triangle(6) ➞ "1 6 15 20 15 6 1"

pascals_triangle(8) ➞ "1 8 28 56 70 56 28 8 1"
"""
def pascals_triangle(row):

	if row == 1:
		return ' '.join(map(str, [1, 1]))

	triangle = [[1]]

	for i in range(1, row):
		prev_row = triangle[-1]
		cur_row = [1]

		for j in range(1, i):
			cur_row.append(prev_row[j-1] + prev_row[j])

		cur_row.append(1)
		triangle.append(cur_row)

	return ' '.join(map(str, triangle[-1]))

# import copy
#
# def pascals_triangle(row):
#
# 	count = 0
#
# 	def set_list(top_cur_list, bottom_cur_list, count):
#
# 		cur_list = []
# 		top_cur_list.insert(0, 0)
# 		bottom_cur_list.append(0)
#
# 		for i, k in zip(top_cur_list, bottom_cur_list):
# 			cur_list.append(i + k)
#
# 		count += 1
#
# 		if count < row:
# 			temp_cur_list = copy.deepcopy(cur_list)
# 			return set_list(cur_list, temp_cur_list, count)
# 		else:
# 			return ' '.join(map(str, cur_list[1:-1]))
#
# 	while row >= count:
# 		# Initial settings
# 		top_pre_list = [0, 1, 0]
# 		bottom_pre_list = [0, 1, 0]
#
# 		return set_list(top_pre_list, bottom_pre_list, count)
#
print(pascals_triangle(1))
print(pascals_triangle(2))
print(pascals_triangle(3))
print(pascals_triangle(4))
print(pascals_triangle(5))
print(pascals_triangle(29))




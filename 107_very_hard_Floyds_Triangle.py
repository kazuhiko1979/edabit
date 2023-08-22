"""
Floyd's Triangle
Floyd's triangle is a right-angled triangular array of natural numbers. It's defined by filling the rows of the triangle with consecutive numbers, starting with a 1 in the top left corner:

Floyd's triangle

Write a function that takes an integer n and returns Floyd's triangle's rows as a list of lists. Your function should return one of two possibilities:

If a value is passed to n_row, return the first n rows.
If a value is passed to up_to, return all rows up to, and including, the row that contains n.
Expect an argument to be passed to one parameter or the other, but not both.

Examples
floyd(up_to = 5) ➞ [[1], [2, 3], [4, 5, 6]]
# The third row contains a 5.

floyd(n_row = 5) ➞[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
# Returns the first five rows.

floyd(up_to = 10) ➞ [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

floyd(n_row = 1) ➞[[1]]
Notes
Hint: You can define n_row from up_to using the triangular number sequence. That is, n_row should be x in the equation (x*(x+1))/2 = up_to rounded up. Then, you only need to write a function for n_row.
"""

def floyd(up_to = None, n_row = None):

	input_list = []

	count = up_to if up_to else n_row

	while count > 0:
		x = int(count * (count + 1) / 2)
		input_list.append([i for i in range(x, x - count, -1)])
		count -= 1

	output_list = sorted(input_list, key=lambda x: sum(x))
	output_list = [sorted(sublist) for sublist in output_list]

	if up_to:
		index_containing_target = next((i for i, sublist in enumerate(output_list) if up_to in sublist), None)
		return output_list[:index_containing_target+1]
	else:
		return output_list


print(floyd(up_to = 1))
print(floyd(up_to = 2))
print(floyd(up_to = 7))
print(floyd(up_to = 9))
print(floyd(up_to = 15))
print(floyd(up_to = 50))
print(floyd(n_row = 1))
print(floyd(n_row = 2))
print(floyd(n_row = 5))
print(floyd(n_row = 6))
print(floyd(n_row = 11))


"""
Colour Harmony
In colour theory, colour harmony refers to an aesthetically pleasing combination of colours. The standard colour wheel shows the 12 primary, secondary and tertiary colours. Starting with red, and moving clockwise, the colours are:

colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
With an initial colour (called the anchor), you can find combinations of harmonious colours. The combination types are shown below, for an anchor colour of green:

Image of Colour Combinations

Given an anchor colour and a combination type, write a function that returns a set containing all colours within the combination.

Examples
colour_harmony("green", "triadic") ➞ { "green", "violet", "orange" }

colour_harmony("blue-green", "complementary") ➞ { "blue-green", "red-orange" }

colour_harmony("orange", "analogous") ➞ { "yellow-orange", "red-orange", "orange" }
Notes
Create the combinations given their relative positions from the anchor colour. For example, the rectangle combination starts with the colours two positions clockwise and four positions anti-clockwise from the anchor (and not the other way around). With the split-complemetary combination, you take the colours five positions both clockwise and anti-clockwise from the anchor. For the analogous combination, you include the colours directly on either side of the anchor.
Include the anchor colour in the final set.
"""


def colour_harmony(anchor, combination_type):
	colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green", "green", "blue-green", "blue",
			   "blue-violet", "violet", "red-violet"]

	anchor_index = colours.index(anchor)
	result = set()

	if combination_type == "complementary":
		complement_index = (anchor_index + 6) % 12
		result.add(anchor)
		result.add(colours[complement_index])
	elif combination_type == "analogous":
		prev_index = (anchor_index - 1) % 12
		next_index = (anchor_index + 1) % 12
		result.add(colours[prev_index])
		result.add(anchor)
		result.add(colours[next_index])
	elif combination_type == "triadic":
		triad_indices = [(anchor_index + 4) % 12, (anchor_index + 8) % 12]
		result.add(anchor)
		for index in triad_indices:
			result.add(colours[index])
	elif combination_type == "square":
		square_indices = [(anchor_index + 3) % 12, (anchor_index + 6) % 12, (anchor_index + 9) % 12]
		for index in square_indices:
			result.add(colours[index])
	elif combination_type == "rectangle":
		rect_indices = [(anchor_index + 3) % 12, (anchor_index + 6) % 12, (anchor_index + 9) % 12,
						(anchor_index + 2) % 12]
		for index in rect_indices:
			result.add(colours[index])
	elif combination_type == "split_complementary":
		split_comp_indices = [(anchor_index + 5) % 12, (anchor_index + 7) % 12]
		result.add(anchor)
		for index in split_comp_indices:
			result.add(colours[index])

	return result

# テスト
print(colour_harmony('blue-green', 'triadic'))  # {'red-violet', 'blue-green', 'yellow-orange'}
print(colour_harmony('blue', 'complementary'))  # {'orange', 'blue'}
print(colour_harmony('violet', 'square'))  # {'violet', 'red-orange', 'yellow', 'blue-green'}
print(colour_harmony('yellow-green', 'analogous'))  # {'yellow-green', 'yellow', 'green'}
print(colour_harmony('red', 'rectangle'))  # {'green', 'blue', 'orange', 'red'}
print(colour_harmony('violet', 'split_complementary'))  # {'violet', 'yellow-orange', 'yellow-green'}
print(colour_harmony('orange', 'analogous'))  # {'yellow-orange', 'red-orange', 'orange'}
print(colour_harmony('red-orange', 'complementary'))  # {'blue-green', 'red-orange'}
print(colour_harmony('red-orange', 'square'))  # {'blue-green', 'yellow', 'red-orange', 'violet'}
print(colour_harmony('blue-violet', 'split_complementary'))  # {'orange', 'blue-violet', 'yellow'}
print(colour_harmony('red-violet', 'triadic'))  # {'red-violet', 'yellow-orange', 'blue-green'}
print(colour_harmony('red-violet', 'rectangle'))  # {'red-violet', 'yellow-green', 'red-orange', 'blue-green'}

# colors = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
#
# def find_four_points(anchor, index, opposite_index, points):
#
# 	anchor_right_two_index = (index + points[0]) % 12
# 	anchor_opposite_right_index = (anchor_right_two_index + points[1]) % 12
#
# 	anchor_opposite_color = colors[opposite_index]
# 	anchor_right_color = colors[anchor_right_two_index]
# 	anchor_opposite_right_color = colors[anchor_opposite_right_index]
#
# 	return {anchor_opposite_right_color, anchor, anchor_opposite_color, anchor_right_color}
#
# def find_three_points(anchor, index, points):
# 	right_four_index = (index + points[0]) % 12
# 	left_four_index = (index - points[0]) % 12
#
# 	right_four_color = colors[right_four_index]
# 	left_four_color = colors[left_four_index]
#
# 	return {anchor, right_four_color, left_four_color}
#
# def colour_harmony(anchor, combination):
#
# 	index = colors.index(anchor)
# 	num_for_complementary = 6
# 	opposite_index = (index + num_for_complementary) % 12
#
# 	num_for_rectangle = [2,6]
# 	num_for_sqaure = [3,6]
# 	num_for_triadic = [4]
# 	num_for_split_complementary = [5]
# 	num_for_analogous = [1]
#
# 	if combination == "complementary":
# 		opposite_number = colors[opposite_index]
# 		return {anchor, opposite_number}
#
# 	if combination == "rectangle":
# 		return find_four_points(anchor, index, opposite_index, num_for_rectangle)
#
# 	if combination == "square":
# 		return find_four_points(anchor, index, opposite_index, num_for_sqaure)
#
# 	if combination == "triadic":
# 		return find_three_points(anchor, index, num_for_triadic)
#
# 	if combination == "split_complementary":
# 		return find_three_points(anchor, index, num_for_split_complementary)
#
# 	if combination == "analogous":
# 		return find_three_points(anchor, index, num_for_analogous)

# print(colour_harmony('blue-green', 'triadic'))
# # , {'blue-green', 'red-violet', 'yellow-orange'})
# print(colour_harmony('blue', 'complementary'))
# #, {'blue', 'orange'})
# print(colour_harmony('violet', 'square'))
# #, {'blue-green', 'red-orange', 'violet', 'yellow'})
# print(colour_harmony('yellow-green', 'analogous'))
# #, {'yellow-green', 'yellow', 'green'})
# print(colour_harmony('red', 'rectangle'))
# #, {'green', 'blue', 'orange', 'red'})
# print(colour_harmony('violet', 'split_complementary'))
# #, {'yellow-orange', 'yellow-green', 'violet'})
# print(colour_harmony('orange', 'analogous'))
# #, {'yellow-orange', 'red-orange', 'orange'})
# print(colour_harmony('red-orange', 'complementary'))
# #, {'blue-green', 'red-orange'})
# print(colour_harmony('red-orange', 'square'))
# #, {'blue-green', 'red-orange', 'violet', 'yellow'})
# print(colour_harmony('blue-violet', 'split_complementary'))
# #, {'blue-violet', 'orange', 'yellow'})
# print(colour_harmony('red-violet', 'triadic'))
# #, {'blue-green', 'red-violet', 'yellow-orange'})
# print(colour_harmony('red-violet', 'rectangle'))
# #, {'blue-green', 'red-violet', 'yellow-green', 'red-orange'})
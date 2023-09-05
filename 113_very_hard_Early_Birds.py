"""
Early Birds
A Natural Number String Sequence is a string containing all numbers, starting from 0, joined without spaces or other delimitators between them.

"01234567891011121314151617181920..."
If you think of the sequence as a list, any number has a natural position index it occupies within a string long enough to contain it based on the real position in the numeric sequence. Looking at the example above, numbers from 0 to 9 are equals to their index position in the string; starting from 10, every number has a string natural index position different from itself (number 10 has a position of 10|11 because it has two digits, number 11 has a position of 12|13, and so on).

When a number appears in the sequence before its natural position is an Early Bird. Suppose that we want to know if number 12 is an Early Bird in the above example sequence:

01234567891011121314151617181920
_!!___________!!________________
Natural position index of 12 is |14, 15| (after 11 and before 13 in the numeric sequence), but, if we look closely at the sequence, it appears before its natural position, at index |1, 2| (after 0 and before 3): 12 is then an Early Bird number (and the first to appear, also).

You are given two integers as parameters: _range is the ending number of the string sequence to generate, and n is the number to analyze. You must implement a function that returns a list that contains the position indexes of n (with every position index being a list in turn), and the string "Early Bird!" as the last element of the list only if n is an Early Bird. If n it's not an Early Bird and the returned list has to contain just the list with its natural position index.

Examples
is_early_bird(20, 14) ➞ [[18, 19]]

is_early_bird(20, 12) ➞ [[1, 2], [14, 15], "Early Bird!"]

is_early_bird(101, 101) ➞ [[10, 11, 12], [193, 194, 195], "Early Bird!"]
Notes
The given number n will be greater than 9 for every case, as trivially every single-digit number appears at the same index in the numeric sequence and in the string sequence.
The position indexes have to be in the order they appear in the string sequence.
The string at the end of the list has to be present only if n is an Early Bird.
Check the Resources tab for more info on this sequence.
"""
def is_early_bird(r, n):
	r, l = ''.join(str(i) for i in range(r+2)), len(str(n))
	f = [list(range(i, i+l)) for i, j in enumerate(r[:-l]) if r[i:i+l] == str(n)]
	return f + ["Early Bird!"] if len(f) > 1 else f

# def is_early_bird(_range, n):
# 	num_string_sequence = ''.join(map(str, range(_range + 1)))
# 	num_str = str(n)
# 	positions = []
#
# 	for i in range(len(num_str), len(num_string_sequence)):
# 		num = num_string_sequence[i - len(num_str):i]
# 		if num == num_str:
# 			positions.append(list(range(i - len(num_str), i)))
#
# 	if len(positions) > 1:
# 		positions.append("Early Bird!")
#
# 	return positions


# テストケース
print(is_early_bird(20, 14))
print(is_early_bird(20, 12))
print(is_early_bird(101, 101))
print(is_early_bird(50, 34))
print(is_early_bird(212, 156))
print(is_early_bird(400, 240))
print(is_early_bird(900, 888))
print(is_early_bird(1200, 745))
print(is_early_bird(2000, 666))

# import re
#
# def is_early_bird(_range, n):
#
# 	num_string_sequence= ''.join([str(i) for i in range(0, _range + 1)])
# 	matches = re.finditer(str(n), num_string_sequence)
#
# 	match_positions = []
#
# 	for match in matches:
# 		match_positions.append([match.start(), match.end()])
#
# 	result = []
# 	temp = []
# 	count = 0
# 	length = len(str(n))
#
# 	for index in match_positions:
# 		for i, v in enumerate(range(index[0], index[1])):
# 			temp.append(v)
# 			count += 1
# 			if length == count:
# 				result.append(temp)
# 				temp = []
# 				count = 0
#
# 	if len(result) > 1:
# 		result.append("Early Bird!")
#
# 	return result


# print(is_early_bird(20, 14))
# print(is_early_bird(20, 12))
# print(is_early_bird(101, 101))
# print(is_early_bird(50, 34))
# print(is_early_bird(212, 156))
# print(is_early_bird(400, 240))
# print(is_early_bird(900, 888))
# print(is_early_bird(1200, 745))
# print(is_early_bird(2000, 666))




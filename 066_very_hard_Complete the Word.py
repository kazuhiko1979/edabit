"""
Complete the Word
An input string can be completed if additional letters can be added and no letters need to be taken away to match the word. Furthermore, the order of the letters in the input string must be the same as the order of letters in the final word.

Create a function that, given an input string, determines if the word can be completed.

Examples
can_complete("butl", "beautiful") ➞ True
# We can add "ea" between "b" and "u", and "ifu" between "t" and "l".

can_complete("butlz", "beautiful") ➞ False
# "z" does not exist in the word beautiful.

can_complete("tulb", "beautiful") ➞ False
# Although "t", "u", "l" and "b" all exist in "beautiful", they are incorrectly ordered.

can_complete("bbutl", "beautiful") ➞ False
# Too many "b"s, beautiful has only 1.
Notes
Both string input and word will be lowercased.
"""
# v3
def can_complete(initial, word):

	stack = list(initial)[::-1]
	for letter in word:
		if letter == stack[-1]:
			stack.pop()
	return not stack

# v2
# import re
#
# def can_complete(initial, word):
# 	pattern = r'.*?'.join(initial)
# 	return bool(re.match(pattern, word))

# v1
# import copy
#
# def can_complete(initial, word):
#
# 	copy_word = copy.copy(word)
# 	pre_w_index = 0
#
# 	for i, c in enumerate(initial):
# 		if initial[i] in copy_word:
# 			i_index = i
#
# 			w_index = copy_word.index(initial[i])
#
# 			if i_index == w_index or i_index < w_index and w_index >= pre_w_index:
# 				copy_word = list(copy_word)
# 				copy_word[w_index] = ''
# 				copy_word = "".join(copy_word)
# 				pre_w_index = w_index
# 			else:
# 				return False
# 		else:
# 			return False
#
# 	return "".join(sorted(initial + copy_word)) == "".join(sorted(word))


print(can_complete("butl", "beautiful"))
print(can_complete("butlz", "beautiful"))
print(can_complete('tulb', 'beautiful'))
print(can_complete('bbutl', 'beautiful'))
print(can_complete('sg', 'something'))
print(can_complete('sgi', 'something'))
print(can_complete('sing', 'something'))
print(can_complete('siing', 'something'))

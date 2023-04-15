"""
Fit the Pattern
Create a function that checks if the sub-lists in a list adhere to the specified pattern.

Examples
check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True

check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True

check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True

check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True

check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True
Notes
The length of the pattern will always be the same as the length of the (main) list.
The pattern does not necessarily have to be alphabetically ordered (see last example).
"""
# v2
def check_pattern(lst, pattern):

	return [lst.index(x) for x in lst] == [pattern.index(i) for i in pattern]


#v2

# ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# def check_pattern(lst, pattern):
#
#     used_letters = []
#     pattern_idx = 0
#
#     for letter in lst:
#         if letter not in used_letters:
#             used_letters.append(letter)
#
#         letter_idx = ALPHABETS.index(letter)
#
#         if letter_idx != pattern_idx:
#             return False
#
#         pattern_idx += 1
#
#         if pattern_idx >= len(pattern):
#             break
#
#     return pattern_idx == len(pattern)


# v1
# ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTU'
#
# def check_pattern(lst, pattern):
#
# 	temp = []
# 	alpha = ""
#
# 	idx = 0
# 	list_idx = 0
#
# 	for i in lst:
# 		if not temp:
# 			temp.append(i)
# 			alpha += ALPHABETS[idx]
# 			list_idx += 1
# 		else:
# 			for j in lst[list_idx:]:
# 				if j in temp:
# 					for k in temp:
# 						if j == k:
# 							alpha += ALPHABETS[temp.index(k)]
# 							list_idx += 1
# 				else:
# 					alpha += ALPHABETS[idx+1]
# 					temp.append(j)
# 					idx += 1
# 					list_idx += 1
#
# 	if alpha == pattern[::-1] or alpha == pattern:
# 		return True
# 	return False

print(check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB"))
print(check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA"))

print(check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD"))
print(check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA"))

print(check_pattern([[1, 1], [2, 2], [1, 1], [1, 2]], "ABAB"))


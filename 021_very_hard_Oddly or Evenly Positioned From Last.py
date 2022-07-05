"""
Oddly or Evenly Positioned From Last
Create a function that extracts the characters from a list (or a string) on odd or even positions, depending on the specifier. The string "odd" for items on odd positions (... 5, 3, 1) and "even" for even positions (... 6, 4, 2) from the last item of that list or string.

Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 4th & 2nd positions from right.

char_at_pos("EDABIT", "odd") ➞ "DBT"
# "D", "B" and "T" occupy the 5th, 3rd and 1st positions from right.

char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd") ➞ ["(", "&", "%", "#", "!"]
Notes
Lists are zero-indexed, so, index+1 = position or position-1 = index.
Optional: Solve this challenge in a single-line lambda function.
A recursive version of this challenge can be found via this link.
"""


def char_at_pos(r, s, res=None):

	if res is None:
		res = []
	# Recursive
	if r:
		if s == "even" and len(r) > 1:
			res.append(r[-2])
		elif s == "odd":
			res.append(r[-1])
		r = r[:-2]

	return char_at_pos(r, s, res) if r else res[::-1]




	# v2
	# if s == "even":
	# 	return r[::-1][1::2][::-1]
	# else:
	# 	return r[::-1][0::2][::-1]


	# v1
	# if s == "odd":
	# 	result = list(reversed([str(value) for key, value in enumerate(r[::-1], 1) if key % 2 != 0]))
	# else:
	# 	result = list(reversed([str(value) for key, value in enumerate(r[::-1], 1) if key % 2 == 0]))
	#
	# if type(r) == list:
	# 	if type(r[0]) == int:
	# 		return [int(i) for i in result]
	# 	return result
	# return ''.join(result)


print(char_at_pos("EDABIT", "even"), "EAI")
# print(char_at_pos("EDABIT", "odd"), "DBT")
# # print(char_at_pos("QWERTYUIOP", "even"), "QETUO")
# print(char_at_pos("POIUYTREWQ", "odd"), "OUTEQ")
# print(char_at_pos("ASDFGHJKLZ", "odd"), "SFHKZ")
# # print(char_at_pos("ASDFGHJKLZ", "even"), "ADGJL")
# # print(char_at_pos([2, 4, 6, 8, 10], "even"), [4, 8])
# print(char_at_pos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "odd"), [2, 4, 6, 8, 10])
# print(char_at_pos(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"], "odd"), ["@", "$", "^", "*", ")"])
# print(char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd"), ["(", "&", "%", "#", "!"])
# # print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"), ["A", "B", "T", "A", "I", "Y"])
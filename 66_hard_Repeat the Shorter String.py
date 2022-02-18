"""
Repeat the Shorter String
Write a function that repeats the shorter string until it is equal to the length of the longer string.

Examples
lengthen("abcdefg", "ab") ➞ "abababa"

lengthen("ingenius", "forest") ➞ "forestfo"

lengthen("clap", "skipping") ➞ "clapclap"
Notes
Both strings will differ in length.
Both strings will contain at least one character.
Either of the two strings could be the shortest in length.
"""

def lengthen(s1, s2):

	a = max(len(s1), len(s2))
	return ((s1 if len(s1) < len(s2) else s2)*a)[:a]


	# a = max(len(s1), len(s2))
	#
	# if len(s1) < len(s2):
	# 	return (s1 * a)[:a]
	# else:
	# 	return (s2 * a)[:a]

	# if len(s1) < len(s2):
	# 	short_string = s1
	# 	len_short_string = len(s1)
	# 	len_long_string = len(s2)
	#
	# else:
	# 	short_string = s2
	# 	len_short_string = len(s2)
	# 	len_long_string = len(s1)
	#
	# multi_num = 0
	#
	# while len_long_string > len_short_string:
	# 	multi_num += 1
	# 	len_short_string = len_short_string * multi_num
	#
	# max_lenghOf_short_string = (short_string * len_short_string)
	# return max_lenghOf_short_string[:len_long_string]

print(lengthen("abcdefg", "ab"))
print(lengthen("ingenius", "forest"))
print(lengthen("clap", "skipping"))
print(lengthen("k", "champagne"))
print(lengthen("DUH", "champagne"))


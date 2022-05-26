"""
A Capital Challenge
Given two strings, s1 and s2, select only the characters in each string where the character in the same position in the other string is in uppercase. Return these as a single string.

To illustrate, given the strings s1 = "heLLo" and s2 = "GUlp", we select the letters "he" from s1, because "G" and "U" are uppercase. We then select "lp" from s2, because "LL" is in uppercase. Finally, we join these together and return "help".

Examples
select_letters("heLLO", "GUlp") ➞ "help"

select_letters("1234567", "XxXxX")  ➞ "135"

select_letters("EVERYTHING", "SomeThings") ➞  "EYSomeThings"
Notes
The strings don't have to be the same length.
Strings can contain non-alphabetic characters.
"""

def select_letters(s1, s2):

	# v3
	left = ''.join(l1 for l1, l2 in zip(s1, s2) if l2.isupper())
	right = ''.join(l2 for l1, l2 in zip(s1, s2) if l1.isupper())

	return left + right

	# v2
	# res = ""
	# for l1, l2 in zip(s1, s2):
	# 	if l2.isupper():
	# 		res += l1
	# for l1, l2 in zip(s1, s2):
	# 	if l1.isupper():
	# 		res += l2
	# return res


	# v1
	# s1_index = [s2_key for s2_key, s2_value in enumerate(s2) if s2_value.isalpha() and s2_value.isupper()]
	# s2_index = [s1_key for s1_key, s1_value in enumerate(s1) if s1_value.isalpha() and s1_value.isupper()]
	#
	# s1_result = [s1[key] for key, value in zip(s1_index, s1) if key < len(s1)]
	# s2_result = [s2[key] for key, value in zip(s2_index, s2) if key < len(s2)]
	#
	# return ''.join(s1_result + s2_result)


print(select_letters("heLLO", "GUlp"))
print(select_letters("1234567", "XxXxX"))
print(select_letters("EVERYTHING", "SomeThings"))
print(select_letters("PaTtErN", "pAtTeRn"))
print(select_letters("nothing", "nothing"))
print(select_letters("What do you think of it so far?", "RUBBISH!"))



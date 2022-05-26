"""
Ice Cream Sandwich
An ice cream sandwich is a string that is formed by two identical ends and a different middle.

Some examples of ice cream sandwiches:
"AABBBAA"

"3&&3"

"yyyyymmmmmmmmyyyyy"

"hhhhhhhhmhhhhhhhh"
Notice how left and right ends of the sandwich are identical in both length and in repeating character). The middle section is distinctly different.

Not ice cream sandwiches:
"BBBBB"
// You can't have just plain icecream.

"AAACCCAA"
// You can't have unequal sandwich ends.

"AACDCAA"
// You can't have more than one filling.

"A"
// You can't have fewer than 3 characters.
Write a function that returns True if a string is an ice cream sandwich and False otherwise.

Examples
is_icecream_sandwich("CDC") ➞ True

is_icecream_sandwich("AAABB") ➞ False

is_icecream_sandwich("AA") ➞ False
Notes
An ice cream sandwich must have a minimum length of 3 characters, and at least two of these characters must be distinct (you can't only have the filling!).
"""

def is_icecream_sandwich(txt):

	# v3
	# return txt == txt[::-1] and len(set(txt)) == 2

	# v2
	from itertools import groupby
	return txt == txt[::-1] and len(list(groupby(txt))) == 3


	# v1
	# temp = []
	# unique_txt = []
	# if len(txt) >= 3 and len(set(list(txt))) != 1:
	# 	for i in range(1, len(list(txt))+1):
	# 		if list(txt)[i-1] == list(txt)[i*-1]:
	# 			temp.append(True)
	# 			unique_txt.append(list(txt)[i-1])
	# 		else:
	# 			return False
	# 	return all(temp) and len(set(unique_txt)) == 2
	# return False

# print(is_icecream_sandwich("CDC"))
# print(is_icecream_sandwich("AAABB"))
# print(is_icecream_sandwich("AA"))
print(is_icecream_sandwich(""))
print(is_icecream_sandwich("AABBBAA"))
print(is_icecream_sandwich("3&&3"))
print(is_icecream_sandwich("yyyyymmmmmmmmyyyyy"))
print(is_icecream_sandwich("hhhhhhhhmhhhhhhhh"))
print(is_icecream_sandwich("BBBBB"))
print(is_icecream_sandwich("AAACCCAA"))
print(is_icecream_sandwich("AACDCAA"))
print(is_icecream_sandwich("AAABB"))
print(is_icecream_sandwich("AA"))
print(is_icecream_sandwich("A"))

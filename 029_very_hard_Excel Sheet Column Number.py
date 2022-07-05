"""
Excel Sheet Column Number
Given a column title as it appears in an Excel sheet return its corresponding column number.

The number is computed in the following way:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
Examples
title_to_number("A") ➞ 1

title_to_number("R") ➞ 18

title_to_number("AB") ➞ 28
Notes
1 <= len(s) <= 7
s consists only of uppercase English letters.
"""

def title_to_number(s):

	# v3
	# al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# result = 0
	#
	# for l in s:
	# 	result = result * 26 + al.index(l) + 1
	# return result

	# v2
	alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	result = 0
	for i in range(len(s)):
		result += alphabet.find(s[-i-1])*26**i
	return result

	# v1
	# alpha = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# result = 0
	#
	# for i, k in reversed(list(enumerate(reversed(list(s)), 1))):
	# 	if i == 1:
	# 		result += i**i * alpha.index(k)
	# 	elif i == 2:
	# 		result += 26 * alpha.index(k)
	# 	elif i > 2:
	# 		result += 26 ** (i-1) * alpha.index(k)
	# return result

print(title_to_number("A"))
print(title_to_number("B"))
print(title_to_number("Z"))
print(title_to_number("AB"))
print(title_to_number("ZY"))
print(title_to_number("KFC"))
print(title_to_number("FRIENDS"))

"""
Digital Vowel Ban
In this challenge, it's time to ban some impenitent digit!

Your job is to delete the digits of a given number that, within their name written in English, contain a given vowel.

Given an integer n, and a string ban being the vowel to search, implement a function that returns:

If the given vowel is not present in the name of any of the digits of n, the same n.
If n has at least a digit that contains the given vowel in its name, the new integer obtained after the elimination of banned digits (as a natural number without leading zeros).
If all digits of n are banned, a string "Banned Number".
Examples
digital_vowel_ban(143, "o") ➞ 3
# 1 = "One" contains "o" (banned).
# 4 = "Four" contains "o" (banned).
# 3 = "Three" is safe.

digital_vowel_ban(14266330, "e") ➞ 4266
# "One" contains "e" (banned).
# "Four", "Two" and "Six" are safe.
# "Three" and "Zero" contain "e" (banned).

digital_vowel_ban(4020, "u") ➞ 20
# "Four" contains "u" (banned).
# Leading zeros are not considered.

digital_vowel_ban(586, "i") ➞ "Banned Number"
# All digits ("Five, "Eight", "Six") contain "i".
Notes
Every given number will be a positive integer greater than 0.
"""

num_alpha = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	0: "zero"
}

import copy

def digital_vowel_ban(n, ban):

	# v3
	d = {"e": "0135789", 'i': '5689', "o": "0124", "u": "4"}
	new = ''.join(i for i in str(n) if i not in d.get(ban, ""))
	return "Banned Number" if not new else int(new)


	# v2
	# num = ''.join(i for i in str(n) if ban not in num_alpha[int(i)])
	# if num:
	# 	return int(num)
	# return "Banned Number"


	# v1
	# original_n = str(copy.deepcopy(n))
	#
	# for key, val in enumerate(str(n)):
	# 	if ban in num_alpha[int(val)]:
	# 		original_n = original_n.replace(val, '')
	# return "Banned Number" if original_n == '' else int(original_n)

print(digital_vowel_ban(143, "o"))
print(digital_vowel_ban(14266330, "e"))
print(digital_vowel_ban(4020, "u"))
print(digital_vowel_ban(586, "i"))
print(digital_vowel_ban(123456789, "i"))
print(digital_vowel_ban(20442, "o"))
print(digital_vowel_ban(1100, "u"))

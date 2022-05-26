"""
Tweaking Letters
Create a function that tweaks letters by one forward (+1) or backwards (-1) according to a list.

Examples
tweak_letters("apple", [0, 1, -1, 0, -1]) ➞ "aqold"
# "p" + 1 => "q"; "p" - 1 => "o"; "e" - 1 => "d"

tweak_letters("many", [0, 0, 0, -1]) ➞ "manx"

tweak_letters("rhino", [1, 1, 1, 1, 1]) ➞ "sijop"
Notes
Don't worry about capital letters.
"""

def tweak_letters(txt, lst):

	# v4
	alphabet = "abcdefghijklmnopqrstuvwxyz"


	# step1 find index of alphabet
	# return [alphabet.find(txt[i]) for i in range(len(lst))]

	# step2 find string from index
	# return [alphabet[(alphabet.find(txt[i]))] for i in range(len(lst))]

	# step3 transfer string by lst
	# return ''.join([alphabet[(alphabet.find(txt[i]) + lst[i])] for i in range(len(lst))])

	# step4 convert for A and Z
	return ''.join([alphabet[(alphabet.find(txt[i]) + lst[i]) % 26] for i in range(len(lst))])

# v3
	# alphabet = "abcdefghijklmnopqrstuvwxyz"
	# result = ""
	# for i in range(len(txt)):
	# 	result = result + alphabet[alphabet.index(txt[i]) + lst[i]]
	# return result

	# v2
	# alphabet = "abcdefghijklmnopqrstuvwxyz"
	# result = ""
	# for key, value in zip(lst, txt):
	# 	if value in list(alphabet):
	# 		alphabet_index = alphabet.index(value)
	# 		if key == 0:
	# 			result += alphabet[alphabet_index]
	# 		elif key == 1:
	# 			if alphabet_index == len(alphabet)-1:
	# 				result += alphabet[0]
	# 			else:
	# 				result += alphabet[alphabet_index + 1]
	# 		elif key == -1:
	# 			result += alphabet[alphabet_index - 1]
	# return result


	# v1
	# result = ""
	#
	# for key, value in zip(lst, txt):
	# 	ord_value = ord(value)
	# 	# print(ord_value)
	# 	if key == 0:
	# 		result += chr(ord_value)
	# 	elif key == 1:
	# 		if ord_value != 122:
	# 			result += chr(ord_value + 1)
	# 		if ord_value == 122:
	# 			result += chr(97)
	# 	elif key == -1:
	# 		if ord_value != 97:
	# 			result += chr(ord_value - 1)
	# 		if ord_value == 97:
	# 			result += chr(122)
	# return result

print(tweak_letters("apple", [0, 1, -1, 0, -1]))
print(tweak_letters("many", [0, 0, 0, -1]))
print(tweak_letters("rhino", [1, 1, 1, 1, 1]))
print(tweak_letters('xyz', [1, 1, 1]))
print(tweak_letters('abc', [-1, -1, -1]))


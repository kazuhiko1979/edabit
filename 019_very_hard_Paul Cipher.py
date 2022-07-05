"""
Paul Cipher
In Paul Cipher, only alpha characters will be encoded with the following rules:

All alpha characters will be treated as uppercase letters.
The first alpha character will not change (except for switching to upper case).
All subsequent alpha characters will be shifted toward "Z" by the alphabetical position of the previous alpha character (wrap back to "A" if "Z" is passed).
he1lo would be encoded as follows:

paul_cipher("he1lo") ➞ "HM1QA"

h -> H (First character to be changed to uppercase)
e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)
Given a string txt, return the encoded message. See the below examples for a better understanding:

Examples
paul_cipher("muBas41r") ➞ "MHWCT41K"

paul_cipher("a1rForce") ➞ "A1SXUGUH"

paul_cipher("MATT") ➞ "MNUN"
"""

import string

def paul_cipher(txt) -> string:


	# v2
	# res, shift = [], 0
	# for c in txt.upper():
	# 	if c.isalpha():
	# 		c_pos = ord(c) - 65
	# 		new_c = chr((c_pos + shift) % 26 + 65)
	# 		shift = c_pos + 1
	# 	else:
	# 		new_c = c
	# 	res.append(new_c)
	#
	# return res


	# v1 お勧め
	a = 'abcdefghijklmnopqrstuvwxyz'.upper()
	a_to_pos = {}
	pos_to_a = {}

	for n in range(26):
		a_to_pos[a[n]] = n+1
		pos_to_a[n + 1] = a[n]

	# print(a_to_pos)
	# print(pos_to_a)

	txt = txt.upper()

	movement = None
	encode = ''

	for i in txt:
		if movement == None or i not in a:
			encode += i
		else:
			try:
				encode += pos_to_a[a_to_pos[i] + movement]
			except KeyError:
				encode += pos_to_a[a_to_pos[i] + movement - 26]

		try:
			movement = a_to_pos[i]
		except KeyError:
			continue



	return encode


	# result = []
	# num_alpha = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
	#  14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
	#  26: 'z'}
	#
	# alpha_num = dict(zip(string.ascii_lowercase, range(1,27)))
	# print(num_alpha[13])
	#
	# result.append(list(txt)[0].upper())
	#
	# index = 1
	# previous_index = 0
	#
	# temp = []
	# for i in txt:
	# 	if i.isupper():
	# 		i = i.lower()
	# 		temp.append(i)
	# 	else:
	# 		temp.append(i)
	# print(temp)
	#
	#
	#
	# while index < len(temp):
	# 	try:
	# 		if list(temp)[index].isalpha() and not list(temp)[previous_index].isdigit():
	# 			total_index = alpha_num[list(temp)[previous_index]] + alpha_num[list(temp)[index]]
	# 			if total_index >= 27:
	# 				total_index = total_index - 26
	# 				result.append(num_alpha[total_index].upper())
	# 				previous_index += 1
	# 				index += 1
	# 			elif total_index < 27:
	# 				result.append(num_alpha[total_index].upper())
	# 				previous_index += 1
	# 				index += 1
	# 				continue
	#
	# 		if list(temp)[index].isdigit():
	# 			result.append(list(temp)[index])
	# 			# previous_index += 1
	# 			index += 1
	# 		# if list(temp)[previous_index].isdigit():
	# 		# 	result.append(list(temp)[index].upper())
	# 		# 	# previous_index += 1
	# 		# 	index += 1
	# 		else:
	# 			previous_index += 1
	# 			continue
	#
	# 		# if list(temp)[index].isalpha():
	# 		# 	total_index = alpha_num[list(temp)[previous_index]] + alpha_num[list(temp)[index]]
	# 		# 	if total_index >= 27:
	# 		# 		total_index = total_index - 26
	# 		# 		result.append(num_alpha[total_index].upper())
	# 		# 		previous_index += 1
	# 		# 		index += 1
	# 		# 	else:
	# 		# 		result.append(num_alpha[total_index].upper())
	# 		# 		previous_index += 1
	# 		# 		index += 1
	#
	# 	except:
	# 		previous_index += 1
	# 		index += 1
	#
	# return result


# paul_cipher("he1lo") ➞ "HM1QA"
print(paul_cipher("he1lo"))

print(paul_cipher("muBas41r"))
# paul_cipher("muBas41r") ➞ "MHWCT41K"

print(paul_cipher("a1rForce"))
# paul_cipher("a1rForce") ➞ "A1SXUGUH"

# print(paul_cipher("MATT"))

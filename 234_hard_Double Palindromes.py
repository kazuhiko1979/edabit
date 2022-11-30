"""
Double Palindromes
Strings can be segregated into both their letter and digit components.

A double palindrome is when a string's letter component and digit component are both palindromes.
A single-palindrome is when either (but not both) the letter component or the digit component are palindromes.
To illustrate:

"cab97ac79"
# double-palindrome: "cabac" and "9779" are both palindromes.

"1abc4de1"
# single-palindrome: "141" is a palindrome.
Write a function that maps double palindromes to the number 2, single palindromes to the number 1, and everything else to the number 0.

Examples
palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]) ➞ [2, 2, 1, 0]

palindrome_set(["789", "555", "ccc", "abba"]) ➞ [0, 1, 1, 1]

palindrome_set(["7a", "5f", "6c"]) ➞ [2, 2, 2]
Notes
A string is composed of only letters or only numbers, can be at most a single palindrome (see example #2).
All single character components are trivially palindromes (see example #3).
All letters will be lower cased.
"""
# v2
def palindrome_set(lst):

	alphas = [[cha for cha in word if cha.isalpha()] for word in lst]
	digits = [[cha for cha in word if cha.isnumeric()] for word in lst]

	lst = [[1 if digit and digit == digit[::-1] else 0, 1 if alpha and alpha == alpha[::-1] else 0] for alpha, digit in zip(alphas, digits)]
	return [sum(x) for x in lst]


	# result = []
	# point = 0
	# for alpha, digit in zip(alphas, digits):
	# 	if digit and digit == digit[::-1]:
	# 		point += 1
	# 	if alpha and alpha == alpha[::-1]:
	# 		point += 1
	#
	# 	result.append(point)
	# 	point = 0
	# return result






# v1
# def palindrome_set(lst):
#
# 	if lst == [""]:
# 		return [0]
#
# 	alpha, digit = "", ""
# 	temp, separated, result = [], [], []
# 	point = 0
#
# 	for word in lst:
# 		for cha in word:
# 			if cha.isdigit():
# 				digit += cha
# 			else:
# 				alpha += cha
# 		if digit:
# 			temp.append(''.join(digit))
# 		if alpha:
# 			temp.append(''.join(alpha))
#
# 		separated.append(temp)
# 		digit, alpha, temp = [], [], []
#
# 	for word in separated:
# 		if word[0] == word[0][::-1]:
# 			point += 1
# 		try:
# 			if word[1] == word[1][::-1]:
# 				point += 1
# 		except:
# 			ValueError
# 		result.append(point)
# 		point = 0
# 	return result



# import re
#
# def palindrome_set(lst):
#
# 	point = 0
# 	result = []
#
# 	for i in lst:
# 		separeted = re.findall(r"[^\W\d_]+|\d+", i)
#
# 		if len(separeted) > 2:
# 			alpha = ""
# 			digit = ""
# 			for word in separeted:
# 				if word.isdigit():
# 					digit += word
# 				else:
# 					alpha += word
# 			separeted = []
# 			separeted.append(alpha)
# 			separeted.append(digit)
#
# 		if len(separeted) == 2:
# 			if separeted[0] == separeted[0][::-1]:
# 				point += 1
# 			if separeted[1] == separeted[1][::-1]:
# 				point += 1
#
# 		if len(separeted) == 1:
# 			if separeted[0] == separeted[0][::-1]:
# 				point += 1
#
# 		result.append(point)
# 		point = 0
#
# 	return result


print(palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]))
print(palindrome_set(["18a99b89cc881ba", "p7o8p987", "p7o", "p7o8"]))
print(palindrome_set(["ab9a", "abba", "aa78bb8bbaa7", "a88a"]))
print(palindrome_set(["789", "555", "ccc", "abba"]))
print(palindrome_set(["7a", "5f", "6c"]))

print(palindrome_set(["7ab", "5fc", "6cd"]))
print(palindrome_set(["87ab", "15fc", "26cd"]))
print(palindrome_set(["1234ab", "144a441"]))
print(palindrome_set([""]))

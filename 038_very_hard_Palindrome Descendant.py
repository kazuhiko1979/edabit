"""
Palindrome Descendant
A number may not be a palindrome, but its descendant can be. A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.

For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.

Create a function that returns True if the number itself is a palindrome or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).

Examples
palindrome_descendant(11211230) ➞ True
# 11211230 ➞ 2333 ➞ 56 ➞ 11

palindrome_descendant(13001120) ➞ True
# 13001120 ➞ 4022 ➞ 44

palindrome_descendant(23336014) ➞ True
# 23336014 ➞ 5665

palindrome_descendant(11) ➞ True
# Number itself is a palindrome
Notes
Numbers will always have an even number of digits.
"""
# v3
def palindrome_descendant(num):

	num = str(num)
	while len(num) > 1:
		if num == num[::-1]:
			return True
		s = ""
		for idx in range(0, len(num), 2):
			try:
				s += str(int(num[idx]) + int(num[idx+1]))
			except IndexError:
				pass
		num = s
	return False



# v2
# def sum_pairs(s):
# 	new = ''
# 	for i in range(0, len(s), 2):
# 		new + str(sum(int(j) for j in s[i:i+2]))
# 	return new
#
# def palindrome_descendant(num):
# 	s = str(num)
# 	if len(s) < 3:
# 		return s == s[::-1]
#
# 	while len(s) > 2:
# 		s = sum_pairs(s)
# 		if s == s[::-1]:
# 			return True
# 	return False




# v1 not work
import numpy as np

# def palindrome_descendant(num, temp=[], total=[]):
#
# 	while len(str(num)) > 0:
# 		temp.append(int(str(num)[0]))
# 		temp.append(int(str(num)[1]))
# 		total.append(str(sum(temp)))
# 		temp = []
# 		return palindrome_descendant(str(num)[2:], temp, total)
#
# 	return palindrome_help(total)
#
# def palindrome_help(total):
#
# 	if len("".join(total)) != 2:
# 		num = int("".join(total))
# 		total = []
# 		temp = []
# 		return palindrome_descendant(num, temp, total)
#
# 	elif len("".join(total)) == 2:
# 		return True
# 	else:
# 		return False


print(palindrome_descendant(11211230))
print(palindrome_descendant(13001120))
print(palindrome_descendant(23336014))

print(palindrome_descendant(11))
print(palindrome_descendant(1122))

print(palindrome_descendant(9735))
print(palindrome_descendant(97358817))
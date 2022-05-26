"""
Zygodromes
A number is Zygodrome if it can be partitioned into clusters of repeating digits with a length equals or greater than two (as to say that repeating digits need to be placed as an adjacent pair or a greater group, and that no single digits are allowed).

Given a non-negative integer num, implement a function that returns True if num is a Zygodrome number, or False otherwise.

Examples
is_zygodrome(11) ➞ True
# 11 is a pair of repeated digits

is_zygodrome(33322) ➞ True
# 333 is a triplet of repeated digits, and 22 is a pair

is_zygodrome(5) ➞ False
# 5 is a single digit, it doesn't form a pair

is_zygodrome(1001) ➞ False
# 00 is a pair, but the two 1's are not adjacent
Notes
Trivia: the number 9997777 is the only known Zygodrome prime whose index in the Zygodromes sequence (664444) is a prime in turn.
You can expect only non-negative integers as given input, without exceptions to handle.
"""
import re

def is_zygodrome(num):

	# v3
	return not re.sub(r"(\d)\1+", "", str(num))

	# v2
	# num = str(num)
	# check = False
	# for x,y in zip(num, num[1:]):
	# 	if x != y and check == False:
	# 		return False
	# 	check = x == y
	# return check




	# v1
	# isEqual = True
	#
	# if len(str(num)) > 1:
	# 	for i in range(0, len(str(num))):
	# 		if i != len(str(num)) - 1:
	# 			if isEqual != False:
	# 				if str(num)[i] == str(num)[i + 1]:
	# 					isEqual = True
	# 				else:
	# 					isEqual = False
	# 			else:
	# 				if str(num)[i] == str(num)[i + 1]:
	# 					isEqual = True
	# 				else:
	# 					isEqual = False
	# 					return isEqual
	# 		if i == len(str(num)) - 1:
	# 			return isEqual
	# else:
	# 	return False


print(is_zygodrome(11))
print(is_zygodrome(222))
print(is_zygodrome(223))
print(is_zygodrome(33322))
print(is_zygodrome(1001))
print(is_zygodrome(1100))
print(is_zygodrome(11222))
print(is_zygodrome(3344466777))
print(is_zygodrome(1))
print(is_zygodrome(0))
print(is_zygodrome(5))
print(is_zygodrome(8866611229999))
print(is_zygodrome(9977866655522))
print(is_zygodrome(99999999))







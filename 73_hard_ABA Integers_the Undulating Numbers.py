"""
ABA Integers: the Undulating Numbers
In this challenge, you have to establish if a given number is undulating. A number n is undulating when the following conditions are all true:

n has at least three digits.
n has exactly two different digits.
The two digits of n are alternating without repeating groups.
If we think of the first digit of an undulating number as an "A", and the second digit as a "B", we notice a sequence of the form "ABA" that can repeat infinite times and ends either with an "A" or with a "B", but without clusters of "AA" or "BB" in it.

Given a positive integer n, implement a function that returns True if n is an Undulating number, or False if it's not.

Examples
is_undulating(121) ➞ True
# A = 1, B = 2
# The sequence ABA is valid

is_undulating(373737) ➞ True
# A = 3, B = 7
# The sequence ABABABAB is valid

is_undulating(12) ➞ False
# Less than three digits

is_undulating(12122) ➞ False
# The sequence ABABB is not valid

is_undulating(85856) ➞ False
# More than two different digits
"""
import re

def is_undulating(n):

	s = str(n)
	return re.match(r'(.)(.)(\1\2)*\1\2?$', s) and s[0] != s[1] or False



	# n = str(n)
	# if len(n) < 3:
	# 	return False
	# if len(set(n))!= 2:
	# 	return False
	# return all(a!=b for a, b in zip(n, n[1:]))



	# if len(str(n)) <= 2:
	# 	return False
	#
	# if len(set(str(n))) == 1:
	# 	return False
	# else:
	# 	for i in range(2, len(str(n))):
	# 		if str(n)[i-2] != str(n)[i]:
	# 			return False
	# return True

print(is_undulating(121))
print(is_undulating(373737))
print(is_undulating(12))
print(is_undulating(12122))
print(is_undulating(85856))
print(is_undulating(8888))








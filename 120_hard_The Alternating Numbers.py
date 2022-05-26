"""
The Alternating Numbers
In this challenge, you have to establish if an integer num is Alternating. To be Alternating, num must be positive and every digit in its sequence must have a different parity than its next and its previous digit.

Given an integer num, implement a function that returns True is num is an Alternating number, or False if it's not.

Examples
is_alternating(123) ➞ True
# 1 is odd, 2 is even, 3 is odd

is_alternating(67) ➞ True
# 6 is even, 7 is odd

is_alternating(2380) ➞ False
# 2 is even, 3 is odd, 8 is even, 0 is even

is_alternating(75) ➞ False
# 7 is odd, 5 is odd
Notes
A single-digit number is trivially considered Alternating, given the absence of neighboring digits.
The first digit has to be compared only to its next neighbor, and the last digit has to be compared only to its previous neighbor.
Every non-positive integer must be treated as False.
"""

def is_alternating(num):

	# v4
	s = str(num)
	return num > 0 and all((int(a)+int(b)) % 2 for a, b in zip(s, s[1:]))


	# v3
	# if num < 0:
	# 	return False
	# if num < 10:
	# 	return True
	# else:
	# 	n = "".join('o' if int(d) % 2 else 'e' for d in str(num))
	# 	return not "oo" in n and not "ee" in n


	# v2
	# if num <= 0:
	# 	return False
	# for i in range(0, len(str(num)) -1):
	# 	if int(str(num)[i]) % 2 == int(str(num)[i+1]) % 2:
	# 		return False
	# return True


	# v1
	# even = False
	# odd = False
	# count = len(str(num)) - 1
	# result = []
	#
	# if int(str(num)[count]) == 0 and len(str(num)) == 1:
	# 	return False
	# elif int(str(num)[count]) % 2 == 0:
	# 	even = True
	# 	result.append(True)
	# 	count -= 1
	# elif int(str(num)[count]) % 2 != 0:
	# 	odd = True
	# 	result.append(True)
	# 	count -= 1
	#
	# while count >= 0:
	# 	try:
	# 		if odd is True and even is False:
	# 			if int(str(num)[count]) % 2 == 0:
	# 				even = True
	# 				odd = False
	# 				count -= 1
	# 				result.append(True)
	# 				continue
	# 			else:
	# 				count -= 1
	# 				result.append(False)
	# 				break
	# 		if even is True and odd is False:
	# 			if int(str(num)[count]) % 2 != 0:
	# 				odd = True
	# 				even = False
	# 				count -= 1
	# 				result.append(True)
	# 				continue
	# 			else:
	# 				count -= 1
	# 				result.append(False)
	# 				break
	# 	except ValueError:
	# 		return False
	# return all(result)

print(is_alternating(123))
print(is_alternating(67))
print(is_alternating(2380))
print(is_alternating(75))
print(is_alternating(3))
print(is_alternating(903))
print(is_alternating(444))
print(is_alternating(0))
print(is_alternating(14589))
print(is_alternating(1234566789))
print(is_alternating(-12))
print(is_alternating(10))


















"""
Persistence
If you take an integer and form the product of its individual digits, you get a smaller number. Keep doing this and eventually you end up with a single digit.

The number of steps it takes to reach this point is known as the integer's multiplicative persistence. For example, 347 has a persistence of 3: 3*4*7 = 84, 8*4 = 32, 3*2 = 6.

Devise a function that returns the persistence of an integer.

Examples
persistence(9) ➞ 0

persistence(12) ➞ 1

persistence(6788) ➞ 6

persistence(678852) ➞ 2
Notes
The smallest number with persistence 11 is 277777788888899.
A number has never been found, no matter how large, that has a persistence greater than 11.
"""

def persistence(n):

	# v2
	return 0 if n < 10 else 1 + persistence(eval("*".join(str(n))))

	# v1
	# if len(str(n)) > 1:
	# 	return 1 + persistence(eval("*".join(list(str(n)))))
	# else:
	# 	return 0

print(persistence(6788))
print(persistence(678852))


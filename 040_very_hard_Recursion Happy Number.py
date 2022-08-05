"""
Recursion: Happy Number
A happy number is a number which yields a 1 by repeatedly summing up the square of its digit. If such a process results in an endless cycle of numbers containing 4, the number is said to be an unhappy number.

Create a function that accepts a number and determines whether the number is a happy number or not. Return True if so, False otherwise.

Examples
is_happy(67) ➞ False

is_happy(89) ➞ False

is_happy(139) ➞ True

is_happy(1327) ➞ False

is_happy(2871) ➞ False

is_happy(3970) ➞ True
"""

def is_happy(num):

	if num == 1:
		return True
	elif num == 4:
		return False

	return is_happy(sum(int(i) ** 2 for i in str(num)))

print(is_happy(67))
print(is_happy(89))
print(is_happy(139))
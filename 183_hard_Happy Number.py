"""
Happy Number
A happy number is a number which yields a 1 by repeatedly summing up the square of its digits. If such a process results in an endless cycle of numbers containing 4, the number is said to be an unhappy number.

Create a function that accepts a number and determines whether the number is a happy number or not. Return True if so, False otherwise.

Examples
is_happy(67) ➞ False

is_happy(89) ➞ False

is_happy(139) ➞ True

is_happy(1327) ➞ False

is_happy(2871) ➞ False

is_happy(3970) ➞ True
Notes
Hint: Your loop terminates if the value of n is either 1 or 4.
Alternatively, you can solve this challenge via a recursive approach.
"""
# v3
def is_happy(n):
	while n not in [1, 4]:
		n = sum(int(i)**2 for i in str(n))
	return [False, True][n == 1]

# v2
# def is_happy(n):
#
# 	while True:
# 		n = sum([int(d)**2 for d in str(n)])
# 		print(n)
# 		if n in [1, 4]:
# 			return n == 1

# v1
# def is_happy(num):
#
# 	result = 0
#
# 	try:
# 		for i in str(num):
# 			result += int(i)**2
# 		if result == 1:
# 			return True
# 		return is_happy(result)
# 	except:
# 		return False

print(is_happy(67))
print(is_happy(89))
print(is_happy(139))
print(is_happy(1327))
print(is_happy(2871))
print(is_happy(3970))



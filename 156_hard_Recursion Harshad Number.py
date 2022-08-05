"""
Recursion: Harshad Number
A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12

is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171

is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True
Notes
You are expected to solve this challenge via recursion.
"""
def is_harshad(n):
	return n % recur(n) == 0

def recur(n):
	if n < 10:
		return n
	return n % 10 + recur(n // 10)


# def is_harshad(num, index=0, div_num=0):

	# v1
	# if index < len(str(num)):
	# 	div_num += int(str(num)[index])
	# 	return is_harshad(num, index+1, div_num)
	# return num % div_num == 0


print(is_harshad(171))
print(is_harshad(481))
print(is_harshad(89))


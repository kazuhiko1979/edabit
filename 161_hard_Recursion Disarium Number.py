"""
Recursion: Disarium Number
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself. Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True
Notes
Position of the digit is not likely its index.
You are expected to solve this challenge via recursion.
"""

# v2
def is_disarium(num, res=0, index=1):

	if index > len(str(num)):
		return res == num
	else:
		return is_disarium(num, res + int(str(num)[index-1])**index, index+1)

# v1
# def is_disarium(num, res=0, total=0):
#
# 	if res < len(str(num)):
# 		total += int(str(num)[res]) ** (res + 1)
# 		return is_disarium(num, res+1, total)
# 	if res == len(str(num)):
# 		return num == total

print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(466))
print(is_disarium(8))
"""
Sort the String
Create a function that takes a string consisting of lowercase letters, uppercase letters and numbers and returns the string sorted in the same way as the examples below.

Examples
sorting("eA2a1E") ➞ "aAeE12"
// Don't repeat letters.

sorting("Re4r") ➞ "erR4"

sorting("6jnM31Q") ➞ "jMnQ136"

sorting("846ZIbo") ➞ "bIoZ468"
Notes
Don't repeat letters (numbers can be repeated).
"""

def sorting(s):

	# v3
	return ''.join(sorted(s, key=lambda x: (x.isdigit(), x.lower(), x.isupper())))

	# v2
	# new_key = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'
	# return ''.join(sorted(s, key=new_key.index))


	# v1
	# result = []
	# num = []
	#
	# s = sorted(s, reverse=True)
	# for i in s:
	# 	if i.islower():
	# 		result.append(i)
	# 	if i.isupper():
	# 		result.append(i)
	# 	if i.isdigit():
	# 		num.append(i)
	#
	# sorted_items = sorted(result, key=str.lower)
	#
	# return ''.join(sorted_items + sorted(num))



print(sorting("eA2a1E"))
print(sorting("6jnM31Q"))
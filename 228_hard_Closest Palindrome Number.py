"""
Closest Palindrome Number
Write a function that returns the closest palindrome number to an integer. If two palindrome numbers tie in absolute distance, return the smaller number.

Examples
closest_palindrome(887) ➞ 888

closest_palindrome(100) ➞ 99
# 99 and 101 are equally distant, so we return the smaller palindrome.

closest_palindrome(888) ➞ 888

closest_palindrome(27) ➞ 22
Notes
If the number itself is a palindrome, return that number.
"""
# v3
def closest_palindrome(num):
	n = 0
	while num:
		if str(num-n) == str(num-n)[::-1]:
			return num-n
		elif str(num+n) == str(num+n)[::-1]:
			return num+n
		n += 1



# v2
# def closest_palindrome(num):
#
# 	a = b = num
# 	while True:
# 		if str(a) == str(a)[::-1]:
# 			return a
# 		a -= 1
#
# 		if str(b) == str(b)[::-1]:
# 			return b
# 		b += 1


# v1
# def closest_palindrome(s):
#
# 	high, low = s, s
#
# 	while str(high) != str(high)[::-1]:
# 		high += 1
# 	while str(low) != str(low)[::-1]:
# 		low -= 1
#
# 	diff = [abs(s - high), abs(s - low)]
#
# 	if set(diff) == {0}:
# 		return [high, low][0]
# 	if len(set(diff)) == 1:
# 		t = [high, low].index(min([high, low]))
# 		return [high, low][t]
# 	else:
# 		t = diff.index(min(diff))
# 		return [high, low][t]



print(closest_palindrome(887))
print(closest_palindrome(100))
print(closest_palindrome(888))
print(closest_palindrome(27))
print(closest_palindrome(519))
print(closest_palindrome(4892))
print(closest_palindrome(1))
print(closest_palindrome(100))
print(closest_palindrome(33344))
print(closest_palindrome(123456))
print(closest_palindrome(978215236))






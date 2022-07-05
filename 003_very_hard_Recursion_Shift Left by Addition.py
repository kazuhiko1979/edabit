"""
Recursion: Shift Left by Addition
The shift left operation is similar to multiplication by powers of two. This can also be achieved with repetitive addition, thus, the process can be done recursively.

Sample calculation using the shift left operator <<:

10 << 3 = 10 * 2^3 = 10 * 8 = 80
-32 << 2 = -32 * 2^2 = -32 * 4 = -128
5 << 2 = 5 * 2^2 = 5 * 4 = 20
Create a recursive function that mimics the shift left operator and returns the result from the two given integers.

Examples
shift_left(5, 2) ➞ 20

shift_left(10, 3) ➞ 80

shift_left(-32, 2) ➞ -128

shift_left(-6, 5) ➞ -192

shift_left(12, 4) ➞ 192

shift_left(46, 6) ➞ 2944
Notes
There will be no negative values for the second parameter y.
You're expected to solve this challenge using a recursive approach.
"""

def shift_left(x, y):

	# if y:
	# 	return shift_left(x+x, y-1)
	# else:
	# 	return x

	return shift_left(2*x, y-1) if y > 0 else x

print(shift_left(5, 2))
print(shift_left(10, 3))
print(shift_left(-6, 5))
print(shift_left(46, 6))


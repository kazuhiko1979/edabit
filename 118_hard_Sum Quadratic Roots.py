"""
Sum Quadratic Roots
Given a, b and c, find the roots of the equation ax^2 +bx +c = 0 and then add them together.

Round your answer to two decimal places.
If there is only one real root return 1.
If there are no real roots, return 0.
Examples
find_roots_sum(2, 4, -6) ➞ -2.00

find_roots_sum(3, 4, -3) ➞ -1.33

find_roots_sum(4, 3, -8) ➞ -0.75
Notes
The Discriminant of a quadratic equation is b^2-4(a)(c).
"""

def find_roots_sum(a,b,c):

	# v2
	d = b*b - 4*a*c
	return - round(b / a, 2) if d > 0 else 1 if d == 0 else 0


	# v1
	# val = (b ** 2 - (4 * a * c)) ** 0.5
	#
	# root_1 = (-b + val) / (2 * a)
	# root_2 = (-b - val) / (2 * a)
	#
	#
	# if type(root_1) is complex:
	# 	return 0
	# elif root_1 == root_2:
	# 	return 1
	# else:
	# 	return round(root_1 + root_2, 2)

print(find_roots_sum(2, 4, -6))
print(find_roots_sum(3, 4, -3))
print(find_roots_sum(4, 3, -8))
print(find_roots_sum(2, 4, 2))
print(find_roots_sum(3, 4, 3))


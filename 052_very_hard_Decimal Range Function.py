"""
Decimal Range Function
Create a function that can take 1, 2, or 3 arguments (like the range function) and returns a tuple. This should be able to return float values (as opposed to the range function which can't take float values as a step).

Examples
drange(1.2, 5.9, 0.45) ➞ (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)

drange(10) ➞ (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

drange(1, 7, 1.2) ➞ (1, 2.2, 3.4, 4.6, 5.8)
# Here 7 is not included, like in the range function.
Notes
Always round values to the number with the most decimal digits (e.g. in the first example, the answer should always be rounded to 2 digits. In the second, it should be rounded to 0 digits and the third, 1 digit)
"""
from numpy import arange

# v2
def drange(*args):

	return tuple(round(n, 5) for n in arange(*args))


# v1
# def drange(*args):
#
# 	if len(args) == 1:
# 		return tuple([i for i in range(0, args[0])])
# 	if len(args) == 2:
# 		return tuple([i for i in range(args[0], args[1])])
# 	else:
# 		start, ranges, end = args[0], args[2], args[1]
# 		result = [start]
#
# 		while start < end:
# 			start = start + ranges
# 			result.append(round(start, 3))
# 		return tuple(result[:-1])

print(drange(1.2, 5.9, 0.45))
print(drange(10))
print(drange(1, 7, 1.2))
print(drange(3, 10))
print(drange(0.112, 13, 3.27))


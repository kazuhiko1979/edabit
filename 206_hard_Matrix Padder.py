"""
Pascal's Triangle
Mubashir was reading about Pascal's triangle on Wikipedia.

In mathematics, Pascal's triangle is a triangular array of the binomial coefficients that arises in probability theory, combinatorics, and algebra.

Mubashir

Formula for Pascal's triangle is given by:

Mubashir

where n denotes a row of the triangle, and k is the position of a term in the row.

Create a function which takes a number n and returns n top rows of Pascal's Triangle flattened into a one-dimensional list.

Examples
pascals_triangle(1) ➞ [1]

pascals_triangle(2) ➞ [1, 1, 1]

pascals_triangle(4) ➞ [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
"""
from math import factorial as fact

def pascals_triangle(n):

	res = []
	for i in range(n):
		res += [pascal_value(i, j) for j in range(i+1)]
	return res

def pascal_value(n, k):
	return int(fact(n) / (fact(k) * fact(n-k)))

# import sympy
#
# def pascals_triangle(num):
#
# 	x = sympy.Symbol('x')
# 	result = []
#
# 	for i in range(0, num):
# 		expr = (x+1)**i
# 		expr_ex = str(sympy.expand(expr)).split('+')
# 		for f in expr_ex:
# 			f = f.replace(" ", "")
# 			if f.replace(" ", "")[0] == 'x':
# 				result.append(1)
# 			else:
# 				result.append(int(f[0]))
# 	return result

print(pascals_triangle(0))
print(pascals_triangle(1))
print(pascals_triangle(2))
print(pascals_triangle(3))
print(pascals_triangle(4))
print(pascals_triangle(5))

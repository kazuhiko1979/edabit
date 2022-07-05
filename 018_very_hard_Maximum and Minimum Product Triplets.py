"""
Maximum and Minimum Product Triplets
Write two functions:

One that returns the maximum product of three numbers in a list.
One that returns the minimum product of three numbers in a list.
Examples
max_product([-8, -9, 1, 2, 7]) ➞ 504

max_product([-8, 1, 2, 7, 9]) ➞ 126

min_product([1, -1, 1, 1]) ➞ -1

min_product([-5, -3, -1, 0, 4]) ➞ -15
"""

# v3
def max_product(lst):

	s = sorted(lst)
	return max(s[-1]*s[-2]*s[-3], s[-1]*s[0]*s[1])

def min_product(lst):
	s = sorted(lst)
	return min(s[0]*s[1]*s[2], s[0]*s[-1]*s[-2])



# v2
# def products(lst):
#
# 	products = []
#
# 	for i in range(0, len(lst)-1):
# 		for j in range(i+1, len(lst)-1):
# 			for k in range(j+1, len(lst)):
# 				products.append(lst[i] * lst[j] * lst[k])
# 	return products
#
#
# def max_product(lst):
# 	return max(products(lst))
#
# def min_product(lst):
# 	return min(products(lst))



# v1
# import itertools
#
#
# def max_product(lst) -> int:
#
# 	combs = [comb for comb in itertools.combinations(lst, 3)]
# 	return max([elem[0] * elem[1] * elem[2] for elem in combs])
#
# def min_product(lst) -> int:
#
# 	combs = [comb for comb in itertools.combinations(lst, 3)]
# 	return min([elem[0] * elem[1] * elem[2] for elem in combs])


print(max_product([-8, -9, 1, 2, 7]))
print(max_product([-8, 1, 2, 7, 9]))

print(min_product([1, -1, 1, 1]))
print(min_product([-5, -3, -1, 0, 4]))
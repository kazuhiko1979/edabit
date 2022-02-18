"""
Return Exponents of Prime Factors
You are given a list of prime factors lst and a target. When each number in the list is raised to an appropriate power their product will be equal to the target.

Your role is to return the exponents. All these lists will have a length of three. Basically, it is three numbers whose product is equal to challenge. The only difference is what you are expected to return.

Examples
product_equal_target([2, 3, 5], 600) ➞ [3, 1, 2]
# Because 2^3*3^1*5^2 = 600

product_equal_target([2, 3, 5], 720) ➞ [4, 2, 1]
# Because 2^4*3^2*5^1 = 720
Notes
The exponents you will return are expected to replace the base in the list.
Your returned values must be in the same order as the bases.
"""

import math

def product_equal_target(lst, target):


	exps = []

	for base in lst:
		exp = 0
		while target % base == 0:
			target /= base
			exp += 1
		exps.append(exp)
	return exps




	# 参考：リストを利用しない場合、応用？　あくまで因数分解

	# factor = {}
	# div = 2
	#
	# s = math.sqrt(target)
	# while div < s:
	# 	div_cnt = 0
	# 	while target % div == 0:
	# 		div_cnt += 1
	# 		target //= div
	# 	if div_cnt != 0:
	# 		factor[div] = div_cnt
	# 	div += 1
	#
	# if target > 1:
	# 	factor[target] = 1
	#
	# return factor
	# # return [value for key, value in factor.items()]


print(product_equal_target([2, 3, 5], 600))
print(product_equal_target([2, 3, 19], 1026))
print(product_equal_target([2, 3, 5], 600))
print(product_equal_target([2, 37, 149], 11026))
print(product_equal_target([2, 3, 5], 180))

#
print(product_equal_target([2, 3, 5], 2599))
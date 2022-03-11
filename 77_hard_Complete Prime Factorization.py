"""
Complete Prime Factorization
Create a function that decomposes an integer into its prime factors, ordered from smallest to largest.

For instance:

complete_factorization(24) = [2, 2, 2, 3]
# Since 24 = 8 x 3 = 2^3 x 3 = 2 x 2 x 2 x 3
Examples
complete_factorization(10) ➞ [2, 5]

complete_factorization(9) ➞ [3, 3]

complete_factorization(72) ➞ [2, 2, 2, 3, 3]
Notes
1 is not considered a prime number, so omit it in your final list of prime factors.
"""
import math

def complete_factorization(n):

	temp = []

	i = 2

	while i <= n:
		if not n % i:
			n /= i
			temp.append(i)
		else:
			i += 1
	return temp



	# temp = []
	#
	# while n % 2 == 0:
	# 	temp.append(2)
	# 	n = n / 2
	#
	# for i in range(3, int(math.sqrt(n))+1, 2):
	# 	while n % i == 0:
	# 		temp.append(int(i))
	# 		n = n / i
	#
	# if n > 2:
	# 	temp.append(int(n))
	# return temp


print(complete_factorization(24))
print(complete_factorization(10))
print(complete_factorization(72))
print(complete_factorization(315))
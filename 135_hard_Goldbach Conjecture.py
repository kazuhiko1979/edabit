"""
Goldbach Conjecture
Goldbach's Conjecture is amongst the oldest and well-known unsolved mathematical problems. In correspondence with Leonhard Euler in 1742, German mathematician Christian Goldbach made a conjecture, which states:

"Every even whole number greater than 2 is the sum of two prime numbers."

Even though it's been thoroughly tested and analyzed and seems to be true, it hasn't been proved yet (thus, remaining a conjecture.)

Create a function that takes a number and returns an array as per the following rules:

If the given number is odd and greater than two, return an empty array.
If the given number is even and greater than two, return an array of two prime numbers whose sum is the given input.
Both prime numbers must be the farthest (with the greatest difference).
Examples
goldbach_conjecture(1) ➞ []
# The given number is not greater than 2.

goldbach_conjecture(7) ➞ []
# The given number is not an even number.

goldbach_conjecture(14) ➞ [3, 11]
"""

from itertools import combinations

def goldbach_conjecture(n):

# v3
	if n == 1 or n % 2:
		return []

	for i in range(2, n):
		if is_prime(i) and is_prime(n-i):
			return [i, n-i]
	return []

def is_prime(n):
	return all(n % i for i in range(2, int(n**0.5)+1))




# v2
# 	if n == 1 or n % 2:
# 		return []
#
# 	primes = [i for i in range(2, n) if is_prime(i)]
# 	for i in primes:
# 		for j in primes[::-1]:
# 			if i + j == n:
# 				return [i, j]
#
# def is_prime(n):
# 	return all(n % i for i in range(2, int(n**0.5)+1))


	# v1
	# prime = []
	# if n > 1 and n % 2 == 0:
	# 	for i in range(2, n+1):
	# 		for j in range(2, int(i**0.5) +1):
	# 			if i % j == 0:
	# 				break
	# 		else:
	# 			prime.append(i)
	#
	# comb = list(combinations(prime, 2))
	# for tup in comb:
	# 	if sum(tup) == n:
	# 		return sorted(list(tup))
	# if n % 2 == 0:
	# 	return [n / 2] * 2
	# return []



print(goldbach_conjecture(1))
print(goldbach_conjecture(4))
print(goldbach_conjecture(7))
print(goldbach_conjecture(8))
print(goldbach_conjecture(10))
print(goldbach_conjecture(24))
print(goldbach_conjecture(100))
print(goldbach_conjecture(1234))
print(goldbach_conjecture(1400))
print(goldbach_conjecture(1566))
print(goldbach_conjecture(3444))



# from itertools import combinations
#
# def all_pairs(lst, target):

	# v4
	# return [list(i) for i in combinations(sorted(lst), 2) if sum(i) == target]


	# v3
	# result = []
	# comb = list(combinations(lst, 2))
	# # print(comb)
	# for tup in comb:
	# 	if sum(tup) == target:
	# 		result.append(tup)
	# return sorted([sorted(list(i)) for i in result])


	# v2
	# return sorted([sorted([a, b]) for idx, a in enumerate(lst) for b in lst[idx+1:] if sum([a, b]) == target])

	# V1
	# result = []
	# for idx, a in enumerate(lst):
	# 	for b in lst[idx+1:]:
	# 		if sum([a,b]) == target:
	# 			result.append(sorted([a,b]))
	# return sorted(result)

# print(all_pairs([2, 4, 5, 3], 7))
# print(all_pairs([5, 3, 9, 2, 1], 3))
# print(all_pairs([4, 5, 1, 3, 6, 8], 9))
# print(all_pairs([5, 2], 14))
# print(all_pairs([5, 5, 2], 14))
# print(all_pairs([8, 7, 7, 2, 4, 6], 14))
# print(all_pairs([8, 7, 2, 4, 6], 14))
# print(all_pairs([1, 3, 5, 4, 0], 4))







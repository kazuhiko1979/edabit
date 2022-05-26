"""
Sieve of Eratosthenes

Given num as input, return a list with all primes up to num included.

Alternative Text

Examples
eratosthenes(1) ➞ []

eratosthenes(10) ➞ [2, 3, 5, 7]

eratosthenes(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]

eratosthenes(0) ➞ []
"""

def eratosthenes(n):

	# v3
	if n < 2:
		return []
	lst = []
	for num in range(2, n+1):
		if all(num%i for i in lst):
			lst+=[num]
	return lst


	# v2
	# if n < 2:
	# 	return []
	#
	# sieve = [True] * n
	# sieve[0], sieve[1] = False, False
	#
	# for i in range(2, int(n ** 0.5) + 1):
	# 	p = i * 2
	# 	while p < n:
	# 		sieve[p] = False
	# 		p += i
	#
	# return [i for i in range(n) if sieve[i]]


	# v1
	# prime = [True for i in range(n + 1)]
	# p = 2
	#
	# while (p * p <= n):
	# 	if prime[p] == True:
	# 		for i in range(p**2, n+1, p):
	# 			prime[i] = False
	# 	p += 1
	#
	# if n == 0 or n == 1:
	# 	return []
	# else:
	# 	prime[0] = False
	# 	prime[1] = False
	# 	return [p for p in range(n + 1) if prime[p]]

print(eratosthenes(10))
print(eratosthenes(0))
print(eratosthenes(20))
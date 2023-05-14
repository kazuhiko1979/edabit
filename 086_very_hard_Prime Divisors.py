"""
Prime Divisors
Given a number, return all its prime divisors in a list. Create a function that takes a number as an argument and returns all its prime divisors.

To illustrate:

If n = 27
All divisors are: [3, 9, 27]
Finally, from that list of divisors, return the prime ones: [3]
Examples
prime_divisors(27) ➞ [3]

prime_divisors(99) ➞ [3, 11]

prime_divisors(3457) ➞ [3457]
"""
# v3
def divs(n):
	return [i for i in range(2, n + 1) if not n % i]


def is_prime(n):
	return all(n % i for i in range(2, n))


def prime_divisors(num):
	return [n for n in divs(num) if is_prime(n)]



# v2
# from math import sqrt
#
# def prime_divisors(num):
# 	for i in range(2, int(sqrt(num)) + 1):
# 		if num % i == 0:
# 			return sorted(list(set([i] + prime_divisors(num // i))))
# 	return [num]

# v1
def prime_divisors(n):

	c = 2
	result = []
	while (n > 1):
		if (n % c == 0):
			result.append(c)
			n = n / c
		else:
			c = c + 1
	return sorted(list(set(result)))

print(prime_divisors(27))
print(prime_divisors(24))
print(prime_divisors(478170))
print(prime_divisors(1386))
print(prime_divisors(462))
print(prime_divisors(99))







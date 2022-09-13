"""
Interprime Numbers
An interprime number is a composite number which is equidistant from two consecutive primes. For example, the interprime 6 is 1 point after 5, a prime, and 1 point before the next prime, 7. Another interprime is 93, which lies midway between primes 89 and 97.

Create a function that takes a number n as input. If n is an interprime number, return a list containing the two consecutive primes between which it lies. If it isn't, return an empty list.

Examples
interprime(6) ➞ [5, 7]

interprime(9) ➞ [7, 11]

interprime(8) ➞ []
Notes
Interprimes cannot be prime themselves (otherwise the primes would not have been consecutive).
"""

# v2
def interprime(n):

	m, o = n, n

	while not is_prime(m) and not is_prime(o):
		m -= 1
		o += 1
	return [m, o] if m != n and is_prime(m) and is_prime(o) else []


def is_prime(x):
	return all(x % i for i in range(2, x))




# v1
# def is_prime(x):
# 	return all(x % i for i in range(2, x))
#
# def previous_prime_number(num):
# 	for i in range(num-1, 1, -1):
# 		for j in range(2, i):
# 			if i % j == 0:
# 				break
# 		else:
# 			return i
# 			break
#
# def interprime(x):
#
# 	if is_prime(x):
# 		return []
# 	next_prime = min([a for a in range(x + 1, 2 * x) if is_prime(a)])
# 	previous_prime = previous_prime_number(x)
# 	if x - previous_prime == next_prime - x:
# 		return [previous_prime, next_prime]
# 	else:
# 		return []



print(interprime(6))
print(interprime(9))
print(interprime(473))
print(interprime(373))
print(interprime(756))
print(interprime(413))
print(interprime(924))



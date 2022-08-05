"""
Factor Tractor
Write a function to find all the prime factors of a given integer. The function must return a list containing all the prime factors, sorted in ascending order. Remember that 1 is neither prime nor composite and should not be included in your output list.

Examples
prime_factorize(25) ➞ [5, 5]

prime_factorize(19) ➞ [19]

prime_factorize(77) ➞ [7, 11]
Notes
Output list must be sorted in ascending order.
The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.
"""

def prime_factorize(num):

	if num == 1:
		return []
	i = 2
	while i < num:
		if num % i == 0:
			break
		i += 1
	return [i] + prime_factorize(num//i)

print(prime_factorize(25))
print(prime_factorize(19))
print(prime_factorize(77))

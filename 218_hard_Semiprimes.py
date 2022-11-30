"""
Semiprimes
A semiprime is a composite number that is the product of two primes. Apart from these two primes, its only other proper (non-self) divisor is 1.

The two prime factors of a semiprime can be the same number (e.g. the semiprime 49 is the product of 7x7). A semiprime that has two distinct prime factors is called a squarefree semiprime.

Create a function that takes a number and returns "Squarefree Semiprime", "Semiprime", or "Neither".

Examples
semiprime(49) ➞ "Semiprime"

semiprime(15) ➞ "Squarefree Semiprime"

semiprime(97) ➞ "Neither"
"""

def semiprime(num):

	result = []

	for i in range(1, num+1):
		for j in range(1, num+1):
			if i * j == num:
				if isPrime(i, j):
					result.append([i, j])

	if result:
		if result[0][0] == result[0][1]:
			return "Semiprime"
		if result[0][0] != result[0][1]:
			return "Squarefree Semiprime"
	else:
		return "Neither"


def isPrime(num_1, num_2):

	if num_1 == 1 or num_2 == 1:
		return False

	for i in range(2, num_1):
		if (num_1 % i) == 0:
			return False

	for i in range(2, num_2):
		if (num_1 % i) == 0:
			return False

	return True

print(semiprime(49))
print(semiprime(15))
print(semiprime(19))
print(semiprime(75))
print(semiprime(169))
print(semiprime(203))
print(semiprime(177))
print(semiprime(125))
print(semiprime(70))



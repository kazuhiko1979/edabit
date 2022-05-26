"""
Moran Numbers
A Harshad number is a number which is divisible by the sum of its digits. For example, 132 is divisible by 6 (1+3+2).

A subset of the Harshad numbers are the Moran numbers. Moran numbers yield a prime when divided by the sum of their digits. For example, 133 divided by 7 (1+3+3) yields 19, a prime.

Create a function that takes a number and returns "M" if the number is a Moran number, "H" if it is a (non-Moran) Harshad number, or "Neither".

Examples
moran(132) ➞ "H"

moran(133) ➞ "M"

moran(134) ➞ "Neither"
"""

def moran(n):

	# v3
	def is_prime(n):
		return all(n%1 for i in range(2, n))

	s = sum(int(i) for i in str(n))
	return 'M' if is_prime(int(n/s)) else 'H' if not n % s else 'Neither'


	# v2
	# def is_prime(n):
	# 	if n <= 1:
	# 		return False
	# 	for i in range(2, int(n**0.5) + 1):
	# 		if not n % i:
	# 			return False
	# 	return True
	#
	# d = sum(int(i) for i in str(n))
	# if n % d:
	# 	return 'Neither'
	# return 'M' if is_prime(n//d) else 'H'


	# # v1
	# # 素数判定
	# def isprime(n) -> bool:
	# 	if n <= 1:
	# 		return False
	#
	# 	for x in range(2, int(n ** 0.5) + 1):
	# 		if n % x == 0:
	# 			return False
	# 	return True
	#
	# divided = n / sum(list(map(int, str(n))))
	#
	# # 割り切れるか、割り切れないか判定
	# if n % sum(list(map(int, str(n)))) == 0:
	# 	if isprime(int(divided)):
	# 		return 'M'
	# 	else:
	# 		return 'H'
	# else:
	# 	return 'Neither'



print(moran(132))
print(moran(133))
print(moran(134))
print(moran(3033))
print(moran(3030))
print(moran(491423))
print(moran(20937))


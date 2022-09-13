"""
Find the Primorial
A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.

Create a function that returns the Primorial of a number.

Examples
primorial(1) ➞ 2

primorial(2) ➞ 6

primorial(8) ➞ 9699690
"""

def primorial(num):

	lst = [2]
	x = 3
	while len(lst) < num:
		for i in lst:
			if not x % i:
				x += 2
				continue
		lst.append(x)
		x += 2

	result = 1

	for i in lst:
		result *= i
	return result

	# no work
	# for i in range(2, 4):
	# 	print(i)
	# print(2 % 2)

	# while len(prime_list) < num:
	# 	# if prime >= 2:
	# 	# 	for i in range(2, prime+1):
	#
	# 	if prime % div == 0:
	# 		prime += 1
	# 	else:
	# 		prime_list.append(prime)
	# return prime_list


print(primorial(8))
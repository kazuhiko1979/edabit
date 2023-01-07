"""
LCM of More Than Three Numbers
Create a function that takes a list of more than three numbers and returns the Least Common Multiple (LCM).

Examples
lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520

lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340

lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760
Notes
The LCM of a list of numbers is the smallest positive number that is divisible by each of the numbers in the list.
"""
# v3
from functools import reduce


def lcm_of_list(numbers):

	gcd = lambda a, b: gcd(b, a % b) if b else a
	return reduce(lambda x, y: x*y // gcd(x, y), numbers)



# v2 slow
# def lcm_of_list(numbers):
#
# 	lcm = 1
# 	while True:
# 		for i in numbers:
# 			if lcm % i != 0:
# 				break
# 		else:
# 			return lcm
# 		lcm += 1

# result = []
#
# def lcm_of_list(numbers, gcd=2):
#
# 	return lcm_of_list_helper(numbers, gcd, max(numbers))
#
# def lcm_of_list_helper(numbers, gcd, max_numbers):
#
# 	if not gcd or gcd == 2:
# 		gcd = 2
# 		if ["True" if not i % gcd else i for i in numbers].count('True') > 1:
# 			result.append(gcd)
# 			numbers = [i / gcd if not i % gcd else i for i in numbers]
# 			return lcm_of_list(numbers)
# 		else:
# 			gcd += 1
# 			return lcm_of_list(numbers, gcd)
#
# 	if 2 < gcd <= max_numbers:
# 		if ["True" if not i % gcd else i for i in numbers].count('True') > 1:
# 			result.append(gcd)
# 			numbers = [i / gcd if not i % gcd else i for i in numbers]
# 			gcd = 2
# 			return lcm_of_list(numbers, gcd)
# 		else:
# 			gcd += 1
# 			return lcm_of_list(numbers, gcd)
#
# 	total = 1
# 	for i in result + numbers:
# 		total *= i
# 	result.clear()
#
# 	return int(total)

print(lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(lcm_of_list([13, 6, 17, 18, 19, 20, 37]))
print(lcm_of_list([44, 64, 12, 17, 65]))
print(lcm_of_list([200, 30, 18, 11, 8, 64, 34]))





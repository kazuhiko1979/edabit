"""
Sum of Factors of Factors
Create a function that takes a number and returns the sum of factors of factors of the given number.

Examples
sum_ff(69) ➞ 3, 23 ➞ 0
# Both 3 and 23 are prime numbers and have no factors
# other than 1 and themselves so the result is 0.

sum_ff(12) ➞ 2, 3, 4, 6 ➞ (0) + (0) + (2) + (2+3) ➞ 7

sum_ff(420) ➞ 2,4, 6, 10, 12 ... ➞ (2) + (2+3) + (2+5) + (2+3+4+6) ... ➞ 1175

sum_ff(619) ➞ ___ ➞ 0
# 619 doesn't have any factors (other than 1 and 619).
Notes
The number will always be greater than 0.
Factors that are equal to the number or 1, don't count (see example #1).
"""
# v2
def get_factors(num):

	return [i for i in range(2, num - 1) if num % i == 0]

def sum_ff(num):

	return sum([sum(get_factors(i)) for i in get_factors(num)])


# v1
import itertools

# def sum_ff(num):
#
# 	result = []
#
# 	factors = [i for i in range(1, num + 1) if num % i == 0][1:-1]
#
# 	for factor in factors:
# 		result.append([i for i in range(1, factor + 1) if factor % i == 0][1:-1])
# 	return sum(list(itertools.chain.from_iterable(result)))


print(sum_ff(12))
print(sum_ff(69))
print(sum_ff(420))
print(sum_ff(469))
print(sum_ff(619))
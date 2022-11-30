"""
Mind the Gap
A number is gapful if it is at least 3 digits long and is divisible by the number formed by stringing the first and last numbers together. The smallest number that fits this description is 100. First digit is 1, last digit is 0, forming 10, which is a factor of 100. Therefore, 100 is gapful.

Create a function that takes a number n and returns the closest gapful number (including itself). If there are 2 gapful numbers that are equidistant to n, return the lower one.

Examples
gapful(25) ➞ 100

gapful(100) ➞ 100

gapful(103) ➞ 105
"""
# v2
def gapful(n):

	i = 0
	while True:
		for x in (n-i, n+i):
			s = str(x)
			if x >= 100 and x % int(s[0] + s[-1]) == 0:
				return x
		i += 1

# v1
# def gapful(nbr):
#
# 	fast_last_digit = int(str(nbr)[:1] + str(nbr)[-1])
#
# 	if nbr <= 100:
# 		return 100
# 	numbers = [i for i in range(nbr - fast_last_digit, nbr + fast_last_digit) if i % int(str(i)[:1] + str(i)[-1]) == 0]
#
# 	diff_num = lambda numbers: abs(numbers - nbr)
# 	result = min(numbers, key=diff_num)
#
# 	# diff_num = [abs(nbr - i) for i in numbers]
# 	# return numbers[diff_num.index(min(diff_num))]
#
# 	return result



print(gapful(25))
print(gapful(100))
print(gapful(103))
print(gapful(1442))
print(gapful(3345))
print(gapful(4780))
print(gapful(3078))




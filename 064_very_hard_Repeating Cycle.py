"""
Repeating Cycle
Given an integer n, create a function that returns the length of the repeating cycle of the sequence 1/n. If the cycle is non-repetitive, return -1.

repeating_cycle(13) ➞ 6
# 1/13 = 0.076923 076923 076923 076923 ...
# length of `076923` is 6.
Examples
repeating_cycle(5) ➞ -1
# 1/5 = 0.2 (non-repeative)

repeating_cycle(33) ➞ 2
# 1/33 = 0.03 03 03 03 03 03 03 03
# length of `03` is 2

repeating_cycle(197) ➞ 98
Notes
Return -1 if the repeating cycle does not start from the first decimal place. As an example, 1/22 = 0.0 45 45 45 45, your function should return -1 in this case.
"""
def repeating_cycle(num):

	if num % 2 == 0 or num % 5 == 0:
		return -1
	k = 1
	while pow(10, k, num) != 1:
		k += 1
	return k



# from decimal import *
#
# def repeating_cycle(num):
#
# 	getcontext().prec = 10000
# 	num = str(Decimal('1') / Decimal(num))
# 	temp = ""
# 	result = []
# 	total = ""
# 	for i in range(3, len(num)):
# 		temp += num[i]
# 		try:
# 			if num[i] == '0' and num[i + 1] == temp[0]:
# 				result.append(temp)
# 				temp = ""
# 		except:
# 			sub_total = ""
# 			for j in set(result):
# 				sub_total += j
# 			return len(sub_total)
#
# 	for i in set(result):
# 		total += i
# 	return len(total)


print(repeating_cycle(33))
print(repeating_cycle(18118))
print(repeating_cycle(69))
print(repeating_cycle(197))
print(repeating_cycle(65))
print(repeating_cycle(97))
print(repeating_cycle(19))
print(repeating_cycle(111))
print(repeating_cycle(53))
print(repeating_cycle(59))
print(repeating_cycle(93))

print(repeating_cycle(51))

print(repeating_cycle(159))
print(repeating_cycle(183))
print(repeating_cycle(197))
print(repeating_cycle(167))
print(repeating_cycle(94))
print(repeating_cycle(133))
print(repeating_cycle(218713))
print(repeating_cycle(38127))
print(repeating_cycle(431541))
print(repeating_cycle(221193))





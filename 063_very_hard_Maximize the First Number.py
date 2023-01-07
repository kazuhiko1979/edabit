"""
Maximize the First Number
Write a function that makes the first number as large as possible by swapping out its digits for digits in the second number.

To illustrate:

max_possible(9328, 456) ➞ 9658
# 9658 is the largest possible number built from swaps from 456.
# 3 replaced with 6 and 2 replaced with 5.
Examples
max_possible(523, 76) ➞ 763

max_possible(9132, 5564) ➞ 9655

max_possible(8732, 91255) ➞ 9755
Notes
Each digit in the second number can only be used once.
Zero to all digits in the second number may be used.
"""

# V2
# def max_possible(n1, n2):
#
# 	n1, n2 = list(str(n1)),  sorted(str(n2))
#
# 	for i in range(len(n1)):
# 		if n2 and n1[i] < n2[-1]:
# 			n1[i] = n2.pop()
# 	return int(''.join(n1))


# v1
def max_possible(n1, n2):

	index = 0
	n1 = list(map(int, str(n1)))
	n2 = sorted(map(int, str(n2)))

	while index < len(n1):
		if n2 and n1[index] < n2[-1]:
			n1[index] = n2.pop()
			index += 1
		else:
			index += 1

	return int("".join([str(i) for i in n1]))

print(max_possible(9328, 456))
print(max_possible(523, 76))
# print(max_possible(9132, 5564))
# print(max_possible(8732, 91255))
# print(max_possible(589, 777))
# print(max_possible(1, 0))
# print(max_possible(8, 9))
# print(max_possible(28, 19))
# print(max_possible(12345, 4))



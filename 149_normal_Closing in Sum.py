"""
Closing in Sum
Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.

Worked Example
closing_in_sum(2520) ➞ 72

# The first and last digits are 2 and 0.
# 2 and 0 form 20.
# The second digit is 5 and the second to last digit is 2.
# 5 and 2 form 52.

# 20 + 52 = 72
Examples
closing_in_sum(121) ➞ 13
# 11 + 2

closing_in_sum(1039) ➞ 22
# 19 + 3

closing_in_sum(22225555) ➞ 100
# 25 + 25 + 25 + 25
"""

def closing_in_sum(num):

	if len(str(num)) <= 2:
		return int(num)
	return int(str(num)[0] + str(num)[-1]) + closing_in_sum(int(str(num)[1:-1]))

print(closing_in_sum(15))
print(closing_in_sum(121))
print(closing_in_sum(1039))
print(closing_in_sum(22225555))
print(closing_in_sum(2801980378842185820))
"""
Digits Sum Root
Create a function that takes a number and returns one digit that is the result of summing all the digits of the input number. When the sum of the digits consists of more than one digit, repeat summing until you get one digit.

Examples
root_digit(123) ➞ 6
# 1 + 2 + 3 = 6

root_digit(999888777) ➞ 9

root_digit(1238763636555555555555) ➞ 6
Notes
Recursion is allowed.
"""

def root_digit(n):

	# v2
	return n if n < 10 else root_digit(sum(int(d) for d in str(n)))


	# v1
	# if len(str(n)) > 1:
	# 	return root_digit(eval("+".join(list(str(n)))))
	# elif len(str(n)) == 1:
	# 	return n

print(root_digit(123))
print(root_digit(999888777))
print(root_digit(1111177999888777999888777999888777))
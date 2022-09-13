"""
Bit Masking
Bit masking is a technique used to "hide" certain parts of a number. It's great to use if you want to convey lots of information in a single integer. It takes a number n, converts it to its binary form, and then returns the digit at the index b of that binary number. Note that digit 0 is really the last digit since the least significant (smallest) digit is last. Your job is to create a function bit_mask that takes two arguments - the first being n and the second b - and returns the "masked" form of n.

Examples
bit_mask(37, 2) -> 1
# Binary representation is this:
# 0b100101
#      ^
# We return index 2 from the right, which is 1

bit_mask(56, 1) -> 0
# 0b111000
#        ^

bit_mask(327, 6) -> 1
# 0b101000111
#     ^
Notes
You cannot use the bin function.
For an extra challenge, try only using bit operations!
All numbers 0 ≤ n < 256 will be tested.
There are over 2,000 tests, and they all have to run within 12 seconds (set by Edabit, not me).
If n is too small to have a bth index, return 0.
"""

def bit_mask(n, b):

	return (n >> b) & 1

	# v2
	# bit = []
	# while n >= 2:
	# 	bit.append(n % 2)
	# 	n >>= 1
	# bit.append(n)
	# return bit[b] if len(bit) > b else 0



	# v1
	# if n == 0:
	# 	return 0
	# bit = []
	#
	# while n:
	# 	bit.append(str(n % 2))
	# 	n >>= 1
	#
	# binary = ''.join(bit[::-1])
	# binary = "0b" + binary
	# mask = [v for k, v in enumerate(reversed(binary)) if k == b][0]
	# try:
	# 	if int(mask):
	# 		return int(mask)
	# 	else:
	# 		return int(mask)
	# except ValueError:
	# 	return 0

print(bit_mask(0, 1))
print(bit_mask(37, 2))
print(bit_mask(56, 1))
print(bit_mask(327, 9))



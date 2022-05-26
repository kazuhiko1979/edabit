"""
Minimum Swaps to Alternate a Binary String
Create a function that returns the minimum number of swaps it takes to transform a binary string into a string of alternating 0s and 1s. A swap is switching from a 0 to a 1 or vice versa.

Examples
min_swaps("010010111") ➞ 4

# Two possible conversions:
#   1. "101010101" (4 swaps)
#   2. "010101010" (5 swaps)

min_swaps("10101010") ➞ 0

min_swaps("10010") ➞ 2
"""
def min_swaps(txt):

	# v3
	left_zero, left_one = map(txt[::2].count, ['0', '1'])
	right_zero, right_one = map(txt[1::2].count, ['0', '1'])
	return min((left_zero + right_one), (left_one+ right_zero))



	# v2
	# top_txt_zero = ''.join('1' if i % 2 else '0' for i in range(len(txt)))	# print(top_txt_zero)
	# top_txt_one = ''.join('0' if i % 2 else '1' for i in range(len(txt)))
	# swap_count_top_one = sum(not top_txt_one[i] == txt[i] for i in range(len(txt)))
	# swap_count_top_zero = sum(not top_txt_zero[i] == txt[i] for i in range(len(txt)))
	#
	# return min(swap_count_top_one, swap_count_top_zero)


	# v1
	# left_even = [txt[i] for i in range(0, len(txt)) if i % 2 == 0]
	# left_add = [txt[i] for i in range(0, len(txt)) if i % 2 != 0]

	# if left_even[0] == '0':
	# 	swap_count_left = left_even.count('1') + left_add.count('0')
	# else:
	# 	swap_count_left = left_even.count('0') + left_add.count('1')
	#
	# right_even = [txt[i] for i in range(-1, -len(txt)-1, -1) if i % 2 != 0]
	# right_add = [txt[i] for i in range(-1, -len(txt)-1, -1) if i % 2 == 0]
	#
	# if right_even[0] == '0':
	# 	swap_count_right = right_even.count('1') + right_add.count('0')
	# else:
	# 	swap_count_right = right_even.count('0') + right_add.count('1')
	#
	# return min(swap_count_left, swap_count_right)

print(min_swaps("010010111"))
print(min_swaps("10101010"))
print(min_swaps("101010100"))
print(min_swaps("101010000"))
print(min_swaps("101000000"))
print(min_swaps("10001"))
print(min_swaps("10010"))
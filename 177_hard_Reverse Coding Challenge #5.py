"""
Reverse Coding Challenge #5
This is a reverse coding challenge. Normally you're given explicit directions with how to create a function. Here, you must generate your own function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the sample outputs shown.

Examples
832 ➞ 594

51 ➞ 36

7977 ➞ 198

1 ➞ 0

665 ➞ 99

149 ➞ 0
"""
import itertools

def mystery_func(num):

	# v2
	return num - int(''.join(sorted(str(num))))

	# v1
	# min_num = min([int(''.join(i)) for i in list(itertools.permutations(str(num)))])
	# return num - min_num


print(mystery_func(832))
print(mystery_func(51))
print(mystery_func(7977))
print(mystery_func(1))
print(mystery_func(665))
print(mystery_func(149))



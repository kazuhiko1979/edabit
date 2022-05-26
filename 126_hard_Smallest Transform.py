"""
Smallest Transform
Create a function that returns the smallest number of changes it takes to transform one number into one with identical digits. A step is incrementing or decrementing a digit by one.

Examples
smallest_transform(399) ➞ 6
# 399 transformed to 999 in 6 steps.

smallest_transform(1234) ➞ 4
# 1234 can be transformed to either 2222 or 3333 using 4 steps.

smallest_transform(153) ➞ 4

smallest_transform(33338) ➞ 5

smallest_transform(7777) ➞ 0
Notes
If a number already has identical digits, return 0.
"""

def smallest_transform(num):

	matches_num = [i * len(str(num)) for i in set(list(str(num)))]
	candidates = [str(num) for _ in range(len(matches_num))]

	flat_list = []
	sub_result = []

	for match, candidate in zip(matches_num, candidates):
		for i in range(0, len(match)):
			sub_result.append(abs(int(match[i]) - int(candidate[i])))
			if i == len(match) - 1:
				flat_list.append(sum(sub_result))
				sub_result = []
	return min(flat_list)




print(smallest_transform(399))
print(smallest_transform(153))
print(smallest_transform(1234))
print(smallest_transform(33338))
print(smallest_transform(7777))
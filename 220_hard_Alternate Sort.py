"""
Alternate Sort
Write a function that sorts a given list in an aletrnative fashion. The result should be a list sorted in ascending order (number then letter). Lists will contain equal amounts of integer numbers and single characters.

Examples
alternate_sort(["a", "b", "c", 1, 2, 3]) ➞ [1, "a", 2, "b", 3, "c"]

alternate_sort([-2, "f", "A", 0, 100, "z"]) ➞ [-2, "A", 0, "f", 100, "z"]

alternate_sort(["X", 15, 12, 18, "Y", "Z"]) ➞ [12, "X", 15, "Y", 18, "Z"]
"""
# v3
def alternate_sort(lst):
	numbers = sorted(filter(lambda x: isinstance(x, int), lst))
	letters = sorted(filter(lambda x: isinstance(x, str), lst))
	return [c for i in zip(numbers, letters) for c in i]


# v2
# def alternate_sort(lst):
#
# 	digit, alpha, result = [], [], []
# 	for i in lst:
# 		digit.append(i) if type(i) == int else alpha.append(i)
# 	for i in zip(sorted(digit), sorted(alpha)):
# 		result += i
# 	return result


# v1
# def alternate_sort(lst):
#
# 	digit = []
# 	alpha = []
# 	result = []
#
# 	for i in lst:
# 		if str(i).isalpha():
# 			alpha.append(i)
# 		else:
# 			digit.append(i)
# 	for d, a in zip(sorted(digit), sorted(alpha)):
# 		result.append(d)
# 		result.append(a)
# 	return result

print(alternate_sort(["a", "b", "c", 1, 2, 3]))
print(alternate_sort([-2, "f", "A", 0, 100, "z"]))
print(alternate_sort(["X", 15, 12, 18, "Y", "Z"]))

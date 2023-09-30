"""
The Complete Bracelet
A complete bracelet is a list with at least one subsequence (pattern) repeating at least two times, and completely - the subsequence cannot be cut-off at any point. The subsequence must have length two or greater.

Complete bracelets:

[1, 2, 3, 3, 1, 2, 3, 3]  # Pattern: [1, 2, 3, 3]

[1, 2, 1, 2, 1, 2, 1, 2]  # Pattern: [1, 2] or [1, 2, 1, 2]

[1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]  # Pattern: [1, 1, 6, 1, 1, 7]

[4, 4, 3, 4, 4, 4, 4, 3, 4, 4]  # Pattern: [4, 4, 3, 4, 4]
Incomplete bracelets:

[1, 2, 2, 2, 1, 2, 2, 2, 1]  # Incomplete (chopped off)

[1, 1, 6, 1, 1, 7]  # Incomplete (subsequence repeats only once)
Create a function that returns True if a bracelet is complete, and False otherwise.

Examples
complete_bracelet([1, 2, 2, 1, 2, 2]) ➞ True

complete_bracelet([5, 1, 2, 2]) ➞ False

complete_bracelet([5, 5, 5]) ➞ False
# potential pattern [5, 5] cut-off (patterns >= 2)
Notes
Patterns must be at least two integers in length.
"""
def complete_bracelet(lst):

  a = []
  for x, i in enumerate(lst[:-1]):
    a.append(i)
    b = len(lst) // len(a)
    if b * a == lst and len(a) >= 2:
      return True
  return False

# import numpy as np
#
# def complete_bracelet(array):
#
# 	original_array = np.array(array)
# 	num_slice = 2
# 	if len(original_array) < 4:
# 		return False
#
# 	while num_slice <= len(original_array):
# 		try:
# 			split_arrays = np.split(original_array, num_slice)
# 			result = all(np.array_equal(split_arrays[0], arr) for arr in split_arrays)
# 			if result:
# 				break
# 			elif not result and len(split_arrays[0]) == 2:
# 				return False
# 			else:
# 				num_slice += 1
# 		except:
# 			return False
# 	return result


print(complete_bracelet([1, 2, 2, 1, 2, 2]))
print(complete_bracelet([5, 5, 5]))
print(complete_bracelet([5, 5, 7, 7]))
print(complete_bracelet([5, 5, 7, 7, 5, 5, 7, 7]))
print(complete_bracelet([1, 2, 1, 2, 1, 2]))
print(complete_bracelet([1, 2, 2, 2, 1, 2, 2]))
print(complete_bracelet([1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2]))
print(complete_bracelet([5, 2, 5, 5, 2, 5, 2, 5, 2, 2, 5, 2, 5, 2, 5, 5, 2, 5, 2, 5, 2, 2, 5, 2]))

"""
Reorder Digits
Create a function that reorders the digits of each numerical element in a list based on ascending (asc) or descending (desc) order.

Examples
reorder_digits([515, 341, 98, 44, 211], "asc") ➞ [155, 134, 89, 44, 112]

reorder_digits([515, 341, 98, 44, 211], "desc") ➞ [551, 431, 98, 44, 211]

reorder_digits([63251, 78221], "asc") ➞ [12356, 12278]

reorder_digits([63251, 78221], "desc") ➞ [65321, 87221]

reorder_digits([1, 2, 3, 4], "asc")  ➞ [1, 2, 3, 4]

reorder_digits([1, 2, 3, 4], "desc") ➞ [1, 2, 3, 4]
Notes
Single-digit numbers should be ordered the same regardless of direction.
Numbers in the list should be kept the same order.
"""

def reorder_digits(lst, direction):

	return [int(y) for y in [''.join(sorted(str(x), reverse={"asc":False, "desc":True}[direction])) for x in lst]]


	# if direction == "asc":
	# 	return [int(''.join(sorted(x))) for x in [str(num) for num in lst]]
	# else:
	# 	return [int(''.join(sorted(x, reverse=True))) for x in [str(num) for num in lst]]


print(reorder_digits([515, 341, 98, 44, 211], "asc"))
print(reorder_digits([515, 341, 98, 44, 211], "desc"))
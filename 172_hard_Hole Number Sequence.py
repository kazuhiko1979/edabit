"""
Hole Number Sequence
What do the digits 0, 4, 6, 8, and 9 have in common? Well, they are whole numbers... and they are also hole numbers (not actually a thing until now). Hole numbers are numbers with holes in their shapes (8 is special in that it contains two holes).

14 is a hole number with one hole. 88 is a hole number with four holes.

Your task is to create a function with argument N that returns the sum of the holes for the integers n in the range of range 0 < n <= N.

To illustrate, sum_of_holes(14) returns 7, because there are 7 holes in 4, 6, 8, 9, 10 and 14.

Examples
sum_of_holes(4) ➞ 1

sum_of_holes(6) ➞ 2

sum_of_holes(8) ➞ 4

sum_of_holes(6259) ➞ 12345
Notes
All test cases are positive real integers.
Don't forget that 8 has two holes.
"""



# holes = {0: 1,
# 		 4: 1,
# 		 6: 1,
# 		 8: 2,
# 		 9: 1,
#         10: 1,
#         14: 1
# }
#
# def sum_of_holes(num) -> int:
#
# 	count = 0
#
# 	if num < 4:
# 		return 0
# 	if num == 4:
# 		return 1
#
# 	for i in range(4, num+1):
# 		if i <= 14:
# 			if i in holes:
# 				count += holes[i]
# 				continue
#
# 		if i >= 100:
#
# 			# match10 = holes[10]
# 			# num10 = str(i).count("10")
# 			# sub_count += match10 * num10
# 			# match14 = holes[14]
# 			# num14 = str(i).count("14")
# 			# sub_count += match14 * num14
#
# 			for j in str(i):
# 				if int(j) in holes:
# 					count += holes[int(j)]
# 					continue
# 		else:
# 			for j in str(i):
# 				if int(j) in holes:
# 					count += holes[int(j)]
# 					continue
#
# 	return count


print(sum_of_holes(1))
print(sum_of_holes(4))
print(sum_of_holes(6))
print(sum_of_holes(8))
print(sum_of_holes(9))
print(sum_of_holes(10))
print(sum_of_holes(88))
print(sum_of_holes(10000))
print(sum_of_holes(12345))

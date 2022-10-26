"""
Break Point
A number has a breakpoint if it can be split in a way where the digits on the left side and the digits on the right side sum to the same number.

For instance, the number 35190 can be sliced between the digits 351 and 90, since 3 + 5 + 1 = 9 and 9 + 0 = 9. On the other hand, the number 555 does not have a breakpoint (you must split between digits).

Create a function that returns True if a number has a breakpoint, and False otherwise.

Examples
break_point(159780) ➞ True

break_point(112) ➞ True

break_point(1034) ➞ True

break_point(10) ➞ False

break_point(343) ➞ False
Notes
Read each digit as only one number.
"""

# v3
def break_point(num):

	ns = [int(d) for d in str(num)]
	sums = [0]
	for d in ns:
		sums += [sums[-1]+d]
	return sums[-1] / 2 in sums


# v2
# def break_point(num):
#
# 	l = [int(i) for i in list(str(num))]
#
# 	for i in range(1, len(l)):
# 		if sum(l[:i]) == sum(l[i:]):
# 			return True
# 	return False



# v1
# def break_point(num):
#
# 	if len(set(str(num))) == 1:
# 		return True
#
# 	left_temp = []
# 	right_temp = []
# 	left_sub_total = []
# 	right_sub_total = []
#
# 	for i in str(num):
# 		left_sub_total.append(int(i))
# 		left_temp.append(sum(left_sub_total))
#
# 	for i in reversed(str(num)):
# 		right_sub_total.append(int(i))
# 		right_temp.append(sum(right_sub_total))
#
# 	for left in left_temp:
# 		if left in right_temp:
# 			return left_temp.index(left) + 1 + right_temp.index(left) + 1 == len(str(num))



print(break_point(35190))
print(break_point(159780))
print(break_point(112))
print(break_point(1034))
print(break_point(10))
print(break_point(343))
print(break_point(1119444))
print(break_point(6666))
print(break_point(9777771))



"""
Left Side, Right Side
Create two functions:

Leftside function: Returns count of numbers strictly smaller than n on the left.
Rightside function: Returns count of numbers strictly smaller than n on the right.
Examples
left_side([5, 2, 1, 4, 8, 7]) ➞ [0, 0, 0, 2, 4, 4]

right_side([5, 2, 1, 4, 8, 7]) ➞ [3, 1, 0, 0, 1, 0]

left_side([1, 2, 3, -1]) ➞ [0, 1, 2, 0]

right_side([1, 2, 3, -1]) ➞ [1, 1, 1, 0]
Notes
"Left" and "right" refer to the number at indices less than or greater than n's index, respectively.
"""


# v3
def left_side(lst):
	return [sum(1 for i in lst[:j] if i < lst[j]) for j in range(len(lst))]

def right_side(lst):
	return [sum(1 for i in lst[j+1:] if i < lst[j]) for j in range(len(lst))]



# v2
# def left_side(lst):
#
# 	ans = [0]
# 	for i in range(0, len(lst) - 1):
# 		s = list(filter(lambda x: x < lst[i+1], lst[0:i+1]))
# 		ans.append(len(s))
# 	return ans
#
#
# def right_side(lst):
# 	ans =[]
# 	for i in range(0, len(lst) - 1):
# 		s = list(filter(lambda x: x < lst[i], lst[i+1:]))
# 		ans.append(len(s))
# 	ans.append(0)
# 	return ans




# v1
# def right_side(lst):
#
# 	lst_index = 0
# 	count = 0
# 	temp = []
#
# 	while lst_index < len(lst):
#
# 		for n in lst[lst_index+1:]:
# 			if n < lst[lst_index]:
# 				count += 1
# 				continue
# 			elif n > lst[lst_index]:
# 				pass
#
# 		temp.append(count)
# 		count = 0
# 		lst_index += 1
#
# 	return temp
#
#
# def left_side(lst):
#
# 	lst_index = -1
# 	count = 0
# 	temp = []
#
# 	while lst_index >= -(len(lst)):
# 		for n in lst[::-1]:
# 			if n < lst[lst_index]:
# 				count += 1
# 				continue
# 			elif n > lst[lst_index]:
# 				pass
#
# 		temp.append(count)
# 		count = 0
# 		lst.pop(-1)
#
# 	temp.reverse()
# 	return temp

print(left_side([5, 2, 1, 4, 8, 7]))
print(left_side([3, 8, 2, 5, 4]))
print(left_side([1, 2, 3, 4, 5]))


print(right_side([5, 2, 1, 4, 8, 7]))
print(right_side([1, 2, 3, -1]))
print(right_side([3, 8, 2, 5, 4]))
print(right_side([1, 2, 3, 4, 5]))



"""
Replace With Next Largest Number
Write a function that replaces each integer with the next largest in the list.

Examples
replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]

replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]

replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]
Notes
Replace the maximum with -1.
Elements in the list will be unique.
You don't have to swap the elements.
"""
# v3
def replace_next_largest(input_list):

	asc = sorted(input_list) + [-1]
	return [asc[asc.index(i)+1] for i in input_list]


# v2
# def replace_next_largest(input_list):
#
# 	temp = sorted(input_list)
# 	result = []
# 	for i in range(len(input_list)):
# 		if input_list[i] == max(input_list):
# 			result.append(-1)
# 		else:
# 			a = temp.index(input_list[i])
# 			result.append(temp[a+1])
# 	return result


# v1
# import copy
#
# def replace_next_largest(input_list):
#
# 	result = []
# 	index = 0
# 	flag = True
#
# 	while flag:
#
# 		temp_list = copy.copy(input_list)
# 		input_value = temp_list[index]
# 		temp_list.pop(index)
# 		temp_list = [i for i in temp_list if i > input_value]
#
# 		try:
# 			close_value = min(temp_list)
# 		except:
# 			close_value = -1
#
# 		result.append(close_value)
#
# 		if len(result) == len(input_list):
# 			flag = False
# 		else:
# 			index += 1
#
# 	return result

print(replace_next_largest([5, 7, 3, 2, 8]))
print(replace_next_largest([2, 3, 4, 5]))
print(replace_next_largest([4, 1, 6, -7, -8, 2]))
print(replace_next_largest([1, 0, -1, 8, -72]))

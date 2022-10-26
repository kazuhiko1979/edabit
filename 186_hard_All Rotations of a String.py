"""
All Rotations of a String
Create a left rotation and a right rotation function that returns all the left rotations and right rotations of a string.

Examples
left_rotations("abc") ➞ ["abc", "bca", "cab"]

right_rotations("abc") ➞ ["abc", "cab", "bca"]

left_rotations("abcdef")
➞ ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"]

right_rotations("abcdef")
➞ ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"]
"""
# v3
def left_rotations(txt):
	return [txt[i:]+txt[:i] for i in range(len(txt))]

def right_rotations(txt):
	return [txt[-i:]+txt[:-i] for i in range(len(txt))]


# v2
# def rotations(txt, side=""):
#
# 	result = []
# 	i = 0
# 	while i < len(txt):
# 		if side == "l":
# 			new_txt = txt[i:] + txt[:i]
# 		if side == "r":
# 			new_txt = txt[-i:] + txt[:-i]
# 		result.append(new_txt)
# 		i += 1
# 	return result
#
# def left_rotations(txt):
# 	return rotations(txt, "l")
#
# def right_rotations(txt):
# 	return rotations(txt, "r")


# v1
# import copy
#
# def left_rotations(txt, temp=[]):
#
# 	# initializing right rot
# 	r_rot = 1
#
# 	# initializing left rot
# 	l_rot = 0
#
# 	res = (txt * 3)[len(txt) + r_rot - l_rot:2 * len(txt) + r_rot - l_rot]
#
#
# 	if res not in temp:
# 		temp.append(str(res))
# 		return left_rotations(res)
# 	else:
# 		original_txt = temp[-1]
# 		temp.pop()
# 		temp.insert(0, original_txt)
# 		result = copy.deepcopy(temp)
# 		temp.clear()
# 		return result
#
# def right_rotations(txt, temp=[]):
#
# 	r_rot = 0
# 	l_rot = 1
#
# 	res = (txt * 3)[len(txt) + r_rot - l_rot:2 * len(txt) + r_rot - l_rot]
#
# 	if res not in temp:
# 		temp.append(str(res))
# 		return right_rotations(res)
# 	else:
# 		original_txt = temp[-1]
# 		temp.pop()
# 		temp.insert(0, original_txt)
# 		result = copy.deepcopy(temp)
# 		temp.clear()
# 		return result


# v2
# def rotations_master(txt, r_rot, l_rot, temp=[]):
#
# 	res = (txt * 3)[len(txt) + r_rot - l_rot:2 * len(txt) + r_rot - l_rot]
#
# 	if res not in temp:
# 		temp.append(str(res))
# 		return rotations_master(res, r_rot, l_rot, temp)
# 	else:
# 		original_txt = temp[-1]
# 		temp.pop()
# 		temp.insert(0, original_txt)
# 		result = copy.deepcopy(temp)
# 		temp.clear()
# 		return result
#
#
# def left_rotations(txt):
# 	return rotations_master(txt, 1, 0, temp=[])
#
#
# def right_rotations(txt):
# 	return rotations_master(txt, 0, 1, temp=[])


print(left_rotations("abc"))
print(left_rotations("abcdef"))
print(left_rotations("himalaya"))
print(left_rotations("aab"))
print()
print(right_rotations("abc"))
print(right_rotations("abcdef"))
print(right_rotations("himalaya"))
print(right_rotations("aab"))

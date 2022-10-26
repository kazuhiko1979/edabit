"""
Making a Box 2.0!
This is based on Helen Yu's Making a Box challenge. This challenge is the same execpt that instead of a list of strings, your function should output a matrix of characters.

Examples
char_box(1) ➞ [
  ["#"]
]

char_box(4) ➞ [
  ["#", "#", "#", "#"],
  ["#", " ", " ", "#"],
  ["#", " ", " ", "#"],
  ["#", "#", "#", "#"]
]

char_box(2) ➞ [
  ["#", "#"],
  ["#", "#"]
]
Notes
As an added bonus, try making char_box(0) output [[]] and make any strings, non-integers, and negative numbers output -1.
"""
# v2
def char_box(size):

	if size == 0:
		return [[]]
	if size == 1:
		return [["#"]]
	elif not isinstance(size, int) or size < 0:
		return -1

	lst = [["#"] * size]
	for i in range(size-2):
		lst.append(["#"] + ([' ']*(size-2)) + ["#"])
	return lst + [['#'] * size]





# v1
# def char_box(num):
#
# 	box = []
#
# 	if num == 0:
# 		box.append([])
# 		return box
# 	elif not str(num).isdigit():
# 		return -1
#
# 	for i in range(num):
# 		if i == 0:
# 			box.append(list(str("#" * num)))
# 			continue
# 		if i == num - 1:
# 			box.append(list(str("#" * num)))
# 			break
# 		else:
# 			temp = []
# 		for j in range(num):
# 				if j == 0:
# 					temp.append("#")
# 					continue
# 				if j == num - 1:
# 					temp.append("#")
# 					break
# 				else:
# 					temp.append(" ")
# 			box.append(temp)
#
# 	return box

print(char_box(1))
print(char_box(2))
print(char_box(4))
print(char_box(3))
print(char_box(10))
print(char_box(0))
print(char_box("Hi"))
print(char_box(.23))
print(char_box(-4))

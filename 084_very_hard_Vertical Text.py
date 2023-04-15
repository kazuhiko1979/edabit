"""
Vertical Text
Create a function that converts a string into a matrix of characters that can be read vertically. Add spaces when characters are missing.

Examples
vertical_txt("Holy bananas") ➞ [
  ["H", "b"],
  ["o", "a"],
  ["l", "n"],
  ["y", "a"],
  [" ", "n"],
  [" ", "a"],
  [" ", "s"]
]

vertical_txt("Hello fellas") ➞ [
  ["H", "f"],
  ["e", "e"],
  ["l", "l"],
  ["l", "l"],
  ["o", "a"],
  [" ", "s"]
]
"""
# v3
from itertools import zip_longest

def vertical_txt(txt):

	return [list(i) for i in zip_longest(*txt.split(), fillvalue=' ')]


# v2
# def vertical_txt(txt):
#
# 	txt = txt.split()
# 	rows = max(len(w) for w in txt)
# 	cols = len(txt)
#
# 	result = []
# 	for r in range(rows):
# 		result.append([txt[c][r] if len(txt[c]) > r else ' ' for c in range(cols)])
# 	return result

# v1
# import numpy as np
#
#
# def vertical_txt(txt):
#
# 	txt = txt.split()
# 	temp = np.empty([len(max(txt, key=len)), int(len(txt))], dtype=str)
#
# 	count = 0
# 	for word in txt:
# 		length_word = len(word)
# 		for idx, char in enumerate(word):
# 			if idx >= 0:
# 				temp[idx][count] = char
# 				length_word -= 1
# 				if length_word == 0:
# 					count += 1
#
# 	return [[val if val != '' else ' ' for val in lst] for lst in temp]

print(vertical_txt("Holy bananas"))
print(vertical_txt("Hello fellas"))
print(vertical_txt("I hope you have a great day"))
print(vertical_txt("0 11 222 3333 44444 6666666 77777777 888888888 9999999999"))


"""
Simple Symbols
Create a function that takes a string and determine if it's a valid sequence by either returning True or False. The string will be composed of + and = symbols with several characters between them (e.g. "++d+===+c++==a") and for the string to be True, each letter must be surrounded by a + symbol. So the string to the left would be False.

Examples
simple_symbols("f++d+") ➞ False

simple_symbols("+d+=3=+s+") ➞ True

simple_symbols("==+p+++++++++====8+z++++") ➞ True
Notes
The given string will not be empty and will have at least one letter.
"""
import re

def simple_symbols(txt):

	# v3
	txt = re.split('\w', txt)
	return all(['+' in i for i in txt])


	# v2
	# for i, x in enumerate(txt):
	# 	if x.isalpha() and (i==0 or txt[i-1]!='+' or txt[i+1]!='+' or i==len(txt)-1):
	# 		return False
	# return True


	# v1.5
	# for i, x in enumerate(txt):
	# 	if x.isalpha():
	# 		if i - 1 < 0:
	# 			return False
	# 		if txt[i-1] != '+':
	# 			return
	# 		if i + 1 >= len(txt):
	# 			return False
	# 		if txt[i+1] != '+':
	# 			return False
	# return True



	# v1 ※txt[i-1]最後尾を指してしまう！
	# bool = []
	#
	# if txt[0].isalpha():
	# 	return False
	# else:
	# 	for i in range(0, len(txt)):
	# 		if txt[i].isalpha():
	# 			if txt[i-1]:
	# 				if txt[i-1] == "+":
	# 					if txt[i+1]:
	# 						if txt[i+1] == "+":
	# 							bool.append(True)
	# 						else:
	# 							bool.append(False)
	#
	# return all(bool)

print(simple_symbols("f++d+"))
print(simple_symbols("+d+=3=+s+"))
print(simple_symbols("==+p+++++++++====8+z++++"))
print(simple_symbols("======2+++4+u===+i+"))
print(simple_symbols("+u+====3+mmmmm===m++"))
print(simple_symbols("==+p+++++++++====8+z++++"))
print(simple_symbols("+d+=3=+s+"))
print(simple_symbols("f++d+"))





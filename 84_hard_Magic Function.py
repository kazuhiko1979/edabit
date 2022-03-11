"""
Magic Function
Create a class with a few functions like these examples.

magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of the new list is 0, return -1.
Examples
magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

magic.str_length("hello world") ➞ 11

magic.trim("      python is awesome      ") ➞ "python is awesome"

magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]
"""

class Magic:


	# def __init__(self):
	# 	pass
	#
	# def replace(self, string, old, new):
	# 	return string.replace(old, new)
	#
	# def str_length(self, string):
	# 	return len(string)
	#
	# def trim(self, string):
	# 	return string.strip()
	#
	# def list_slice(self, lst, tpl):
	# 	return [i for i in lst if i in tpl]

magic = Magic()

print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world"))
print(magic.trim("  python is awesome  "))
print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))



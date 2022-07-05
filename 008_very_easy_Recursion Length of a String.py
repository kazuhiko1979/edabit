"""
Recursion: Length of a String
Write a function that returns the length of a string. Make your function recursive.

Examples
length("apple") ➞ 5

length("make") ➞ 4

length("a") ➞ 1

length("") ➞ 0
"""

def length(s):
	if not s:
		return 0
	return length(s[:-1]) + 1

# def length(txt, count=0):
#
# 	# if not txt:
# 	# 	return count
# 	# return length(txt[1:], count+1)

print(length("apple"))
print(length("make"))
print(length("a"))
print(length(""))
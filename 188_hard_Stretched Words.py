"""
Stretched Words
Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.

Examples
unstretch("ppoeemm") ➞ "poem"

unstretch("wiiiinnnnd") ➞ "wind"

unstretch("ttiiitllleeee") ➞ "title"

unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"
"""
from itertools import groupby

# v3
def unstretch(txt):
	return ''.join(k for k, g in groupby(txt))

# v2
# def unstretch(txt):
#
# 	c = txt[0]
# 	for i in range(1, len(txt)):
# 		if txt[i] != c[-1]:
# 			c += txt[i]
# 	return c


# v1
# def unstretch(txt):
#
# 	result = ""
#
# 	for i in range(0, len(txt)+1):
# 		temp = txt[i]
# 		if len(txt) - 1 > i:
# 			if temp == txt[i+1]:
# 				continue
# 			else:
# 				result += temp
# 		else:
# 			result += txt[-1]
# 			break
# 	return result

print(unstretch('rrrrepooooorrttt'))
print(unstretch('pppaaaaattteeeennnntt'))
print(unstretch('mmmeeemoooryy'))
print(unstretch('vvvvviiiiisssuuaaalll'))
print(unstretch('eeeennnnsuuurrre'))


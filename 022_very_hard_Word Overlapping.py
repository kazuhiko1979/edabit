"""
Word Overlapping
Given two words, overlap them in such a way, morphing the last few letters of the first word with the first few letters of the second word. Return the shortest overlapped word possible.

Examples
overlap("sweden", "denmark") ➞ "swedenmark"

overlap("edabit", "iterate") ➞ "edabiterate"

overlap("honey", "milk") ➞ "honeymilk"

overlap("dodge", "dodge") ➞ "dodge"
Notes
All words will be given in lowercase.
If no overlap is possible, return both words one after the other (example #3).
"""
import re

def overlap(s1, s2):

	# v3

	# 置換後の文字列 = re.sub(正規表現, 置換する文字列, 置換される文字列[, 置換回数])
	return re.sub(r'(\w*) \1', r'\1', '{} {}'.format(s1, s2))


	# v2
	# for i in range(len(s1)):
	# 	if s2.startswith(s1[i:]):
	# 		return s1[:i] + s2
	# return s1 + s2



	# v1
	# temp = ""
	# common = ""
	#
	# if s1 == s2:
	# 	return s1
	# for i in range(0, len(s1)):
	# 	if s1[i] == s2[0]:
	# 		temp += s1[i:]
	#
	# if temp == s2[:len(temp)] and len(temp) == len(s2[:len(temp)]):
	# 	return s1 + s2[len(temp):]
	# if temp != s2[:len(temp)] and len(temp) == len(s2[:len(temp)]):
	# 	for i, j in zip(temp, s2[:len(temp)]):
	# 		if i == j:
	# 			common += i
	# 	return s1 + s2[len(common):]
	#
	# else:
	# 	return s1 + s2



print(overlap("sweden", "denmark"))
print(overlap("edabit", "iterate"))
print(overlap("honey", "milk"))
print(overlap("dodge", "dodge"))
print(overlap("colossal", "alligator"))
print(overlap("leave", "eavesdrop"))
print(overlap("joshua", "osha"))
print(overlap("diction", "dictionary"))
print(overlap("massive", "mass"))
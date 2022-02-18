"""
Ransom Letter
Write a function that returns True if you can use the letters of the first string to create the second string. Letters are case sensitive.

Examples
can_build("aPPleAL", "PAL") ➞ True

can_build("aPPleAL", "apple") ➞ False

can_build("a", "") ➞ True

can_build("aa", "aaa") ➞ False
Notes
Letters in the first string can be used only once.
"""
from collections import Counter

def can_build(s1, s2):

	return not Counter(s2) - Counter(s1)


	# return all(s2.count(i) <= s1.count(i) for i in s2)


	# lengthOf_s2 = len(s2)
	#
	# for i in s1:
	# 	if i in s2:
	# 		lengthOf_s2 -= 1
	# return lengthOf_s2 <= 0

print(can_build("aPPleAL", "PAL"))
print(can_build("aPPleAL", "apple"))
print(can_build("a", ""))
print(can_build("aa", "aaa"))




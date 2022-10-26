"""
Split String by Identical Characters
Create a function that splits a string into an array of identical clusters.

Examples
split_groups("555") ➞ ["555"]

split_groups("5556667788") ➞ ["555", "666", "77", "88"]

split_groups("aaabbbaabbab") ➞ ["aaa", "bbb", "aa", "bb", "a", "b"]

split_groups("abbbcc88999&&!!!_") ➞ ["a", "bbb", "cc", "88", "999", "&&", "!!!", "_"]
Notes
Each cluster should only have one unique character.
The resulting array should be in the same order as the input string.
Should work with letters, numbers and other characters.
"""
# V3
from itertools import groupby

def split_groups(txt):

	return [''.join(list(x)) for i, x in groupby(txt)]


# V2
# def split_groups(txt):
# 	groups, x = [], 0
# 	for n in txt:
# 		if len(groups) == 0 or n not in groups[len(groups) - 1]:
# 			groups.append(n)
# 		else:
# 			groups[len(groups)-1] += n
#
# 	return groups


# v1
# def split_groups(txt):
#
# 	total = []
# 	sub = ""
#
# 	if len(set(txt)) == 1:
# 		return [txt]
#
# 	for i, j in zip(txt, txt[1:]):
# 		if i == j:
# 			sub += j
# 		else:
# 			sub += i
# 			total.append(sub)
# 			sub = ""
#
# 	if i and i == j:
# 		total.append(i+j)
# 	else:
# 		total.append(j)
# 	return total

print(split_groups("555"))
print(split_groups("5556667788"))
print(split_groups("aaabbbaabbab"))
print(split_groups("abbbcc88999&&!!!_"))
print(split_groups('AABBCC'))


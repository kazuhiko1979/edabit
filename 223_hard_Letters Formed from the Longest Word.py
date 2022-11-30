"""
Letters Formed from the Longest Word
Write a function that returns True if all the strings in a list can be formed by using only the characters from the longest string.

Examples
can_form(["mast", "manifest", "met", "fan"]) ➞ True

can_form(["may", "master", "same", "reams"]) ➞ False

can_form(["may", "same", "reams", "mastery"]) ➞ True
Notes
There will only be one unique longest string.
"""
# v3
def can_form(lst):
	longest = max(lst, key=len)
	return all(longest.count(i) >=  word.count(i) for word in lst for i in set(word))


# v2
# def can_form(lst):
#
# 	for x in lst:
# 		for c in x:
# 			if max(lst, key=len).count(c) < x.count(c):
# 				return False
# 	return True




# v1
# def can_form(lst):
#
# 	str_len = [len(i) for i in lst]
# 	max_string = lst[str_len.index(max(str_len))]
#
# 	for i in lst:
# 		if i != max_string:
# 			for j in i:
# 				if j in max_string:
# 					max_string = max_string.replace(j, '')
# 				else:
# 					return False
# 			return True

print(can_form(["mast", "manifest", "met", "fan"]))
print(can_form(["may", "master", "same", "reams"]))
print(can_form(["may", "same", "reams", "mastery"]))
print(can_form(["kerfuffle", "fluke", "fluff", "ruffle", ]))
print(can_form(["monument", "momento", "moment", "tome"]))
print(can_form(["shape", "shapers", "raps", "saps"]))
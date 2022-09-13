"""
Recursion: Flatten the Curves
The nesting of lists can be viewed indirectly as curves and barriers of the real data embedded in lists, thus, defeats the very purpose of directly accessing them thru indexes and slices. In this challenge, a function is required to flatten those curves (i.e. level, iron, compress, raze, topple) and expose those data as a single list and not as a list of lists.

Examples
flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])
➞ ["direction", 372, "one", "Era", "Sruth", 3337, "First"]

flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]])
➞ [4666, 5394, 466, "Saskia", "DXTD", "Lexi"]

flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]])
➞ [696, "friend", "power", "Marcus", "philus"]

flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])
➞ ["deep", "ocean", "Marge", "rase", 876]
Notes
There are no empty lists to handle.
You're expected to solve this challenge using a recursive approach.
"""
import copy

def flatten(l):

	if not l:
		return []
	if type(l[0]) == list:
		return flatten(l[0] + flatten(l[1:]))
	return l[:1] + flatten(l[1:])

	# if type(l) != list:
	# 	return [l]
	# return sum((flatten(e) for e in l), [])


	# not working
	# for i in l:
	# 	if type(i) == list:
	# 		flatten(i)
	# 	else:
	# 		output.append(i)




print(flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]]))
print(flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]]))
print(flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]]))
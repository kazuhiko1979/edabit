"""
Longest Common Ending
Write a function that returns the longest common ending between two strings.

Examples
longest_common_ending("multiplication", "ration") ➞ "ation"

longest_common_ending("potent", "tent") ➞ "tent"

longest_common_ending("skyscraper", "carnivore") ➞ ""
Notes
Return an empty string if there exists no common ending.
"""
# v3
def longest_common_ending(txt1, txt2):
	while not txt1.endswith(txt2):
		txt2 = txt2[1:]
	return txt2


# v2
# def longest_common_ending(txt1, txt2):
# 	for i in range(min(len(txt1), len(txt2)), 1, -1):
# 		if txt1[-i:] == txt2[-i:]:
# 			return txt1[-i:]
# 	return ''


# v1
# def longest_common_ending(txt1, txt2):
#
# 	result = ""
# 	flag = True
#
# 	while flag:
# 		if not txt1 or not txt2:
# 			return result[::-1]
#
# 		if txt1[-1] == txt2[-1]:
# 			result += txt1[-1]
# 			txt1 = txt1[:-1]
# 			txt2 = txt2[:-1]
# 		else:
# 			flag = False
# 	return result[::-1]

print(longest_common_ending("pitiful", "beautiful"))
# print(longest_common_ending("truck", "trick"))
# print(longest_common_ending("vote", "asymptote"))
# print(longest_common_ending("multiplication", "ration"))
# print(longest_common_ending("potent", "tent"))
# print(longest_common_ending("skyscraper", "carnivore"))


"""
Scrambled Letters
Write a function that receives a list of words and a mask. Return a list of words, sorted alphabetically, that match the given mask.

Examples
scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]

scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]
Notes
The length of a mask will never exceed the length of the longest word in the word list.
"""

recede = ["cee", "dee", "eer", "erd", "ere", "red", "ree", "cede",
			  "cere", "cree", "deer", "dere", "dree", "rede", "reed", "ceder", "cedre", "cered", "creed", "decree",
			  "recede"]

from re import match

# def scrambled(words, mask):

	# v3
	# pattern = mask.replace("*", r"\w") + "$"
	# return [word for word in words if match(pattern, word)]

# v2
def check(word, mask):

	if len(word) != len(mask):
		return False

	for i in range(len(word)):
		if mask[i] != '*' and mask[i] != word[i]:
			return False
	return True


def scrambled(words, mask):

	return sorted([word for word in words if check(word, mask)])


# v1
	# alpha_index = [mask.index(i) for i in mask if i.isalpha()]
	# common_len_words = [i for i in words if len(i) == len(mask)]
	#
	# total = []
	# count = 0
	#
	# if len(set(mask)) == 1:
	# 	return common_len_words
	#
	# for i in common_len_words:
	# 	for j in alpha_index:
	# 		if i[j] == mask[j]:
	# 			count += 1
	# 			if count == len(alpha_index):
	# 				total.append(i)
	# 				count = 0
	# 		else:
	# 			count = 0
	# return total


print(scrambled(recede, "*re**"))
print(scrambled(recede, "***"))
print(scrambled(recede, "******"))
print(scrambled(recede, "c*d**"))
print(scrambled(recede, "d***"))
print(scrambled(recede, "r***"))

"""
Longest Abecedarian Word
An abecedarian word is a word where all of its letters are arranged in alphabetical order. Examples of these words include:

Empty
Forty
Almost
Given a list of words, create a function which returns the longest abecedarian word. If no word in a list matches the criterea, return an empty string.

Examples
longest_abecedarian(["ace", "spades", "hearts", "clubs"]) ➞ "ace"

longest_abecedarian(["forty", "choppy", "ghost"]) ➞ "choppy"

longest_abecedarian(["one", "two", "three"]) ➞ ""
Notes
All words will be given in lowercase.
If two abecedarian words have the same length, return the word which appeared first in the list.
"""

# v3
def longest_abecedarian(lst):

	lst = [w for w in lst if list(w) == sorted(w)]
	return max(lst, key=len) if lst else ''


# v2
# def longest_abecedarian(lst):
#
# 	for i in sorted(lst, key=len, reverse=True):
# 		if i == ''.join(sorted(i)):
# 			return i
# 	return ''

# v1
# def longest_abecedarian(lst):
#
# 	inc_list = [[ord(char) for char in word] for word in lst]
#
# 	temp, result = [], []
#
# 	for num in inc_list:
# 		for i, j in zip(num, num[1:]):
# 			if i <= j:
# 				temp.append(True)
# 			else:
# 				temp.append(False)
# 		result.append(all(temp))
# 		temp = []
#
# 	if not any(result):
# 		return ""
#
# 	if all(result):
# 		return max(enumerate(lst), key=lambda x: len(x[1]))[1]
#
# 	else:
# 		for i, j in zip(lst, result):
# 			if j:
# 				return i



print(longest_abecedarian(["ace", "spades", "hearts", "clubs"]))
print(longest_abecedarian(["forty", "choppy", "ghost"]))
print(longest_abecedarian(["one", "two", "three"]))
print(longest_abecedarian(["almost", "accept", "access"]))
print(longest_abecedarian(["aa", "bbb", "cccc"]))

"""
Alphabetically Sorted
A word is alphabetically sorted if all of the letters in it are in consecutive alphabetical order. Some examples of alphabetically sorted words: abhors (a is before b, b is before h, h is before o, etc.), ghost, accent, hoop.

Create a function that takes in a sentence as input and returns True if there is at least one alphabetically sorted word inside that has a minimum length of 3.

Examples
is_alphabetically_sorted("Paula has a French accent.") ➞ True
# "accent" is alphabetically sorted.

is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
# "biopsy" is alphabetically sorted.

is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
# Although "by" is alphabetically sorted, it is only 2 letters long.
Notes
Do not count words with 2 or fewer characters.
Ignore punctuation (periods, commas, etc).
"""
import re

def is_alphabetically_sorted(sentence):

	# v3
	# match = re.findall("\w{3,}", sentence)
	# return any(["".join(sorted(i.lower())) == i.lower() for i in match])

	# v2
	s = ''.join(i for i in sentence.lower() if i.isalpha() or i == ' ')
	for word in s.split():
		if ''.join(sorted(word)) == word and len(word) > 2:
			return True
	return False



	# v1
	# temp = [' '.join(str(ord(c) - 96) for c in word.lower() if c.isalpha()) for word in sentence.split()]
	#
	# for i in temp:
	# 	if len(list(map(int, i.split()))) > 2 and list(map(int, i.split())) == sorted(list(map(int, i.split()))):
	# 		return True
	# else:
	# 	return False

print(is_alphabetically_sorted("Paula has a French accent."))
print(is_alphabetically_sorted("The biopsy returned negative results."))
print(is_alphabetically_sorted("She sells sea shells by the sea shore."))

print(is_alphabetically_sorted("Beth dislikes eating starfruit but enjoys cherries."))
print(is_alphabetically_sorted("Mara took a photograph."))
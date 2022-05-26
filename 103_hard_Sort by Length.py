"""
Sort by Length
Create a function that takes a string and returns a string ordered by the length of the words. From shortest to longest word. If there are words with the same amount of letters, order them alphabetically.

Examples
sort_by_length("Hello my friend") ➞ "my Hello friend"

sort_by_length("Have a wonderful day") ➞ "a day Have wonderful"

sort_by_length("My son loves pineapples") ➞ "My son loves pineapples"
Notes
Punctuation (periods, commas, etc) belongs to the word in front of it.
"""
import copy

def sort_by_length(txt):

	# v2
	# words = txt.split()
	# words.sort(key = lambda x: (len(x), x.lower()))
	# return ' '.join(words)

	# v1
	output = []
	words = txt.split()
	for i in words:
		output.append([len(i), i.lower(), i])
	output.sort()
	stripped = [i[2] for i in output]
	return ' '.join(stripped)


	# v0 アルファベット順不足
	# temp = copy.copy(txt).split()
	# len_txt = sorted([len(i) for i in txt.split()])
	#
	# for x in txt.split():
	# 	if len(x) in len_txt:
	# 		len_txt[len_txt.index(len(temp[temp.index(x)]))] = temp[temp.index(x)]
	# return ' '.join(len_txt)

print(sort_by_length("Hello my friend"))
print(sort_by_length("Three can keep a secret, if two of them are dead"))
print(sort_by_length("Have a wonderful day"))
print(sort_by_length("My son loves pineapples"))


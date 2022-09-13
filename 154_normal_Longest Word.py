"""
Longest Word
Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word. Characters such as apostrophe, comma, period (and the like) count as part of the word (e.g. O'Connor is 8 characters long).

Examples
longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

longest_word("A thing of beauty is a joy forever.") ➞ "forever."

longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"
"""

def longest_word(txt, res=None):

	# v2
	# if res is None:
	# 	txt = (txt.lower().replace(',', '').replace('.', '')
	# 		   .replace('\'s', '').replace('\"', '').split())
	#
	# 	res, txt = txt[0], txt[1:]
	#
	# return (longest_word(txt[1:], txt[0]) if len(txt[0]) > len(res)
	# 		else longest_word(txt[1:], res)) if txt else res

	# V1
	max_length = max([len(i) for i in txt.split()])

	for j in txt.split():
		if len(j) == max_length:
			return j
	# temp_max = txt.split()[0]

	# if len(txt.split()[0]) > len(txt.split()[1]):
	# 	temp_max = txt.split()[0]
	# 	return longest_word(' '.join(txt.split()[1:]), temp_max)
	# else:
	# 	temp_max = txt.split()[1]
	# 	return longest_word(' '.join(txt.split()[1:]), temp_max)


			# longest_word(' '.join(txt.split()[1:])):
	# 	print(True)
	# else:
	# 	print(True)
	# if not txt:
	# 	return 0
	# else:
	# return longest_word(' '.join(txt.split()[1:]))

# def longest_word_helper()

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))

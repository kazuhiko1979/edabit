"""
Elastic Words
In this challenge, you must think about words as elastics. What happens when do you tend an elastic applying a constant traction force at both ends? Every part (or letter, in this case) of the elastic will expand, with the minimum expansion at the ends, and the maximum expansion in the center.

If the word has an odd length, the effective central character of the word will be the pivot that splits the word into two halves.

"ABC" -> Left = "A" | Center = "B" | Right = "C"
If the word has an even length, you will consider two parts of equal length, with the last character of the left half and the first character of the right half being the center.

"ABCD" -> Left = "AB" | Right = "CD"
You will represent the expansion of a letter repeating it as many times as its numeric position (so counting the indexes from/to 1, and not from 0 as usual) in its half, with a crescent order in the left half and a decrescent order in the right half.

Word = "ANNA"

Left = "AN"
Right = "NA"

Left = "A" * 1 + "N" * 2 = "ANN"
Right = "N" * 2 + "A" * 1 = "NNA"

Word = Left + Right = "ANNNNA"
If the word has an odd length, the pivot (the central character) will be the peak (as to say, the highest value) that delimits the two halves of the word.

Word = "KAYAK"

Left = "K" * 1 + "A" * 2 = "KAA"
Pivot = "Y" * 3 = "YYY"
Right = "A" * 2 + "K" * 1 = "AAK"

Word = Left + Pivot + Right = "KAAYYYAAK"
Given a word, implement a function that returns the elasticized version of the word as a string.

Examples
elasticize("ANNA") ➞ "ANNNNA"

elasticize("KAYAK") ➞ "KAAYYYAAK"

elasticize("X") ➞ "X"
Notes
For words with less than three characters, the function must return the same word (no traction appliable).
Remember, into the left part characters are counted from 1 to the end, and, in reverse order until 1 is reached, into the right.
"""
import math

def elasticize(word):

	return [c*(i+1 if i < len(word) / 2 else len(word)-i) for i, c in enumerate(word)]

	# s = ""
	#
	# for i in range(0, len(word)):
	# 	if i >= len(word) / 2:
	# 		s += (len(word) - i) * word[i]
	# 	else:
	# 		s += (i + 1) * word[i]
	# return s


	# def help_elasticize(word, isdivided=True):
	#
	# 	length = len(word)
	# 	index = int(length / 2)
	#
	# 	left = [word[j] for j in range(0, index)]
	# 	right = [word[j] for j in range(index, len(word))]
	# 	index_left = [i for i in range(1, index + 1)]
	# 	index_right = list(reversed([i for i in range(1, index + 1)]))
	#
	# 	res_left = dict(zip(left, index_left))
	# 	res_right = dict(zip(right, index_right))
	#
		# 注意辞書型は正確では並び替えはしない（厳密的には）

	# 	left_word = ''.join([k * v for k, v in res_left.items()])
	# 	right_word = ''.join([k * v for k, v in res_right.items()])
	#
	# 	if isdivided:
	# 		return left_word + right_word
	# 	else:
	# 		return left_word + pivot_word + right_word
	#
	#
	# if len(word) % 2 == 0:
	#
	# 	return help_elasticize(word, True)
	#
	# elif len(word) % 2 == 1:
	#
	# 	pivot = math.ceil(len(word) / 2) - 1
	# 	pivot_word = word[pivot]
	# 	pivot_word = pivot_word * pivot + pivot_word
	# 	word = word[:pivot] + word[pivot+1:]
	#
	# 	return help_elasticize(word, False)


print(elasticize("ANNA"))
# print(elasticize("KAYAK"))
# print(elasticize("X"))
# print(elasticize("AA"))
# print(elasticize("ABC"))
# print(elasticize("BOB"))
# print(elasticize("OTTO"))
# print(elasticize("LEVEL"))
# print(elasticize("IJKCBA"))
# print(elasticize("REDDER"))
# print(elasticize("ROTATOR"))







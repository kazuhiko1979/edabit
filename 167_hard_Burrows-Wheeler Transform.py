"""
Burrows-Wheeler Transform
Burrows-Wheeler transform (BWT) is an algorithm which is used in data compression. Given a string text, BWT of text is a modified version of the string with same length as text. It can then be used to efficiently find substrings of text (which won't be covered here). We will just find the BWT of text.

Build Burrows-Wheeler-Matrix (BWM) containing all rotations of text.
Sort BWM lexicographically ($ < a < b < ... < z).
BWT is the last coloumn of BWM and gets returned.
# Example with text = "banana$"

# BWM (all rotations of text):
banana$
anana$b
nana$ba
ana$ban
na$bana
a$banan
$banana

# BWM sorted lexicographically:
$banana
a$banan
ana$ban
anana$b
banana$
na$bana
nana$ba

# BWT (last coloumn of BWM):
annb$aa
Examples
bw_transform("banana$") ➞ "annb$aa"

bw_transform("mississippi$") ➞ "ipssm$pissii"

bw_transform("acccgtttgtttcaatagatccatcaa$") ➞ "aacc$tacgttctaccatcaatatttgg"
Notes
Consider $ as the terminator character at the end of every input text.
"""
def bw_transform(text):

	# v3
	return ''.join(i[-1] for i in sorted(text[i:]+text[:i] for i in range(len(text))))

	# v2
	# bwm = []
	# for i in range(len(text)):
	# 	text = text[1:] + text[:1]
	# 	bwm.append(text)
	# bwm = sorted(bwm)
	# return ''.join(bwm[i][-1] for i in range(len(bwm)))


# def bw_transform(word):
#
# 	words = list(word)
# 	temp = []
#
# 	for i in range(len(words)):
# 		word = word[-1] + word[:-1]
# 		new = ''.join(word)
# 		word = new
# 		temp.append(new)
# 		i += 1
#
# 	sorted_temp = sorted(temp)
# 	sorted_last_word = ''.join([j[-1] for j in sorted_temp])
# 	sorted_last_words = list(sorted_last_word)
# 	temp.clear()
#
# 	for i in range(len(sorted_last_words)):
# 		sorted_last_word = sorted_last_word[-1] + sorted_last_word[:-1]
# 		new = ''.join(sorted_last_word)
# 		sorted_last_word = new
# 		temp.append(new)
# 		i += 1
#
# 	return temp[-1]





print(bw_transform("banana$"))
print(bw_transform("mississippi$"))
print(bw_transform("acccgtttgtttcaatagatccatcaa$"))
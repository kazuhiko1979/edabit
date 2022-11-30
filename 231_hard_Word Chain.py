"""
Word Chain
A word-chain is an array of words, where the next word is formed by changing exactly one letter from the previous word. We do not add or subtract letters from words, only change them.

Create a function that returns True if an array is a word-chain and False otherwise.

Examples
is_word_chain(["meal", "seal", "seat", "beat", "beet"]) ➞ True
# Change "m" in "meal" to get "seal", "l" to get "seat", etc.

is_word_chain(["red", "bed", "bet", "bat", "sat"]) ➞ True

is_word_chain(["red", "bat", "cat", "sat"]) ➞ False
# Do not change more than one letter ("red" and "bat").

is_word_chain(["read", "red", "led", "lad", "lady"]) ➞ False
# Do not add or subtract letters.
Notes
Each word in a word chain has equal length.
All words will be in lower case.
"""
# v2
def is_word_chain(lst):

	for first, second in zip(lst, lst[1:]):
		if sum(a != b for a, b in zip(first, second)) != 1:
			return False
	return True



# v1
# def is_word_chain(lst):
#
# 	while len(lst) > 1:
# 		for i in range(0, len(lst)):
# 			return findTheDifference(lst[i], lst[i+1], lst)
# 	return True
#
# def findTheDifference(s, t, lst):
#
# 	ls_s = [s[i] for i in range(len(s))]
# 	ls_t = [t[i] for i in range(len(t))]
#
# 	for elem in ls_s:
# 		if elem in ls_t:
# 			ls_t.remove(elem)
#
# 	if len(ls_t) == 1:
# 		return is_word_chain(lst[1:])
# 	else:
# 		return False


print(is_word_chain(["meal", "seal", "seat", "beat", "beet"]))
print(is_word_chain(["red", "bed", "bet", "bat", "sat"]))
print(is_word_chain(['heady', 'ready', 'beady', 'beads', 'meads', 'meats', 'seats', 'feats']))
print(is_word_chain(['score', 'scare', 'stare', 'spare', 'spire']))
print(is_word_chain(['more', 'mire', 'dire', 'dare', 'date']))

print(is_word_chain(["read", "red", "led", "lad", "lady"]))
print(is_word_chain(["red", "bat", "cat", "sat"]))
print(is_word_chain(['candy', 'candies', 'fat', 'rat']))
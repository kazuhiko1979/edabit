"""
Is the Sum of Letters Even or Odd?
Create a function that takes a string and returns True if the sum of the position of every letter in the alphabet is even and False if the sum is odd.

Examples
is_alpha("i'am king")  ➞ True
# 9 + 1 + 13 + 11 + 9 + 14 + 7 = 64 (even)

is_alpha("True") ➞ True
# 20 + 18 + 21 + 5= 64 (even)

is_alpha("alexa") ➞ False
# 1 + 12 + 5 + 24 + 1= 43 (odd)
Notes
Case insensitive.
Ignore non-letter symbols.
"""


def is_alpha(word):

	word = word.lower()
	alpha = "abcdefghijklmnopqrstuvwxyz"

	for w in word:
		if w in alpha:
			return (alpha.index(w) + 1) + is_alpha(word[1:])
		else:
			return is_alpha(word[1:])
	return 0


	# v1 bad
	# alphabets = string.ascii_lowercase
	# try:
	# 	if len(word) > 1:
	# 		if word[-1].lower().isalpha():
	# 			return (alphabets.index(word[-1]) + 1) + is_alpha(word[:-1])
	# 		else:
	# 			return is_alpha(word[:-1])
	# 	elif len(word) == 1:
	# 		if word[0].lower().isalpha():
	# 			return alphabets.index(word[-1]) + 1
	# except:
	# 	return alphabets.index(word[-1]) + 1 + alphabets.index(word[-1]) + 1

print(is_alpha("i'am king"))
print(is_alpha("True"))
print(is_alpha("alexa"))

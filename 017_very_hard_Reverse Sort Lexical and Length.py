"""
Reverse Sort: Lexical and Length
Write a function that sorts the words in a given string lexicographically (lexical sort) and by length in reverse order.

Examples
reverse_sort("You've rocked the pragmatic world in the making!")
 ➞ "pragmatic making! You've rocked world the the in"

reverse_sort("Tesh makes my world worth enjoying and living for.")
 ➞ "enjoying living worth world makes Tesh for. and my"

reverse_sort("Shaken by the bloody truth and crazy lies.")
 ➞ "Shaken bloody truth lies. crazy the and by"

reverse_sort("Programming in Python is a lot of fun.")
 ➞ "Programming Python fun. lot of is in a"
Notes
Special characters, punctuation marks and symbols are part of the word that directly precedes it.
The space character separates each word in the given string.
Case insensitive sorting is required.
"""

def reverse_sort(txt):

	# v2
	return " ".join(sorted(txt.split(),
						   key=lambda w: (len(w), w.lower(), w[0].isupper()),
						   reverse=True))

	# v1
	# lst = txt.split(" ")
	# lst = sorted(lst, key = lambda x: x.lower(), reverse=True)
	# lst = sorted(lst, key = lambda x: len(x), reverse=True)
	# return " ".join(lst)

	# NG
	# txt = list(txt.split(" "))
	# txt = sorted(txt, key=lambda L: (L.lower(), L))
	# txt = sorted(txt, key=len, reverse=False)
	# return ' '.join(i for i in txt[::-1])


print(reverse_sort("You've rocked the pragmatic world in the making!"))
print(reverse_sort("Tesh makes my world worth enjoying and living for."))
print(reverse_sort("Shaken by the bloody truth and crazy lies."))


print(reverse_sort("To do or not to do, is all up to you."))

'you. not do, all up to to To or is do'
'you. not do, all up To to to or is do'

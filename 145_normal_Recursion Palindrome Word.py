"""
Recursion: Palindrome Word
Create a recursive function that determines whether a word is a palindrome or not.

Examples
is_palindrome("madam") ➞ true

is_palindrome("adieu") ➞ false

is_palindrome("rotor") ➞ true
Notes
All inputs are in lowercase.
You are expected to solve this challenge via recursion.
"""

def is_palindrome(wrd):

	# v3
	return wrd == "" or wrd[0] == wrd[-1] and is_palindrome(wrd[1:-1])

	# v2
	# if len(wrd) <= 1:
	# 	return True
	# elif wrd[0] != wrd[-1]:
	# 	return False
	# return is_palindrome(wrd[1:-1])


	# v1
	# if len(wrd) > 1:
	# 	if wrd[0] == wrd[-1]:
	# 		wrd = wrd[1:]
	# 		wrd = wrd[:-1]
	# 		return is_palindrome(wrd)
	# 	else:
	# 		return False
	#
	# elif len(wrd) == 1 or len(wrd) == 0:
	# 	return True
	# else:
	# 	return 0

print(is_palindrome("madam"))
print(is_palindrome("adieu"))
print(is_palindrome("rotor"))



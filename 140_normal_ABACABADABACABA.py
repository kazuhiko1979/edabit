"""
ABACABADABACABA
Create a function that follows the "ABACABADABACABA" rule up to a certain letter.

The abacabadabacaba pattern is where you start with the first letter (a), and with each new letter, you add the letter in the middle and the others at the start and end.

For instance:

A ➞ **A**
B ➞ A**B**A
C ➞ ABA**C**ABA
D ➞ ABACABA**D**ABACABA
E ➞ ABACABADABACABA**E**ABACABADABACABA
F ➞ ABACABADABACABAEABACABADABACABA**F**ABACABADABACABAEABACABADABACABA

# And so on ...
Examples
ABA("A") ➞ "A"
ABA("B") ➞ "ABA"
ABA("E") ➞ "ABACABADABACABAEABACABADABACABA"
"""
def ABA(s):

	# v2
	# if s == 'A':
	# 	return s
	# return '{0}{1}{0}'.format(ABA(chr(ord(s)-1)), s)


	# v1
	# if s == 'A':
	# 	return 'A'
	# else:
	# 	return ABA(chr(ord(s)-1)) + s + ABA(chr(ord(s)-1))

	# v1
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if s == "A":
		return s
	return ABA(letters[letters.find(s)-1]) + s + ABA(letters[letters.find(s)-1])

# print(ABA("B"))
print(ABA("E"))

"""
Change the Word
Given a string, reverse its order, change lowercase letters to uppercase and increment uppercase letters by one (e.g. A becomes B, C becomes D, Z becomes A).

Examples
change_string("ApPle") ➞ "ELQPB"

change_string("draGON") ➞ "OPHARD"

change_string("ZebrA") ➞ "BRBEA"
Notes
Remember capital "Z" becomes "A".
"""
# v3
def change_string(word):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZA'
	return ''.join(alpha[alpha.index(i) + 1] if i.isupper() else i.upper() for i in word)[::-1]


# v2
# def change_string(word):
# 	return ''.join(i.upper() if i.islower() else chr(65 + (ord(i) - 64) % 26) for i in word[::-1])


# v1
# def change_string(word):
#
# 	return ''.join([i.upper() if i.islower() else chr((ord(i.upper()) + 1 - 65) % 26 + 65) for i in reversed(word)])

	# result = ""
	# for i in reversed(word):
	# 	if i.islower():
	# 		result += i.upper()
	# 	else:
	# 		result += chr((ord(i.upper()) + 1 - 65) % 26 + 65)
	#
	# return result


print(change_string("ApPle"))
print(change_string("draGON"))
print(change_string("ZebrA"))



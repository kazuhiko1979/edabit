"""
Mangle The String
Create a function that takes a string and replaces every letter with the letter following it in the alphabet ("c" becomes "d", "z" becomes "a", "b" becomes "c", etc). Then capitalize every vowel (a, e, i, o, u) and return the new modified string.

Examples
mangle("Fun times!") ➞ "GvO Ujnft!"

mangle("The quick brown fox.") ➞ "UIf rvjdl cspxO gpy."

mangle("Omega") ➞ "Pnfhb"
Notes
If a letter is already uppercase, return it as uppercase (regardless of being a vowel).
"y" is not considered a vowel.
"""
# v4
def mangle(txt):
	
	in_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	out = 'bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZA'
	return txt.translate(str.maketrans(in_, out))



# def mangle(txt):
#   x = ['A' if i in 'zZ' else chr(ord(i)+1) if i.isalpha() else i for i in txt]
#   return ''.join(i.upper() if i in 'aeiou' else i for i in x)

# v3
def mangle(txt):

	temp = []
	for i in txt:
		if i.isalpha():
			if i in 'zZ':
				temp.append(i)
			else:
				temp.append(chr(ord(i)+1))
		else:
			temp.append(i)

	result = []

	for x in temp:
		if x in "aiueo":
			result.append(x.upper())
		else:
			result.append(x)

	return ''.join(result)


# v2
# import string
# letters = string.ascii_letters
#
# def mangle(s):
#
# 	res = ""
# 	for x in s:
# 		if x == " ":
# 			res = res + " "
# 		elif not x.isalpha():
# 			res = res + x
# 		elif x == "z" or x == "Z":
# 			next_char = chr(ord(x) - 25)
# 			res = res + next_char.upper()
# 		else:
# 			x = letters[letters.index(x) + 1]
# 			if x in "aiueoAIUEO":
# 				nxt_letter = x.upper()
# 				res = res + nxt_letter
# 			else:
# 				res = res + x
# 	return res

print(mangle("Fun times!"))
print(mangle("abcz"))
print(mangle("ABCZ"),)


# v1
# def mangle(txt):
#
# 	rep_str = ''
#
# 	for letter in txt:
# 		if letter == "Z":
# 			rep_str = rep_str + "A"
# 			continue
# 		if letter == "z":
# 			rep_str = rep_str + "a"
# 			continue
# 		if letter == " ":
# 			rep_str = rep_str + " "
# 		elif not letter.isalpha():
# 			rep_str = rep_str + letter
# 		else:
# 			code = ord(letter)
# 			nxt_letter = chr(code + 1)
# 			if nxt_letter in "aiueoAIUEO":
# 				nxt_letter = nxt_letter.upper()
# 				rep_str = rep_str + nxt_letter
# 			else:
# 				rep_str = rep_str + nxt_letter
# 	return rep_str

# print(mangle("Fun times!"))
# print(mangle("The quick brown fox."))
# print(mangle("Omega"))
#
# print(mangle("abcz"))

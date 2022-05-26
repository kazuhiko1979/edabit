"""
Caesar Cipher
Create a function that takes two arguments (text, key) and returns a new encrypted text using the key. For example, if the input is "a" and the key is 1, it should move that letter 1 step in alphabetic order so the output would be "b".

Examples
caesar_cipher("hello", 5) ➞ "mjqqt"

caesar_cipher("hello world", 1) ➞ "ifmmp xpsme"

caesar_cipher("a", 2) ➞ "c"
Notes
The input is only letters and spaces; no special characters.
"""

def caesar_cipher(text, key):

	alphabets = 'abcdefghijklmnopqrstuvwxyz'

	# v3
	# maketrans - refer : https://hibiki-press.tech/python/str-translate/5322
	# translate - refer : https://qiita.com/tag1216/items/df6c93bdb823dd48af6c
	out = alphabets[key:] + alphabets[:key]
	return text.translate(str.maketrans(alphabets, out))



	# v2
	res = []
	# for ch in text:
	# 	if ch in alphabets:
	# 		res.append(alphabets[(alphabets.find(ch)+key) % 26])
	# 	else:
	# 		res.append(ch)
	# return ''.join(res)

	# return ''.join(alphabets[(alphabets.find(ch) + key) % 26] if ch in alphabets else ch for ch in text)


	# V1
	# final_list = []
	# new_word = ''
	# for char in text:
	# 	if char == " ":
	# 		final_list.append(" ")
	# 	if char in alphabets:
	# 		index_val = alphabets.index(char) + key
	# 		if index_val >= 26:
	# 			index_val = index_val - 26
	# 			new_word += alphabets[index_val]
	# 			final_list.append(new_word)
	# 			new_word = ''
	# 		elif index_val < 26:
	# 			new_word += alphabets[index_val]
	# 			final_list.append(new_word)
	# 			new_word = ''
	# return ''.join(final_list)


print(caesar_cipher("hello world", 1))
print(caesar_cipher("hello world", 26))
print(caesar_cipher("iwxh xh p rwxetg", 11))
print(caesar_cipher("z", 2))
print(caesar_cipher("fruuhfw", 23))
print(caesar_cipher("tfexirkj", 9))





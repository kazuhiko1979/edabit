"""
Super Reduced String
Steve has a string of lowercase characters in range ascii[["a".."z"]]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation, he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, return "Empty String".

Case
super_reduced_string("aaabccddd") ➞ "abd"
Explanation:

"aaabccddd" -> "abccddd" -> "abddd" -> "abd"
Examples
super_reduced_string("cccxllyyy") ➞ "cxy"

super_reduced_string("aa") ➞ "Empty String"

super_reduced_string("baab") ➞ "Empty String"

super_reduced_string("fghiiijkllmnnno") ➞ "fghijkmno"

super_reduced_string("chklssstt") ➞ "chkls"
"""
# v2
def super_reduced_string(txt):

	for i in txt:
		x = i + i
		if x in txt:
			txt = txt.replace(x, '')
	if txt == '':
		return "Empty String"
	return txt

# v1
# def super_reduced_string(txt):
#
# 	for i, j in enumerate(zip(txt, txt[1:])):
# 		if j[0] == j[1]:
# 			txt = txt[:i] + txt[i+1:]
# 			txt = txt[:i] + txt[i+1:]
# 			return super_reduced_string(txt)
#
# 	if not txt:
# 		return "Empty String"
# 	return txt


	# for i, j in zip(txt, txt[1:]):
	#
	# 	if i == j:
	# 		print(txt.index(i), txt.index(j))
	# 		txt = txt[:txt.index(i)] + txt[txt.index(i)+1:]
	# 		txt = txt[:txt.index(j)] + txt[txt.index(j)+1:]
	# 		print(txt)
	# 		return super_reduced_string(txt)
	#
	# if not txt:
	# 	return "Empty String"
	# return txt

	# for i, j in zip(txt, txt[1:]):
	# 	if i == j:
	# 		txt = txt[:txt.index(i)] + txt[txt.index(i)+1:]
	# 		txt = txt[:txt.index(j)] + txt[txt.index(j)+1:]
	# 		return super_reduced_string(txt)
	#
	# if not txt:
	# 	return "Empty String"
	# return txt


print(super_reduced_string("cccxllyyy"))
print(super_reduced_string("aa"))
print(super_reduced_string("baab"))
print(super_reduced_string("fghiiijkllmnnno"))
print(super_reduced_string("chklssstt"))

print(super_reduced_string("acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj"))


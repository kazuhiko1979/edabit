"""
Message from Space
You have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:

Message string will consist of capital letters, numbers, and brackets only.
When there's a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times.
Message can be embedded in multiple layers of blocks.
Final decrypted message will only consist of capital letters.
Create a function that takes encrypted message txt and returns the decrypted message.

Examples
space_message("ABCD") ➞ "ABCD"

space_message("AB[3CD]") ➞ "ABCDCDCD"
# "AB" = "AB"
# "[3CD]" = "CDCDCD"

space_message("IF[2E]LG[5O]D") ➞ "IFEELGOOOOOD"

space_message("AB[2C[2EF]G]") -> "ABCEFEFGCEFEFG"
"""
# v1

# import re
#
# def change(s):
# 	s = s.replace('[', '').replace(']','')
# 	return s[1:] * (int(s[0]))
#
# def space_message(txt):
#
# 	for i in range(2):
# 		txt = re.sub(r'\[\w+\]', lambda x:change(x.group(0)), txt)
# 	return txt

# v2
def space_message(txt):
	res = ['']
	for c in txt:
		if c == '[':
			res.append('')
		elif c == ']':
			tmp, i = res.pop(), 0
			# print(tmp, i)
			while tmp[i].isdigit():
				i += 1
			res[-1] += tmp[i:]*int(tmp[:i])
		else:
			res[-1] += c
	return res


print(space_message("AB[3CD]"))
print(space_message("IF[2E]LG[5O]D"))
print(space_message("AB[2[3CD]]"))
print(space_message("AB[2C[2EF]G]"))
print(space_message("MU[2B][2A][2S][2H][2I]RISN[4O]TAMA[4Z]ING"))

"""
Difference Cipher
It's time to send and receive secret messages.

Create a single function that takes a string or a list and returns a coded or decoded message.

The first letter of the string, or the first element of the list represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.

Examples
dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
# H = 72, the difference between the H and e is 29 (upper- and lowercase).
# The difference between the two l's is obviously 0.

dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]
Notes
The input of the function will always be a string or a list with numbers.
"""
def dif_ciph(inpt):
	if type(inpt) is str:
		return [ord(inpt[0])] + [ord(b) - ord(a) for a, b in zip(inpt, inpt[1:])]
	else:
		for i in range(1, len(inpt)):
			inpt[i] += inpt[i-1]
		return ''.join(chr(code) for code in inpt)





# def dif_ciph(input:str or list) -> str or list:
#
# 	if type(input) == str:
# 		res = []
# 		res.append(ord(input[0]))
#
# 		for x in range(1, len(input)):
# 			res.append(ord(input[x]) - ord(input[x-1]))
# 		return res
#
# 	if type(input) == list:
# 		res = []
# 		top = chr(input[0])
# 		res.append(top)
# 		for x in range(1, len(input)):
# 			res.append(chr(input[x] + ord(top)))
# 			top = chr(input[x] + ord(top))
# 		return ''.join(res)

print(dif_ciph("How are you?"))
print(dif_ciph("?"))
print(dif_ciph([84, 20,  -3,  -69,  78,  -9,  4,  -2,  1,  -6,  13,  6,  -3,  1,  -83,  65,  17,  -13,  -69,  83,  1,  -2,  -17,  13,  -7,  -2,  -55,  0 ]))


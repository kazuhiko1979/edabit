"""
String Expansion
Create a function that takes a string txt and expands it as per the following rules:

The numeric values represent the occurrence of each letter preceding that numeric value.
string_expansion("3M2u5b2a1s1h2i1r") ➞ "MMMuubbbbbaashiir"
The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears.
string_expansion("3Mat")➞ "MMMaaattt"      # correct

string_expansion("3Mat") ➞ "MMMat"          # wrong
string_expansion("3Mat") ➞ "MatMatMat"      # wrong
If there are consecutive numeric characters, ignore them all except last one.
string_expansion("3M123u42b12a") ➞ "MMMuuubbaa"
If there are two consecutive alphabetic characters then the string will remain unchanged.
string_expansion("airforce") ➞ "airforce"
Empty strings should return an empty string.
string_expansion("") ➞ ""
"""
# v3
def string_expansion(txt):

	m, n = "", 1

	for j in txt:
		if j.isdigit():
			n = int(j)
		else:
			m += j*n
	return m


# v2
# def string_expansion(txt):
#
# 	final = ""
# 	cur = ""
# 	expand = 1
#
# 	for i in txt:
# 		if i.isalpha():
# 			cur += i
# 		elif cur != "":
# 			final += "".join(j * expand for j in cur)
# 			cur = ""
# 			expand = int(i)
# 		else:
# 			expand = int(i)
#
# 	return final + "".join(i * expand for i in cur)


# v1
# def string_expansion(txt):
#
# 	if txt.isdigit():
# 		return ""
#
# 	result = []
# 	num = ""
# 	alpha = ""
#
# 	for value in txt:
# 		if not alpha:
# 			if value.isdigit():
# 				num += value
# 			elif value.isalpha():
# 				alpha += value
# 		else:
# 			if value.isalpha():
# 				alpha += value
# 				continue
# 			temp = [num, alpha]
# 			result.append(temp)
# 			num = ""
# 			alpha = ""
# 			num += value
# 			continue
#
# 	temp = [num, alpha]
# 	result.append(temp)
# 	# print(result)
#
# 	text = ""
#
# 	for n, v in result:
#
# 		if v == '':
# 			pass
# 		if n == '':
# 			n = "1"
#
# 		if len(v) > 1:
# 			if len(n) > 1:
# 				for j in v:
# 					text += j * int(str(n[-1]))
# 			elif len(n) == 1:
# 				for j in v:
# 					text += j * int(n)
#
# 		elif len(n) > 1:
# 			for j in v:
# 				text += j * int(str(n[-1]))
# 		elif len(n) == 1:
# 			for j in v:
# 				text += j * int(n)
# 		else:
# 			text += v * int(n)
#
# 	return text


print(string_expansion("3M2u5b2a1s1h2i1r"))
print(string_expansion("3Mat"))
print(string_expansion("3M123u42b12a"))
print(string_expansion("3n6s7f3n"))
print(string_expansion("0d4n8d2b"))
print(string_expansion("0c3b1n7m"))
print(string_expansion("2B"))


print(string_expansion("A4g1b4d"))
print(string_expansion("111111"))
print(string_expansion("5M0L8P1"))

print(string_expansion("5919nf3u"))

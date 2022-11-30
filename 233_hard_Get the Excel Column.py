"""
Get the Excel Column
Excel column names are in the following format:

A, B, ..., Z, AA, ..., AZ, BA, ..., ZZ, AAA, AAB, ...
Write a function that returns the column number from the row name.

Examples
column("A") ➞ 1

column("Z") ➞ 26

column("AA") ➞ 27

column("BA") ➞ 53
"""

# alpha = "ABCDEDFHIZKLMNOPQRSTUVWXYZ"

# alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
# 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
# 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
#
#
# def column(txt):
#
# 	# total = 0
# 	# txt = txt[::-1]
# 	# for i in range(len(txt)):
# 	# 	print(i)
# 	# 	total += alpha[txt[i]]*26**i
# 	# return total
#
# 	temp = ''.join(list(reversed(txt)))
# 	result = 0
#
# 	for key, value in enumerate(temp):
# 		result += alpha[value]*26**key
# 	return result

# print(column("A"))
# print(column("B"))
# print(column("Z"))
#
# print(column("AA"))
# print(column("BA"))
# print(column("CW"))
# print(column("DD"))
# print(column("PQ"))

# print(column("ABC"))
# print(column("ZZ"))

# print(column("ZZT"))
# print(column("STVW"))

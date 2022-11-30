"""
Express Number in Expanded Notation
Create a function that takes a number and return a string with the number in expanded notation (AKA expanded form). See the resources tab for details on expanded notation.

Examples
expand(13) ➞ "10 + 3"

expand(86) ➞ "80 + 6"

expand(17000000) ➞ "10000000 + 7000000"

expand(5325) ➞ "5000 + 300 + 20 + 5"
Notes
You can expect only whole numbers greater than 0 as test input.
"""

def expand(num):

	n = str(num)
	return ' + '.join([x + "0" * (len(n)-1-i) for i, x in enumerate(n) if x != "0"])

# def expand(num):
#
# 	result = []
# 	temp = ""
#
# 	for i, n in enumerate(reversed(str(num))):
# 		if int(n) > 0:
# 			temp += n
# 			temp += "0" * i
# 			result.append(temp)
# 			temp = ""
#
# 	return " + ".join(list(reversed(result)))

print(expand(13))
print(expand(86))
print(expand(17000000))
print(expand(5325))





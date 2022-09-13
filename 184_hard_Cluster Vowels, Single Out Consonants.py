"""
Cluster Vowels, Single Out Consonants
Write a function that takes in a word and splits the consonants one by one, but keeps the vowels in a cluster.

Examples
split("beautifully") ➞ ["b", "eau", "t", "i", "f", "u", "l", "l", "y"]

split("spoonful") ➞ ["s", "p", "oo", "n", "f", "u", "l"]

split("swimming") ➞ ["s", "w", "i", "m", "m", "i", "n", "g"]
Notes
Vowels are: a, e, i, o, u.
All letters will be in lower case.
"""
# import re
#
# def split(txt):
#
# 	return re.findall('[aiueo]+|[bcdfghjklmnpqrstvwxyz]{1}', txt)


# def split(txt):
#
# 	result = []
# 	vowels = ''
#
# 	for i in txt:
# 		if i in 'aeiou':
# 			vowels += i
# 		else:
# 			result = result + ([vowels] if vowels != '' else [])
# 			vowels = ''
# 			result += [i]
# 	result = result + ([vowels] if vowels != '' else [])
# 	return result

vowels = 'aeiou'

def split(word):
	output = []
	cluster = ''
	for i in range(len(word)):
		if word[i] not in vowels:
			if cluster != '':
				output.append(cluster)
				output.append(word[i])
				cluster = ''
			else:
				output.append(word[i])
		else:
			cluster += word[i]

	if cluster != '':
		output.append(cluster)
	return output

print(split("beautifully"))
print(split("spoonful"))
print(split("swimming"))

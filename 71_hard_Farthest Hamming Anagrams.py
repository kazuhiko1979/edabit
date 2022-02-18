"""
Farthest Hamming Anagrams
An anagram is a word, x, formed by rearranging the letters that make up another word, y, and using up all the letters in y at the same frequency. For example, "dear" is an anagram of "read" and "plead" is an anagram of "paled".

The Hamming distance between two strings is the number of positions at which they differ. Hamming distances can only be calculated for strings of equal length.

s1 = "eleven"

s2 = "twelve"
They only have the third position (index 2) in common, giving them a Hamming distance of 5.

As anagrams are of identical length, the Hamming distance between them can be calculated.

s1 = "read"

s2 = "dear"
These strings differ at the first and last positions, giving them a Hamming distance of 2. "Plead" and "paled" have a Hamming distance of 3.

Create a function that takes two strings, and returns:

True if they are anagrams of each other and their Hamming distance is equal to their length (i.e. no letters in the same positions).
False if they aren't anagrams, or
Their Hamming distance if they are anagrams with >=1 letter at the same index.
Examples
max_ham("dear", "read") ➞ 2

max_ham("dare", "read") ➞ True

max_ham("solemn", "molest") ➞ False
"""

def max_ham(str1, str2):

	if sorted(list(str1)) != sorted(list(str2)):
		return False

	d = sum(1 for i in range(len(str1)) if str1[i] != str2[i])
	return d if d != len(str1) else True


	# if sorted(str1) != sorted(str2):
	# 	return False
	#
	# ham = 0
	# for i in range(len(str1)):
	# 	if str1[i] != str2[i]:
	# 		ham += 1
	#
	# return True if ham == len(str1) else ham









# # Python program to check if two strings are anagrams of
# # each other
# NO_OF_CHARS = 256
#
#
# def max_ham(str1, str2):
#
# 	# Create two count arrays and initialize all values as 0
# 	count1 = [0] * NO_OF_CHARS
# 	count2 = [0] * NO_OF_CHARS
#
# 	# For each character in input strings, increment count
# 	# in the corresponding count array
# 	for i in str1:
# 		count1[ord(i)] += 1
#
# 	for i in str2:
# 		count2[ord(i)] += 1
#
# 	if len(str1) != len(str2):
# 		return False
#
# 	# Compare count arrays
# 	for i in range(NO_OF_CHARS):
#
# 		if count1[i] != count2[i]:
# 			return False
#
# 	# return 1
# 	else:
#
# 		# Hamming distance
# 		i = 0
# 		count = 0
#
# 		while (i < len(str1)):
# 			if (str1[i] != str2[i]):
# 				count += 1
# 			i += 1
#
# 		if len(str1) == count and len(str2) == count:
# 			return True
# 		return count


print(max_ham("dare", "read"))
print(max_ham("dear", "read"))
print(max_ham('naive','ravine'))
print(max_ham('observe','verbose'))
print(max_ham('mister','remits'))
print(max_ham('pirates','traipse'))
print(max_ham('petal','leapt'))
print(max_ham('solemn','molest'))
print(max_ham('solemn','melons'))

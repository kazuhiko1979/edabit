"""
ASCII Capitals
Each character in the English Alphabet has an ASCII Char Code.

Create a function that converts any word in a given sentence to upper case if the sum of the ASCII codes of the letters in the word is greater than the global average for the sentence. The global average of a sentence is the sum of all the word values divided by the number of words.

For example:

Word	Tell	me	the	time
Sum	401	210	321	431
Since on average, a word in this sentence has a char code sum of 340.75, "Tell" & "time" would be returned capitalised: "TELL me the TIME"

Examples
average_ascii("Tell me the time") ➞ "TELL me the TIME"
# Global Average for char code sum of a word is 340.75

average_ascii("To be or not to be") ➞ "To be or NOT to be"
# Global Average for char code sum of a word is 230.33

average_ascii("Edabit helps you learn in bitesize chunks") ➞ "EDABIT HELPS you learn in BITESIZE CHUNKS"
# Global Average for char code sum of a word is 533.43
Notes
Do not count whitespace as part of a word.
There will be no punctuation/special characters in the tests.
If a word does not meet the capitalisation citeria, don't fully lowercase it ⁠— leave it how it is (i.e. the first words of a sentence should not be fully lowercased if they don't meet the criteria).
The char code of a capital letter will be different than its lowercase counterpart.
When you find the global average, it may help to round it to 2 decimal places, then compare against it.
"""

# v2
def average_ascii(txt):

	lst = txt.split()
	ave = sum([sum([ord(i) for i in j]) for j in lst]) / len(lst)

	temp = []
	for j in lst:
		if sum([ord(i) for i in j]) <= ave:
			temp.append(j)
		else:
			temp.append(j.upper())
	return ' '.join(temp)


# v1
# def average_ascii(txt):
#
# 	chr_list = []
# 	sub_total = 0
#
# 	temp = list(txt.split(" "))
#
# 	if len(temp) == 1:
# 		return txt
#
# 	for txt in temp:
# 		for words in txt:
# 			sub_total += ord(words)
# 		chr_list.append(sub_total)
# 		sub_total = 0
# 	avg = sum(chr_list) / len(chr_list)
#
# 	for k, v in zip(chr_list, temp):
# 		if k >= avg:
# 			temp[chr_list.index(k)] = temp[chr_list.index(k)].upper()
# 	return ' '.join(temp)

print(average_ascii("Edabit helps you learn in bitesize chunks"))
print(average_ascii("To be or not to be"))
print(average_ascii("What you egg"))
print(average_ascii("Made by Harith Shah"))
print(average_ascii("Boom"))
print(average_ascii("The most addictive way to learn"))
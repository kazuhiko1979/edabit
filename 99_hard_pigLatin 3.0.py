"""
pigLatin 3.0
Write a function that converts a sentence into pig latin.

Rules for converting to pig latin:

For words that begin with a vowel (a, e, i, o, u), add "way".
Otherwise, move all letters before the first vowel to the end and add "ay".
For simplicity, no punctuation will be present in the inputs.
Examples
pig_latin_sentence("this is pig latin") ➞ "isthay isway igpay atinlay"

pig_latin_sentence("wall street journal") ➞ "allway eetstray ournaljay"
Notes
All letters will be in lowercase.
"""

# v2
# def pigLatin(w):
# 	if w[0] in 'aeiou':
# 		return w + 'way'
# 	for i, c in enumerate(w):
# 		if c in 'aeiou':
# 			return w[i:] + w[:i] + 'ay'
#
# def pig_latin_sentence(sentence):
#
# 	return ' '.join(pigLatin(w) for w in sentence.split())



# v1
# def pig_latin_sentence(sentence):

	# vowels = {'a', 'e', 'i', 'o', 'u'}
	# result = []
	#
	# for cha in sentence.split():
	# 	for i in cha:
	# 		if i in vowels:
	# 			if cha.index(i) == 0:
	# 				result.append(cha + "way")
	# 				break
	# 			if cha.index(i) > 0:
	# 				pop_cha = cha[cha.index(i):]
	# 				origin_cha = cha[:cha.index(i)]
	# 				result.append(pop_cha + origin_cha + "ay")
	# 				break
	# return ' '.join(result)


print(pig_latin_sentence("this is pig latin"))
print(pig_latin_sentence("wall street journal"))



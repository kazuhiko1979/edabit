"""
Constrained Writing
In this challenge, establish which type of constrained writing is applied to a sentence. There are four possible types to detect:

Pangram: the sentence contains all the 26 letters of the English alphabet.
Heterogram: the sentence doesn't have multiple instances of its letters (as to say that every letter is unique).
Tautogram: every word of the sentence starts with the same letter.
Transgram: all words of the sentence share at least a common letter.
Given a string txt being a sentence, implement a function that returns the strings "Pangram", "Heterogram", "Tautogram" or "Transgram" accordingly to the above definitions and following the same given order to establish the result. If no constrained writing is detected, return the string "Sentence".

Examples
constraint("The quick brown fox jumps over the lazy dog.") ➞ "Pangram"
# The sentence contains every letter of the alphabet.
# Repetitions are not considered.

constraint("The big dwarf only jumps.") ➞ "Heterogram"
# The sentence has only unique characters.

constraint("Todd told Tom to take the tiny turtles.") ➞ "Tautogram"
# Every word starts with the letter "t".

constraint("A cannibal alligator has attacked an unaware vegan alligator.") ➞ "Transgram"
# Every word contains the letter "a".

constraint("The unbearable lightness of coding...") ➞ "Sentence"
# No constraint is applied to the sentence.
Notes
Remember to respect the given order to establish the result: a Pangram has to be detected before a Heterogram, and a Tautogram has to be detected before a Transgram.
Sentences will contain letters (either uppercase or lowercase) and punctuation. Your function must be case-insensitive.
"""

alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
def constraint(txt):

	result = txt.replace(' ', '')
	result = result.replace('.', '')

	common_characters = alphabet_set.intersection(result.lower())

	character_set = set()
	def heterogram(result):
		for char in result:
			if char in character_set:
				return False
			character_set.add(char)
		return True

	def tautogram(txt):
		starts_with_t = set([word[0].lower() for word in txt.split(' ')])
		return len(starts_with_t) == 1

	def transgram(txt):
		words = txt.split()
		common_characters = set(words[0].lower())
		for word in words[1:]:
			common_characters = common_characters.intersection(set(word.lower()))
		return common_characters


	if len(common_characters) == 26:
		return "Pangram"
	elif heterogram(result):
		return "Heterogram"
	elif tautogram(txt):
		return "Tautogram"
	elif transgram(txt):
		return "Transgram"
	else:
		return "Sentence"

print(constraint("The quick brown fox jumps over the lazy dog."))
print(constraint("The big dwarf only jumps."))
print(constraint("Todd told Tom to take the tiny turtles."))
print(constraint("A cannibal alligator has attacked an unaware vegan alligator."))
print(constraint("The unbearable lightness of coding..."))
print(constraint("Pack my box with five dozen liquor jugs."))
print(constraint("The dog is crazy."))
print(constraint("It is indeed included instantly!"))
print(constraint("Those loops could work without constants sometimes."))
print(constraint("Sphinx of black quartz, judge my vow."))
print(constraint("Mind the gap!"))
print(constraint("Put some more tobacco inside it next time, it's just too strong!"))
print(constraint("Thursdays: the time to teach them the truth."))
print(constraint("Would you mind pass me that axe, Eugene?"))
print(constraint("AbCdEfGhIjKlMnOpQrStUvWxYz"))
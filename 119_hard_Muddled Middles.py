"""
Muddled Middles
Given a sentence of all lowercase words, reverse all the letters in each word, but leave the first and last letters as they are.

Examples
mix_middle("the quick brown fox jumps high") ➞ "the qciuk bworn fox jpmus hgih"

mix_middle("this sentence is quite muddled") ➞ "tihs scnetnee is qtiue melddud"

mix_middle("buying a first-class ticket") ➞ "bniyug a fsalc-tsris tekcit"
Notes
Treat hyphenated words like one word (example #3).
Notice how one, two and three-letter words remain unchanged.
"""

def mix_middle(txt):

	# v2
	list = txt.split(' ')
	txt = ''
	for i in list:
		if len(i) > 3:
			txt += i[0]
			txt += i[1:-1][::-1]
			txt += i[-1]
		else:
			txt += i
		txt += ' '
	return txt[0:-1]


	result = []
	temp = []
	a = ""

	for word in txt.split():
		original_word = word
		if len(original_word) == 1 or len(original_word) == 2:
			a = original_word
			result.append(a)
			temp = []
			continue
		else:
			left, right, center = [], [], []
			middle = len(word)
			print(middle)
			last_buttom = word[-1]
			firt_top = word[0]

		middle = len(word)

		while middle > 2:
			if middle == 3:
				top = word[0]
				buttom = word[-1]
				center = word[1]

				right = right[::-1]
				left.insert(0, firt_top)
				right.append(last_buttom)

				temp.append(left)
				temp.append(center)
				temp.append(right)

				for i in temp:
					if type(i) == list:
						a += ''.join(i)
					else:
						a += i
				result.append(a)
				a = ""
				temp = []
				break

			if middle == 2:
				temp = []
				break
			else:
				word = word.lstrip(word[0])
				word = word.rstrip(word[-1])
				top = word[0]
				buttom = word[-1]
				left.append(buttom)
				right.append(top)
				middle = len(word)

	if len(original_word) != 1 or len(original_word) != 2:
		if len(original_word) % 2 == 0:
			right = right[::-1]
			left.insert(0, firt_top)
			right.append(last_buttom)

			temp = ''.join(left + right)
			result.append(temp)
			temp = []
		else:
			right = right[::-1]
			left.insert(0, firt_top)
			right.append(last_buttom)

			temp = ''.join(left + right)
			result.append(temp)
			temp = []

	return " ".join(result)


print(mix_middle("the quick brown fox jumps high"))
print(mix_middle("this sentence is quite muddled"))
print(mix_middle("buying a first-class ticket"))
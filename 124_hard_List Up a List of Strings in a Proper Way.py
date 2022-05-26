"""
List Up a List of Strings in a Proper Way
Given a list of strings (nouns), list them up in a complete sentence.

Examples
sentence(["orange", "apple", "pear"]) ➞ "An orange, an apple and a pear."

sentence(["keyboard", "mouse"]) ➞ "A keyboard and a mouse."

sentence(["car", "plane", "truck", "boat"]) ➞ "A car, a plane, a truck and a boat."
Notes
The sentence starts with a capital letter.
Do not change the order of the words.
A/An should be correct in all places.
Put commas between nouns, except between the last two (there you put "and").
The sentence ends with a .
There are at least two nouns given.
Every given word is lowercase.
"""

def is_vowel(c):
	return c in ['a', 'e', 'i', 'o', 'u']

def sentence(lst):

	temp = []

	for word in lst:
		first = word[0]
		if is_vowel(first):
			temp.append("an " + word)
		else:
			temp.append("a " + word)

	# case 2 words
	if len(lst) == 2:
		temp.insert(1, "and")
		return " ".join(temp).capitalize() + "."

	# case 3 words
	if len(lst) == 3:
		temp[0] = temp[0] + ","
		temp.insert(2, "and")
		return " ".join(temp).capitalize() + "."

	# case over 4 words
	if len(lst) > 3:
		for key, val in enumerate(temp[:-2]):
			temp[key] = val + ","
		temp.insert(-1, "and")
	return " ".join(temp).capitalize() + "."




	# v1
	# head = []
	# middle = []
	# buttom = []
	#
	# # 単語数が2の場合
	# if len(lst) == 2:
	# 	if lst[0][0] in "aiueo":
	# 		lst.insert(0, "An")
	# 	else:
	# 		lst.insert(0, "A")
	#
	# 	if lst[2][0] in "aiueo":
	# 		lst.insert(2, "an")
	# 	else:
	# 		lst.insert(2, "a")
	# 	lst.insert(2, "and")
	# 	return " ".join(lst) + "."
	#
	# # 単語数が3の場合
	# if len(lst) == 3:
	# 	if lst[0][0] in "aiueo":
	# 		head.append("An " + lst[0] + ", ")
	# 	else:
	# 		head.append("A " + lst[0] + ", ")
	# # 後方2単語処理
	# 	for i in lst[1:]:
	# 		if i[0] in "aiueo":
	# 			i = "an " + i
	# 			buttom.append(i)
	# 		else:
	# 			i = "a " + i
	# 			buttom.append(i)
	# 	buttom.insert(1, "and")
	# 	buttom = " ".join(buttom) + "."
	# 	return "".join(head) + buttom
	#
	# # 単語数が4以上処理
	# if len(lst) > 3:
	# 	if lst[0][0] in "aiueo":
	# 		head.append("An " + lst[0] + ", ")
	# 	else:
	# 		head.append("A " + lst[0] + ", ")
	# # 中間単語処理
	# 	for i in lst[1:-2]:
	# 		if i[0] in "aiueo":
	# 			i = "an " + i
	# 			middle.append(i + ",")
	# 		else:
	# 			i = "a " + i
	# 			middle.append(i + ",")
	# # 後方2単語処理
	# 	for i in lst[-2:]:
	# 		# print(i)
	# 		if i[0] in "aiueo":
	# 			i = "an " + i
	# 			buttom.append(i)
	# 		else:
	# 			i = "a " + i
	# 			buttom.append(i)
	#
	# 	buttom.insert(1, "and")
	# 	buttom = " ".join(buttom) + "."
	# 	return " ".join(head) + " ".join(middle) + " " + buttom

print(sentence(["orange", "apple", "pear"]))
print(sentence(["banana", "apple", "orange"]))
print(sentence(["car", "plane"]))
print(sentence(["keyboard", "mouse"]))
print(sentence(["car", "plane", "truck", "boat"]))
print(sentence(["fox", "wolf", "elephant", "cat"]))
print(sentence(["aa", "ee", "ii", "oo", "uu", "vv", "tt", "qw", "zz"]))




"""
Capitalization Families
Write a function that groups words by the number of capital letters and returns a dictionary of object entries whose keys are the number of capital letters and the values are the groups.

Examples
grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]) ➞ {
  0: ["yummy"],
  2: ["mayBE", "mOOdy"],
  3: ["HaPPy"]
}

grouping(["eeny", "meeny", "miny", "moe"]) ➞ {
  0: ["eeny", "meeny", "miny", "moe"]
}

grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]) ➞ {
  0: ["lor"],
  1: ["sOr"],
  2: ["MoR", "bOR", "tOR"],
  3: ["FORe"]
}
Notes
The object entries have to be sorted by the number of capital letters.
The groups will be arrays of all words sharing the same number of capital letters.
The groups have to be sorted alphabetically (ignoring case).
Words will be unique.
"""
def grouping(words):
	words.sort(key=str.lower)
	groups = {}

	for w in words:
		cap = sum(map(str.isupper, w))
		if cap in groups:
			groups[cap].append(w)
		else:
			groups[cap] = [w]
	return groups


# def grouping(w):
#
# 	capitalize_count_per_word = {}
#
# 	for word in w:
# 		capitalize_count = sum(1 for letter in word if letter.isupper())
# 		capitalize_count_per_word[word] = capitalize_count
#
# 	grouped_dict = {}
#
# 	for word, count in capitalize_count_per_word.items():
# 		if count not in grouped_dict:
# 			grouped_dict[count] = [word]
# 		else:
# 			grouped_dict[count].append(word)
#
# 	sorted_grouped_dict = {key: sorted(value, reverse=False) for key, value in sorted(grouped_dict.items())}
# 	return sorted_grouped_dict


print(grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]))
print(grouping(["the", "them", "theme", "EVERY"]))
print(grouping(["eeny", "meeny", "miny", "moe"]))
print(grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]))
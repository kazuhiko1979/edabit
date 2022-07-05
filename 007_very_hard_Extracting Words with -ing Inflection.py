"""
Extracting Words with "-ing" Inflection
Write a function that takes a string as an argument and returns a list of all the words inflected by "-ing". Your function should also exclude all the mono-syllabic words ending in "-ing" (e.g. bing, sing, sling, ...). Although these words end in "-ing", the "-ing" is not an inflection affix.

Examples
ing_extractor("coming bringing Letting sing") ➞ ["coming", "bringing", "Letting"]

ing_extractor("going Ping, king sHrink dOing") ➞ ["going", "dOing"]

ing_extractor("zing went ring, ding wing SINk") ➞ []
Notes
Mono-syllabic means a word containing just one syllable.
It's probably best to use RegEx for this challenge.
"""


def ing_extractor(str):

	str = [i for i in str.split() if i[-3:].lower() in "ing"]
	temp = []
	for i in str:
		for j in i[:-3]:
			if j.lower() in 'aiueo':
				temp.append(i)

	return sorted(set(temp), key=temp.index)


print(ing_extractor("feeling killing saying discussing FALLing"))
print(ing_extractor("Taking taLkING pending SING"))
print(ing_extractor("suggest drive run lend"))
print(ing_extractor("KING sing bring ring pING"))
print(ing_extractor("bing reading dancing ing"))

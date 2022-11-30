"""
Words Inside Words
Words can be grouped together when one word can be found within another (e.g. eat is in heat and theater). Given a list of words, return a dictionary that groups together each word with a list of all other words that contain it. Each group of words should be returned in alphabetical order.

Examples
word_groups(["grates", "rat", "rates", "rations"]) ➞ {
  "rates": ["grates"],
  "rat": ["grates", "rates", "rations"]
}

word_groups(["duct", "produce", "product", "rod"]) ➞ {
  "duct": ["product"],
  "rod": ["produce", "product"]
}

word_groups(["her", "the", "here", "other", "there"]) ➞ {
  "the": ["other", "there"],
  "here": ["there"],
  "her": ["here", "other", "there"]
}
Notes
Words can belong to more than one group.
"""
# v2

def word_groups(lst):

	dic = {}

	for i in lst:
		x = [j for j in lst if i in j and i != j]
		if x:
			dic[i] = sorted(x)
	return dic



#  V1
# def word_groups(lst):
#
# 	dic = {}
# 	values = []
#
# 	for i in lst:
# 		for j in lst:
# 			if i != j:
# 				if i in j:
# 					if j not in values:
# 						values.append(j)
# 						values = sorted(values)
# 						dic[i] = values
# 		values = []
# 	return dic

print(word_groups(["grates", "rat", "rates", "rations"]))
print(word_groups(["duct", "produce", "product", "rod"]))
print(word_groups(["her", "the", "here", "other", "there"]))
print(word_groups(['cargo', 'are', 'bar', 'car', 'careful', 'embargo']))


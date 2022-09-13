"""
Recursion: Find The Longest Word
Write a recursive function that will return the longest word in a sentence. In cases where more than one word is found, return the first one.

Examples
find_longest("I will and ever will be gratefully and perpetually loving you Tesh!") ➞ "perpetually"

find_longest("A thing of beauty is a joy forever.") ➞ "forever"

find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"

find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"
Notes
Special characters and symbols don't count as part of the word.
Return the longest word found in lowercase letters.
You are expected to solve this challenge via a recursive approach.
"""
# v3
import re

def find_longest(s, w=''):
	if not s:
		return w
	t = re.search(r'\w+', s.lower())
	if t:
		t = t.group(0)
	if len(t) > len(w):
		w = t
	return find_longest(s[len(t)+1:], w)


# v2
# def find_longest(s, res=None):
#
# 	if res is None:
# 		s = (s.lower().replace(',', '').replace('.', '').replace('\'s', '')
# 			 .replace('\"', '').split())
# 		res, s = s[0], s[1:]
#
# 	return (find_longest(s[1:], s[0]) if len(s[0]) > len(res)
# 			else find_longest(s[1:], res)) if s else res








# v1
# import re
# import copy
#
# reg = r'[^A-Za-z ]+'
#
# def find_longest(*s, longest=[]):
# 	if type(s) == tuple:
# 		if type(s[-1]) != list:
# 			s = ' '.join([i for i in s])
# 		else:
# 			s = s[0]
#
# 	s = re.sub(reg, ' ', s).split()
# 	temp = s[0]
#
# 	if not longest:
# 		longest.append(temp)
# 	if len(temp) >= len(longest[0]):
# 		longest.clear()
# 		longest.append(temp)
# 		s = ' '.join(s[1:])
# 		if s:
# 			return find_longest(s)
# 		result = copy.deepcopy(longest[0])
# 		longest.clear()
# 		return result.lower()
# 	else:
# 		s = ' '.join(s[1:])
# 		if s:
# 			return find_longest(s)
# 		result = copy.deepcopy(longest[0])
# 		longest.clear()
# 		return result.lower()

print(find_longest("Hello darkness my old friend.", "Yourself is your soul's captain and fate's master."))
print(find_longest("I will and ever will be gratefully and perpetually loving you Tesh!"))
print(find_longest("A thing of beauty is a joy forever."))
print(find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel."))
print(find_longest("The pretty daughter's toy, a doll, is as pretty as her."))


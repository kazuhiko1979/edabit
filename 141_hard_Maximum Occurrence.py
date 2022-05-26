"""
Maximum Occurrence
Given a string text. Write a function that returns the character with the highest frequency. If more than 1 character has the same highest frequency, return all those characters as an array sorted in ascending order. If there is no repetition in characters, return "No Repetition".

Examples
max_occur("Computer Science") ➞ ['e']

max_occur("Edabit") ➞ "No Repetition"

max_occur("system admin") ➞ ['m', 's']

max_occur("the quick brown fox jumps over the lazy dog") ➞ [' ']
Notes
Try to make use of the concept used in counting sort.
"""

from collections import defaultdict
from collections import Counter

def max_occur(text):

	# v3
	max_count, cnt = 1, dict()
	for c in text:
		if c in cnt:
			cnt[c] += 1
		else:
			cnt[c] = 1
		max_count = max(max_count, cnt[c])

	return sorted(k for k, v in cnt.items() if v == max_count) \
			if max_count > 1 else "No Repetition"


	# v2
	# d = Counter(text)
	# m = max(d.values())
	# res = [x for x in d if d[x] == m]
	# return sorted(res) if m!=1 else "No Repetition"


	# v1
	# temp = {}
	# for i in text:
	# 	if i in temp:
	# 		temp[i] += 1
	# 	else:
	# 		temp[i] = 1
	# d = defaultdict(list)
	# for key, value in temp.items():
	# 	d[value].append(key)
	# if max(d.items())[0] != 1:
	# 	return sorted(max(d.items())[1])
	# return "No Repetition"

print(max_occur("Computer Science"))
print(max_occur("Edabit"))
print(max_occur("system admin"))
print(max_occur("the quick brown fox jumps over the lazy dog"))
print(max_occur("Computer ScienceComputer ScienceComputer ScienceComputer ScienceComputer ScienceComputer ScienceComputer ScienceComputer ScienceComputer Science"))
print(max_occur("edabitisawesomequickcountingmergebubbleinsertionselctionshellsortingbinarylinearsearch"))
print(max_occur("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog"))
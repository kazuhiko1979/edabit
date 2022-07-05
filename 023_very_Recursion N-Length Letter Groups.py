"""
Recursion: N-Length Letter Groups
Write a function that returns an array of strings populated from the slices of n-length characters of the given word (a slice after another while n-length applies onto the word).

Examples
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]

collect("strengths", 3)
➞ ["eng", "str", "ths"]

collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]
Notes
Ensure that the resulting array is lexicographically ordered.
Return an empty array if the given string is less than n.
"""

def collect(txt, num):

	if len(txt) < num:
		return []
	return sorted([txt[:num]] + collect(txt[num:], num))

print(collect("interctalontinenisationalism", 6))
print(collect("strengths", 3))
print(collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15))

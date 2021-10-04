"""
Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.

Examples
is_anagram("cristian", "Cristina") ➞ True

is_anagram("Dave Barry", "Ray Adverb") ➞ True

is_anagram("Nope", "Note") ➞ False
Notes
Should be case insensitive.
The two given strings can be of different lengths.
"""
def is_anagram(s1, s2):

    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("cristian", "Cristina"))
print(is_anagram("Dave Barry", "Ray Adverb"))
print(is_anagram("Nope", "Note"))





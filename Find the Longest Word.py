"""
Write a function that will return the longest word in a sentence. In cases where more than one word is found, return the first one.

Examples
find_longest("A thing of beauty is a joy forever.") ➞ "forever"

find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"

find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"
Notes
Special characters and symbols don't count as part of the word.
Return the longest word found in lowercase letters.
A recursive version of this challenge can be found via this link.
"""
import re


def find_longest(sentence):

    return max((re.split(r'\W', sentence)), key=len).lower()

print(find_longest("A thing of beauty is a joy forever."))
print(find_longest("Forgetfulness is by all means powerless!"))
print(find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel."))

print(find_longest("Hello darkness my old friend."))
print(find_longest("Yourself is your soul's captain and fate's master."))

# actual_param, expected_param = [
#   "Hello darkness my old friend.", "Yourself is your soul's captain and fate's master.",
#   "The pretty daughter's toy, a doll, is as pretty as her.",
#   "A thing of beauty is a joy forever.", "Forgetfulness is by all means powerless!",
#   "Strengths is the longest and most commonly used word that contains only a single vowel."
# ], [
#   "darkness", "yourself", "daughter", "forever", "forgetfulness", "strengths"
# ]
# for i, s in enumerate(actual_param):
#
# print(find_longest(s), expected_param[i])







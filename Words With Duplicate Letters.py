"""
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".
Notes
Letter matches are case-insensitive.
"""
from collections import Counter


def no_duplicate_letters(phrase):


    wordlist = phrase.split()
    # print(wordlist)
    for word in wordlist:
        if len(word) > len(set(word)):
            return False
    return True


print(no_duplicate_letters("Fortune favours the bold."))
print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap."))



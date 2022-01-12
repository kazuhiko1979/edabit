"""
House of Cards
The image below shows a sequence of larger and larger houses of cards, with the total number of cards included for each:

House of Cards

Given the tower height n, return the number of cards needed to construct a full house of cards.

Examples
cards_needed(3) ➞ 15

cards_needed(4) ➞ 26

cards_needed(0) ➞ 0
Notes
The height should always be equal or greater than 0. Return "invalid" if the value given doesn't abide by this rule.
"""

# Therefore the number of cards needed for building a House of Cards of N levels will be:
#  n*(3*n+1)/2

def cards_needed(n):

    return 'invalid' if n < 0 else n * (3*n+1) / 2

print(cards_needed(3))
print(cards_needed(4))
print(cards_needed(0))
print(cards_needed(-1))
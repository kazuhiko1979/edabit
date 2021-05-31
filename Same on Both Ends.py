"""
Given a sentence, return the number of words which have the same first and last letter.

Examples
count_same_ends("Pop! goes the balloon") ➞ 1

count_same_ends("And the crowd goes wild!") ➞ 0

count_same_ends("No I am not in a gang.") ➞ 1
Notes
Don't count single character words (such as "I" and "A" in example #3).
The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
Mind the punctuation!
Bonus points indeed for using regex!
"""


def count_same_ends(txt):

    count = 0

    for i in txt.split():
        i = ''.join(filter(str.isalnum, i))
        if len(i) > 1 and i[0].lower() == i[-1]:
            count += 1
    return count

print(count_same_ends("Pop! goes the balloon"))
print(count_same_ends("And the crowd goes wild!"))
print(count_same_ends("No I am not in a gang."))





"""
Abbreviating a Sentence
Create a function which takes a sentence and returns its abbreviation. Get all of the words over or equal to n characters in length and return the first letter of each, capitalised and overall returned as a single string.

Examples
abbreviate("do it yourself") ➞ "Y"

abbreviate("do it yourself", 2) ➞ "DIY"
# "do" and "it" are included because the second parameter specified that word lengths 2 are allowed.

abbreviate("attention AND deficit OR hyperactivity THE disorder") ➞ "ADHD"
# Words below the default 4 characters are not included in the abbreviation.

abbreviate("the acronym of long word lengths", 5) ➞ "AL"
# "acronym" and "lengths" have 5 or more characters.
Notes
There may not be an argument given for n so set the default to 4.
"""

# def abbreviate(sentence, n=4):
#
#     # return ''.join([i[0].upper() for i in sentence.split() if len(i) >= n])
#
#     return ''.join([i[0] for i in sentence.split() if len(i) >= n]).upper()

# lambda
abbreviate = lambda sentence, n=4: "".join(i[0].upper()*(len(i) >= n) for i in sentence.split())




# def abbreviate(sentence, *n):

    # result = ""
    # if not n:
    #     n = 4
    #     for i in sentence.split():
    #         if len(i) >= n:
    #             result += i.capitalize()[0]
    #     return result
    #
    # else:
    #     for x in sentence.split():
    #         if len(x) >= n[0]:
    #             result += x.capitalize()[0]
    #     return result

print(abbreviate("do it yourself"))
print(abbreviate("do it yourself", 2))
print(abbreviate("attention AND deficit OR hyperactivity THE disorder"))


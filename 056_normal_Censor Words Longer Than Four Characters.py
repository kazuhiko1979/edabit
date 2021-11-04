"""
Create a function that takes a string and censors words over four characters with *.

Examples
censor("The code is fourty") ➞ "The code is ******"

censor("Two plus three is five") ➞ "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word.
"""

def censor(s):

    # return ' '.join(['*' * len(i) if len(i) > 4 else i for i in s.split()])

    # for i in s.split():
    #     if len(i) > 4:
    #         s = s.replace(i, "*" * len(i))
    # return s


    # res = []
    # for word in list(s.split(" ")):
    #     if len(word) < 5:
    #         res.append(word)
    #     else:
    #         res.append(len(word) * "*")
    # return ' '.join(res)

print(censor("The code is fourty"))
print(censor("Two plus three is five"))


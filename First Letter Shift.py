"""
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).

Examples
shift_sentence("create a function") ➞ "freate c aunction"

shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

shift_sentence("edabit") ➞ "edabit"
Notes
The last word shifts its first letter to the first word in the sentence.
All sentences will be given in lowercase.
Note how single words remain untouched (example #4).
"""


def shift_sentence(txt):


    # txt = txt.split(" ")
    # top_txt = [i[0] for i in txt]
    #
    # if len(set(top_txt)) == 1:
    #     return ' '.join(txt)
    #
    # else:
    #     top_txt = top_txt[-1:] + top_txt[:-1]
    #     res = []
    #     for i, k in zip(txt, top_txt):
    #         i = i.strip(i[0])
    #         i = str(k) + i
    #         res.append(i)
    #
    #     return ' '.join(res)

    words = txt.split()
    return ' '.join([a[0] + b[1:] for a, b in zip(words[-1:] + words[:-1], words)])

print(shift_sentence("create a function"))
print(shift_sentence("it should shift the sentence"))
print(shift_sentence("the output is not very legible"))
print(shift_sentence("where is the butter"))
print(shift_sentence("she sells sea shells"))
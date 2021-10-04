"""
Create a function that, given a phrase and a number of letters guessed,
returns a string with hyphens - for every letter of the phrase not guessed,
and each letter guessed in place.

Examples
hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"

hangman("tree", ["r", "t", "e"]) ➞ "tree"

hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"

hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"

Notes
The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
All characters other than letters should always be returned (see example #4).
"""


def hangman(phrase, lst):

    # return ''.join([i if i.lower() in lst or not i.isalpha() else '-' for i in phrase])

    tmp = []
    for i in phrase:
        if i.lower() in lst or not i.isalpha():
            tmp.append(i)
        else:
            tmp.append("-")

    return ''.join(tmp)

# tmp_num = []
# tmp_word = []
#
# def hangHelper(tmp_num, tmp_word, phrase):
#
#     phrase = (["-" if i != " " else " " for i in phrase])
#
#     if tmp_num:
#         for num in range(0, len(tmp_num)):
#             phrase[tmp_num[num]] = tmp_word[num]
#             # print(phrase)
#         phrase = ''.join(phrase)
#         tmp_num[:] = []
#         tmp_word[:] = []
#         return phrase
#
#     elif tmp_num == []:
#         return ''.join(phrase)
#
#
# def hangmanTailer(phrase, index_phrase, lst):
#
#     pattern = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", "."]
#
#     if len(phrase) > index_phrase:
#         if phrase[index_phrase].lower() in lst:
#             tmp_num.append(index_phrase)
#             tmp_word.append(phrase[index_phrase])
#         elif phrase[index_phrase] in pattern:
#             tmp_num.append(index_phrase)
#             tmp_word.append(phrase[index_phrase])
#         return hangmanTailer(phrase, index_phrase+1, lst)
#
#     return hangHelper(tmp_num, tmp_word, phrase)
#
#
# def hangman(phrase, lst):
#
#     index_phrase = 0
#
#     return hangmanTailer(phrase, index_phrase, lst)




print(hangman("Looney Tunes", ["a", "e", "i", "o", "u"]))
print(hangman("summer", ["f", "l", "i"]))
print(hangman("Connect-4", ["c", "e", "e"]))
print(hangman("thE elePhaNt IN the rOom.", ["o", "g", "g", "m", "h","n","p"]))
print(hangman("deoxyribonucleic acid", []))
print(hangman("IM YELLING!", ["m", "y", "i", "l", "g"]))
print(hangman("Show me the money", ["a", "f", "u", "r", "q"]))
print(hangman("peter pan", ["e", "r", "p", "n", "n", "a", "t"]))
"""
Create a function that takes in two words as input and returns a list of three elements, in the following order:

Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element should have unique letters, and have each letter be alphabetically sorted.

Examples
letters("sharp", "soap") ➞ ["aps", "hr", "o"]

letters("board", "bored") ➞ ["bdor", "a", "e"]

letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]

letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should
# only exist a single "f" in your first element.

letters("match", "ham") ➞ ["ahm", "ct", ""]
# "ham" does not contain any letters that are not found already
# in "match".
"""


def letters(word1, word2):

    txt_1_list = []
    txt_2_list = []

    result = []

    for i in word1:
        txt_1_list.append(i)

    for j in word2:
        txt_2_list.append(j)

    intersection = ''.join(sorted(list(set(txt_1_list) & set(txt_2_list))))
    letters_unique_1 = ''.join(sorted(list(set(txt_1_list).difference(set(txt_2_list)))))
    letters_unique_2 = ''.join(sorted(list(set(txt_2_list).difference(set(txt_1_list)))))

    result.append(intersection)
    result.append(letters_unique_1)
    result.append(letters_unique_2)

    return result

print(letters("sharp", "soap"))
print(letters("board", "bored"))
print(letters("happiness", "envelope"))
print(letters("kerfuffle", "fluffy"))
print(letters("match", "ham"))




"""
Please help me unmix these strings!

Somehow my strings have all become mixed up; every pair of characters has been swapped. Help me undo this so I can understand my strings again.

Examples
unmix("123456") ➞ "214365"

unmix("hTsii  s aimex dpus rtni.g") ➞ "This is a mixed up string."

unmix("badce") ➞ "abcde"
Notes
The length of a string can be odd — in this case the last character is not altered (as there's nothing to swap it with).
"""


def unmix(txt):

    # tmp = []
    # tmp_2 = []
    #
    # for i in range(0, len(txt), 2):
    #     tmp.append(txt[i])
    #
    # for j in range(1, len(txt), 2):
    #     tmp_2.append(txt[j])
    #
    # if len(tmp) > len(tmp_2):
    #     tmp_2.append(' ')
    #
    # result = []
    #
    # for i in zip(tmp_2, tmp):
    #     result.append(i)
    #
    # strings = ''.join([str(x) for t in result for x in t])
    #
    # if '!' in strings:
    #     return strings
    # if '?' in strings:
    #     return strings
    # if '.' in strings:
    #     return strings
    #
    # return ''.join([str(x) for t in result for x in t]).replace(' ', '')

    txt1 = ''
    for i in range(0, len(txt), 2):
        txt1+=(txt[i:i+2])[::-1]
    return txt1


print(unmix("hTsii  s aimex dpus rtni.g"))
print(unmix("badce"))
print(unmix("123456"))
print(unmix(' Imaf eeilgna l tilt eidzz!y'))
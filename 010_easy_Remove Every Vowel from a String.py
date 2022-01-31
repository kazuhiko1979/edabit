"""
文字列からすべての母音（Vowel：バウル）を削除する関数

例：
remove_vowels("I have never seen a thin person drinking Diet Coke.")
➞ " hv nvr sn  thn prsn drnkng Dt Ck."

remove_vowels("We're gonna build a wall!")
➞ "W'r gnn bld  wll!"

remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"
"""

# aiueo AIUEO

def remove_vowels(txt):

    return ''.join([x for x in txt if x not in "aiueoAIUEO"])

    # by append
    # res = []
    # for i in txt:
    #     if i not in "aiueoAIUEO":
    #         res.append(i)
    # return ''.join(res)


    # by replace
    # v = "aiueoAIUEO"
    # for i in txt:
    #     if i in v:
    #         txt = txt.replace(i, "")
    # return txt

print(remove_vowels("I have never seen a thin person drinking Diet Coke."))
print(remove_vowels("We're gonna build a wall!"))
print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
)
















# def remove_vowels(txt):

    # by not append and replace
    # return ''.join([x for x in txt if x not in "aeiouAEIOU"])

    # by append

    # res = []
    # for i in txt:
    #     if i not in 'AIUEOaiueo':
    #         res.append(i)
    # return ''.join(res)

    # by replace

    #     s = "ueoaiUEOAI"
    #     for i in txt:
    #         if i in s:
    #             txt = txt.replace(i, "")
    #     return txt


# table = str.maketrans(dict.fromkeys('AIUEOaiueo'))
# return txt.translate(table)


# print(remove_vowels("I have never seen a thin person drinking Diet Coke."))
# print(remove_vowels("We're gonna build a wall!"))
# print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!"))







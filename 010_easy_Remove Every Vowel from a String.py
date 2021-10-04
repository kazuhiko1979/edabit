"""
remove_vowels("I have never seen a thin person drinking Diet Coke.")
➞ " hv nvr sn  thn prsn drnkng Dt Ck."

remove_vowels("We're gonna build a wall!")
➞ "W'r gnn bld  wll!"

remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"
Notes
"y" is not considered a vowel.
Expect a valid string for all test cases.
"""

def remove_vowels(txt):

    table = str.maketrans(dict.fromkeys('AIUEOaiueo'))
    return txt.translate(table)

    # res = []
    # for i in txt:
    #     if i not in 'AIUEOaiueo':
    #         res.append(i)
    # return ''.join(res)


print(remove_vowels("I have never seen a thin person drinking Diet Coke."))
print(remove_vowels("We're gonna build a wall!"))
print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!"))







"""Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
"""
def replace_vowels(txt, ch):

    # vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 'aeiou'

    for i in txt:
        if i in vowels:
            txt = txt.replace(i, ch)
    return txt

# 	return ''.join([i if i not in 'aeoui' else ch for i in txt])


print(replace_vowels("the aardvark", "#"))

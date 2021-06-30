"""
Create a function which takes every letter in every word, and puts it in alphabetical order. Note how the original word lengths must stay the same.

Examples
true_alphabetic("hello world") ➞ "dehll loorw"

true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"

true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"
Notes
All sentences will be in lowercase.
No punctuation or numbers will be included in the Tests.
"""


def true_alphabetic(txt):

    lst_space = ([num for num, val in enumerate(txt) if val in ' '])
    txt = sorted(''.join(txt.split(' ')))
    [txt.insert(num, ' ') for num, val in enumerate(txt) if num in lst_space]

    return ''.join(txt)


print(true_alphabetic("hello world"))
print(true_alphabetic("have a nice day"))
print(true_alphabetic("i love to code"))




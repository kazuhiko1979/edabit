"""
Remove Repeated Letters
Create a function that replaces all consecutively repeated letters in a word with single letters.

Examples
remove_repeats("aaabbbccc") ➞ "abc"

remove_repeats("bookkeeper") ➞ "bokeper"

remove_repeats("nananana") ➞ "nananana"
"""
from itertools import groupby
import re

def remove_repeats(txt):


    return re.sub(r'(\w)\1+', r'\1', txt)


    # return ''.join([k  for k, g in groupby(txt)])


    # new = ""
    # for i in range(len(txt)-1):
    #     if txt[i+1] != txt[i]:
    #         new += txt[i]
    # return new + txt[-1]




    # res = []
    # index = 0
    # res.append(txt[index])
    #
    # while index < len(txt):
    #     try:
    #         if txt[index] != txt[index+1]:
    #             res.append(txt[index+1])
    #             index += 1
    #         else:
    #             index += 1
    #     except:
    #         break
    # return ''.join(res)


print(remove_repeats("aaabbbccc"))
print(remove_repeats("bookkeeper"))
print(remove_repeats("nananana"))
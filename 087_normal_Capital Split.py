"""
Capital Split
Create a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.

Examples
cap_space("helloWorld") ➞ "hello world"

cap_space("iLoveMyTeapot") ➞ "i love my teapot"

cap_space("stayIndoors") ➞ "stay indoors"
Notes
The first letter will stay uncapitalized.
"""
import re


def cap_space(txt):

    # return "".join(" " + s if s.isupper() else s for s in txt).lower()

    return re.sub('([A-Z])', r' \1', txt).lower()



    # res = ""
    #
    # for i in txt:
    #     if i.islower():
    #         res += i
    #     if i.isupper():
    #         i = " " + i.lower()
    #         res += i
    # return res


print(cap_space("helloWorld"))
print(cap_space("iLoveMyTeapot"))
print(cap_space("stayIndoors"))


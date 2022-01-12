"""
Capitalize the Last Letter
Create a function that capitalizes the last letter of every word.

Examples
cap_last("hello") ➞ "hellO"

cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"

cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"
Notes
There won't be any cases of punctuation in the tests.
"""
import re

def cap_last(str):

    # return ' '.join([i[:-1] + i[-1].upper() for i in str.split()])

    return re.sub(r'(\w)(\s|\Z)', lambda x: x.group(0).upper(), str)



    # tmp = []
    #
    # for i in str.split():
    #     bottom = i[-1].upper()
    #     i = i[:-1]
    #     i = i + bottom
    #     tmp.append(i)
    # return ' '.join(tmp)


print(cap_last("hello"))
print(cap_last("My Name Is Edabit"))
print(cap_last("HELp THe LASt LETTERs CAPITALISe"))


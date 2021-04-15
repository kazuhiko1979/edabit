"""
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""
def censor_string(txt, lst, char):

    for i in lst:
        if i in txt:
            txt = txt.replace(i, len(i)*char)
    return txt


    # txt = txt.lower()
    # txt_splitted = list(map(lambda x: x.strip(' .m!?'), txt.split()))
    #
    # for i in txt_splitted:
    #     if i in list(map(str.lower, lst)):
    #         new_char = len(i) * char
    #         txt_splitted = txt.replace(i, new_char)
    #
    # return txt_splitted.capitalize()

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
print(censor_string("How do I stop myself from using python!?", ["do", "stop", "using"], "-"))


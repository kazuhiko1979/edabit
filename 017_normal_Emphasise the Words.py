"""
The challenge is to recreate the functionality of the title() method into a function called emphasise(). The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.

Examples
emphasise("hello world") ➞ "Hello World"

emphasise("GOOD MORNING") ➞ "Good Morning"

emphasise("99 red balloons!") ➞ "99 Red Balloons!"
Notes
You won't run into any issues when dealing with numbers in strings.
Please don't use the title() method directly :(
"""


def emphasise(txt):

    txt = [i.lower() for i in txt.split()]
    txt = [i[0].upper() + i[1:] for i in txt]

    return ' '.join(txt)


print(emphasise("hello world"))
print(emphasise("GOOD MORNING"))
print(emphasise("99 red balloons!"))
print(emphasise("1 2 3 4 5 6 7 8 9"))
print(emphasise(""))
print(emphasise("joshua senoron"))


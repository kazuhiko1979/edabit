"""
Create a function based on the input and output. Look at the examples, there is a pattern.

Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"
Notes
Input is a string.
"""

def secret(txt):

    txt = [s for s in txt.split('.')]

    name_cls = txt[0]
    list_cls = ' '.join(txt[1:])

    return "<{} class='{}'></{}>".format(name_cls, list_cls, name_cls)


print(secret("p.one.two.three"))
print(secret("h3.one"))
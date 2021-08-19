"""
In this exercise you will have to:

Take a list of names.
Add "Hello" to every name.
Make one big string with all greetings.
The solution should be one string with a comma in between every "Hello (Name)".

Examples
greet_people(["Joe"]) ➞ "Hello Joe"

greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"

greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"
"""


def greet_people(names):

    return ', '.join(["Hello {}".format(name) for name in names])


print(greet_people(["Joe"]))
print(greet_people(["Angela", "Joe"]))
print(greet_people(["Frank", "Angela", "Joe"]))
"""
Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
Write a function that takes in a name and returns a name tag, that should read:

"Hi! I'm [name], and I'm from [country]."
If the name is not in the dictionary, return:

"Hi! I'm a guest."
Examples
greeting("Randy") ➞ "Hi! I'm Randy, and I'm from Germany."

greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."

greeting("Monti") ➞ "Hi! I'm a guest."
"""

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}

def greeting(name):

    return "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name]) \
        if name in GUEST_LIST.keys() else "Hi! I'm a guest."

    # if name in GUEST_LIST.keys():
    #     country = ''.join([val for key, val in GUEST_LIST.items() if key == name])
    #     return 'Hi! I\'m {}, and I\'m from {}.'.format(name, country)
    # else:
    #     return "Hi! I'm a guest."



print(greeting("Randy"))
print(greeting("Sam"))
print(greeting("Monti"))


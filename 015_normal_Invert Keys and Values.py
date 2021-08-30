"""
Write a function that inverts the keys and values of a dictionary.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""

def invert(dct):

    # good solutions
    return {y : x for x, y in dct.items()}

    # My solutions
    # new_dic = {}
    #
    # for keys, values in dct.items():
    #     new_dic[values] = keys
    #
    # return new_dic


print(invert({"a": 1, "b": 2, "c": 3}))

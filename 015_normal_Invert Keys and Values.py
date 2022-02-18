"""
辞書のキーと値を反転する関数を作成します。

例：
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""

def invert(dct):

    return {value: key for key, value in dct.items()}

    # return {value: key for key, value in zip(dct.keys(), dct.values())}


    # new_dic = {}
    # for key, value in dct.items():
    #     new_dic[value] = key
    # return new_dic
        # print(value, key)


print(invert({ "a": 1, "b": 2, "c": 3 }))
print(invert({ "zebra": "koala", "horse": "camel" }))





































# """
# Write a function that inverts the keys and values of a dictionary.
#
# Examples
# invert({ "z": "q", "w": "f" })
# ➞ { "q": "z", "f": "w" }
#
# invert({ "a": 1, "b": 2, "c": 3 })
# ➞ { 1: "a", 2: "b", 3: "c" }
#
# invert({ "zebra": "koala", "horse": "camel" })
# ➞ { "koala": "zebra", "camel": "horse" }
# """
#
# def invert(dct):
#
#
#     return {y : x for x, y in zip(dct.keys(), dct.values())}
#
#     # return {y : x for x, y in dct.items()}
#
#
#     # My solutions
#     # new_dic = {}
#     #
#     # for keys, values in dct.items():
#     #     new_dic[values] = keys
#     #
#     # return new_dic
#
# print(invert({"z": "q", "w": "f"}))
# print(invert({"a": 1, "b": 2, "c": 3}))
# print(invert({ "zebra": "koala", "horse": "camel" }))

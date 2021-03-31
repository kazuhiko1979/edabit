"""
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
Notes
This is an oversimplification of the English language so no edge cases will appear.
Only focus on whether or not to add an s to the ends of words.
All tests will be valid.
"""

import collections


def pluralize(lst):

    dic = collections.Counter(lst)

    # pluralize_list = []
    #
    # for i, j in dic.items():
    #     if j > 2:
    #         i = i + 's'
    #         pluralize_list.append(i)
    #     else:
    #         pluralize_list.append(i)
    #
    # return set(pluralize_list)

    return set([i + "s" if j >= 2 else i for i, j in dic.items()])

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))
print(pluralize(["set", "set", "tuple", "tuple", "string", "string", "string", "string", "integer"]))



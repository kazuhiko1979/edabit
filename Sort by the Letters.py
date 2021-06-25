"""
Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).

Examples
sort_by_letter(["932c", "832u32", "2344b"])
➞ ["2344b", "932c", "832u32"]

sort_by_letter(["99a", "78b", "c2345", "11d"])
➞ ["99a", "78b", "c2345", "11d"]

sort_by_letter(["572z", "5y5", "304q2"])
➞ ["304q2", "5y5", "572z"]

sort_by_letter([])
➞ []
Notes
Each string will only have one (lowercase) letter.
If given an empty list, return an empty list.
"""

import re

def sort_by_letter(lst):

    return sorted(lst, key=lambda x: "".join(i for i in x if i.isalpha()))

    # alpha_list = [re.sub(r"[^a-zA-Z]", "", s) for s in lst]
    #
    # strings_dict = dict(zip(alpha_list, lst))
    # list = sorted(strings_dict.items())
    # strings_dict.clear()
    # strings_dict.update(list)
    # # return strings_dict.values()
    # return [i for i in strings_dict.values()]

# 辞書型だと、正確なソート結果にならないため、テスト結果はFailになります。


print(sort_by_letter(["932c", "832u32", "2344b"]))
print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
print(sort_by_letter(["572z", "5y5", "304q2"]))

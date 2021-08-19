"""
Write a function that transforms a list of characters into a list of dictionaries, where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

to_dict(["^"]) ➞ [{"^": 94}]

to_dict([]) ➞ []
"""

def to_dict(lst):

    list_master = []

    for cha in lst:
        tmp_code = {}

        if cha == "":
            return []

        tmp_code[cha] = ord(cha)
        list_master.append(tmp_code)
    return list_master

print(to_dict(["a", "b", "c"]))
print(to_dict(["!", ".", "?"]))
print(to_dict(["^"]))
print(to_dict([" "]))
print(to_dict([]))



"""
Create a function that takes a list of non-negative integers and
strings and return a new list without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
"""
from typing import List


# def filter_list(lst):
def filter_list(lst: list) -> List[int]:

    for i in lst[:]:
        if type(i) != int:
            lst.remove(i)
    return lst

print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))


"""
In mathematics, interval is the difference between the largest number
and the smallest number in a list.

To illustrate:

A = (3, 5, 7, 23, 11, 42, 80)

Interval of A = 80 - 3 = 77
Create a function that takes a list and returns ":)" if the interval of the list is
equal to any other element; otherwise return ":(".

Examples
face_interval([1, 2, 5, 8, 3, 9]) ➞ ":)"
# List interval is equal to one of the other elements.

face_interval([5, 2, 8, 3, 11]) ➞ ":("
# List interval is not among the other elements.

face_interval("bruh") ➞ ":/"
# "bruh" is not a list. It's string.
"""


def face_interval(num):
    if isinstance(num, list):
        interval = max(num) - min(num)
        # print(interval)
        if interval in num:
            return ":)"
        return ":("
    else:
        return ":/"


print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval("bruh"))


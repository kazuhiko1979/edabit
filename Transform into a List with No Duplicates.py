"""
A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.

[1, 3, 3, 5, 5, 5]
# original list

[1, 3, 5]
# original list transformed into a set
Create a function that sorts a list and removes all duplicate items from it.

Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
"""
def setify(lst):

    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return sorted(result)


print(setify([1, 3, 3, 5, 5]))
print(setify([4, 4, 4, 4]))
print(setify([5, 7, 8, 9, 10, 15]))
print(setify([3, 3, 3, 2, 1]))
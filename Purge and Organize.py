"""
Given a list of numbers, write a function that returns a list that...

Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
"""
def unique_sort(lst):

    result = []
    for i in lst:
        if i not in result:
            result.append(i)
            result.sort()
    return result


print(unique_sort([1, 2, 4, 3]))
print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
print(unique_sort([6, 7, 3, 2, 1]))





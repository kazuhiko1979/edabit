"""
Free Range
Create a function which converts an ordered number list into a list of ranges (represented as strings). Note how some lists have some numbers missing.

Examples
numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]

numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]

numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]

numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]
Notes
If there are no numbers consecutive to a number in the list, represent it as only the string version of that number (see example #4).
Return an empty list if the given list is empty.
"""


def numbers_to_ranges(lst):
    if not lst:
        return lst

    result = []
    start = lst[0]
    end = lst[0]

    for num in lst[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = end = num

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    return result


print(numbers_to_ranges([1, 2, 3, 4, 5]))
print(numbers_to_ranges([3, 4, 5, 10, 11, 12]))
print(numbers_to_ranges([1, 2, 3, 4, 99, 100]))
print(numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]))


# def numbers_to_ranges(lst):
#
#     if not lst:
#         return lst
#
#     result = []
#     sub = []
#     index = 0
#
#     while len(lst) > 1:
#
#       if abs(lst[index] - lst[index + 1]) == 1:
#           sub.append(lst[index])
#           lst = lst[1:]
#       else:
#           sub.append(lst[index])
#           result.append(sub)
#           lst = lst[1:]
#           sub = []
#
#     sub.append(lst[-1])
#     result.append(sub)
#
#
#     return ['{}-{}'.format(lst[0], lst[-1]) if len(lst) > 1 else str(lst[0]) for lst in result]


print(numbers_to_ranges([1, 2, 3, 4, 5]) )
print(numbers_to_ranges([3, 4, 5, 10, 11, 12]))
print(numbers_to_ranges([1, 2, 3, 4, 99, 100]))
print(numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]))


print(numbers_to_ranges([6, 7, 8, 10, 11, 12]))
print(numbers_to_ranges([1]))
print(numbers_to_ranges([3, 4, 5, 10, 11, 12]))
print(numbers_to_ranges([]))

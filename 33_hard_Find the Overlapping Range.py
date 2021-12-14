"""
Find the Overlapping Range
For a list of ranges, find the maximum range that is contained in all the ranges. If there is no such range, return "No overlapping".

Examples
overlapping([(1, 7), (2, 8), (0, 4)]) ➞ (2, 4)

overlapping([(5, 10), (2, 15), (10, 12)]) ➞ (10, 10)

overlapping([(11, 18), (3, 7), (2, 20), (5, 16)]) ➞ "No overlapping"
Notes
Both ends are inclusive for all ranges.
"""

def overlapping(lst):

    low = max([i[0] for i in lst])
    high = min([i[1] for i in lst])

    return (low, high) if high >= low else "NO overlapping"

    # head_min = min([i[0] for i in lst])
    # head_max = max([i[0] for i in lst])
    #
    # bottom_min = min([j[1] for j in lst])
    # bottom_max = max([j[1] for j in lst])
    #
    #
    # if head_min < head_max and bottom_min < bottom_max:
    #     if head_max <= bottom_min:
    #         return (head_max, bottom_min)
    #     return "No overlapping"


print(overlapping([(4, 24), (3, 10), (4, 18)]))
print(overlapping([(4, 9), (8, 22), (8, 24)]))
print(overlapping([(12, 16), (11, 20), (11, 24)]))
print(overlapping([(9, 13), (12, 17), (11, 23), (3, 21)]))
print(overlapping([(5, 9), (7, 8), (2, 11), (2, 12)]))
print(overlapping([(4, 18), (6, 17), (5, 8), (6, 16)]))
print(overlapping([(4, 9), (8, 22), (10, 24)]))
print(overlapping([(9, 11), (12, 17), (11, 23), (3, 21)]))
print(overlapping([(4, 24), (24, 25), (4, 30)]))
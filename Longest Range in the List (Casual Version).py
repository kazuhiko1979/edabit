"""
Given a list of integers, find the length of the longest range of consecutive integers that are contained in the sorted version of the list.

Here's an illustrative example. Consider the list:

[4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]
... which, after sorting, becomes:

[1, 3, 4, 5, 8, 9, 10, 11, 12, 17, 18, 20]
The longest consecutive subsequence is now clearly [8, 9, 10, 11, 12], which has length 5.

Examples
max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]) ➞ 5
# After sorting list becomes [1, 2, 4, 5, 8, 9, 10, 11, 12, 17, 18, 20]
# Longest consecutive subsequence is [8, 9, 10, 11, 12], which has length 5

max_consec([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]) ➞ 4
# After sorting get [1, 3, 4, 5, 7, 7, 7, 7, 11, 12, 12, 13, 14]
# Longest consecutive subsequence is [11, 12, 13, 14], which has length 4

max_consec([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 6
# After sorting get [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]
# Longest consecutive subsequence is [1, 2, 3, 4, 5, 6], which has length 6
Notes
As in the 2nd and 3rd examples, the given list is allowed to include repeated elements,
but such repetitions are ignored when finding the longest range of consecutive elements.
"""


def max_consec(arr):

    s = set()
    ans = 0

    for ele in arr:
        s.add(ele)

    for i in range(len(arr)):
        if (arr[i] - 1) not in s:

            j = arr[i]
            while (j in s):
                j += 1

            ans = max(ans, j - arr[i])
    return ans

print(max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]))
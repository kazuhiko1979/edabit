"""
Validate Subsequences
Given two non-empty lists, write a function that determines whether the second list is a subsequence of the first list.

For instance, the numbers [1, 3, 4] form a subsequence of the list [1, 2, 3, 4], and so do the numbers [2, 4].

Examples
is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) ➞ False

is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) ➞ True

is_valid_subsequence([1, 2, 3, 4], [2, 4]) ➞ True
"""

def is_valid_subsequence(lst, sub):
    # Initialize pointers for both lists
    lst_ptr = 0
    sub_ptr = 0

    # Iterate through the lists
    while lst_ptr < len(lst) and sub_ptr < len(sub):

        if lst[lst_ptr] == sub[sub_ptr]:
            sub_ptr += 1
        lst_ptr += 1

    return sub_ptr == len(sub)


# Test cases
print(is_valid_subsequence([1, 1, 6, 1], [1, 1, 1, 6]))  # ➞ False
print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))  # ➞ True
print(is_valid_subsequence([1, 2, 3, 4], [2, 4])) # ➞ True

"""
Circular Shift
Write a function that takes two lists (lst1 and lst2) and an int n, and returns True if the second list equals the first list shifted by n positions. Otherwise, return False.

Examples
circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2) ➞ True

circular_shift([1, 1], [1, 1], 6) ➞ True

circular_shift([0, 1, 2, 3, 4, 5], [3, 4, 5, 2, 1, 0], 3) ➞ False
Notes
The two lists will have the same length.
n can be a negative value.
"""

def circular_shift(lst1, lst2, n):

    return lst1 == lst2[n:] + lst2[:n]

    # if lst1 == lst2 and abs(n) >= len(lst1) or n == 0:
    #     return True
    # elif lst2[n] == lst1[n-n]:
    #     return True
    #
    # return False

print(circular_shift([1, 2, 3, 4],[3, 4, 1, 2],2))
print(circular_shift([1, 1],[1, 1],6))
print(circular_shift([0, 1, 2, 3, 4, 5],[3, 4, 5, 2, 1, 0],3))
print(circular_shift([0, 1, 2, 3],[1, 2, 3, 1],1))
print(circular_shift(list(range(32)), list(range(32)),0))
print(circular_shift([1, 2, 1],[1, 2, 1],3))
print(circular_shift([5, 7, 2, 3],[2, 3, 5, 7],-2))
print(circular_shift([2, 3, 5, 7, 87],[2, 3, 5, 7, 87],-4))





"""
Write four functions that directly mutate a list:

repeat(lst, n): Repeat lst n times.
add(lst, x): Adds x to the end of the lst.
remove(lst, m, n): Removes all elements between indices m and n inclusive in lst.
concat(lst, x): concatenates lst with x (another list).
Examples
lst = [1, 2, 3, 4]

repeat(lst, 3) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

add(lst, 1) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1]

remove(lst, 1, 12) ➞ [1]

concat(lst, [3, 4]) ➞ [1, 3, 4]
Notes
Your functions should mutate the list directly, not make a copy.
"""
lst = [1, 2, 3, 4]
n = 3



def repeat(lst, n):
    for i in lst * (n-1):
        lst.append(i)
    return lst


def add(lst, x):
    lst.append(x)
    return lst


def remove(lst, i, j):
    del lst[i:j+1]
    return lst

def concat(lst, lst2):
    lst+=lst2
    return lst

print(repeat(lst, 3))
print(add(lst, 1))
print(remove(lst, 1, 12))
print(concat(lst, [3, 4]))









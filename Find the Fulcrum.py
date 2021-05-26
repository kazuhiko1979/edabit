"""
A fulcrum of a list is an integer such that all elements to the left of it and all elements to the right of it sum to the same value. Write a function that finds the fulcrum of a list.

To illustrate:

find_fulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
// Since [3, 1, 5] and [4, 6, -1] both sum to 9
Examples
find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4

find_fulcrum([9, 1, 9]) ➞ 1

find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0

find_fulcrum([8, 8, 8, 8]) ➞ -1
"""

# list = [1, 2, 4, 9, 10, -10, -9, 3]
# list = [3, 1, 5, 2, 4, 6, -1]
# list = [9, 1, 9]
# list = [7, -1, 0, -1, 1, 1, 2, 3]
# list = [8, 8, 8, 8]

def find_fulcrum(lst):

    count=[]

    for i in range(0,len(lst)-1):
        if sum(lst[i:])==sum(lst[:i+1]):
            count.append(i)

    if len(count)==0:
        return -1
    else:
        return lst[count[0]]

print(find_fulcrum([3, 1, 5, 2, 4, 6, -1]))
print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
print(find_fulcrum([9, 1, 9]))
print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))




"""
Balanced List
Given a list of even length, copy the half with the higher sum of numbers to the other half of the list. If the sum of the first half equals the sum of the second half, return the original list.

Examples
balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
# 1 + 2 + 4 < 6 + 3 + 1 sol = [6, 3, 1, 6, 3, 1]

balanced([88, 3, 27, 5, 9, 0, 13, 10]) ➞ [88, 3, 27, 5, 88, 3, 27, 5]
# 88 + 3 + 27 + 5 > 9 + 0 + 13 + 10  sol = [88, 3 ,27 ,5 ,88 ,3 ,27 ,5]

balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]) ➞ [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
# 7 + 5 + 2 + 6 + 1 + 0 = 1 + 5 + 2 + 7 + 0 + 6 sol =  [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
Notes
The length of the list is even.
"""

def balanced(lst):

    h1, h2 = sorted((lst[:len(lst)//2], lst[len(lst)//2:]), key=sum)
    # print(h1, h2)
    return lst if sum(h1) == sum(h2) else h2*2

    # if len(lst) % 2 != 0:
    #     return None
    #
    # topHalfList = lst[0:int(len(lst)/2)]
    # buttomHalfList = lst[int(len(lst)/2):]
    #
    # if sum(topHalfList) < sum(buttomHalfList):
    #     return buttomHalfList * 2
    # if sum(topHalfList) > sum(buttomHalfList):
    #     return topHalfList * 2
    # else:
    #     return lst

print(balanced([1, 2, 4, 6, 3, 1]))
print(balanced([88, 3, 27, 5, 9, 0, 13, 10]))
print(balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]))
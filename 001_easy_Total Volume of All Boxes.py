"""
レベル：やさしい

ボックスが入ったリストを指定して、すべてのボックスを組み合わせた体積を返す関数を作成します。
ボックスは、長さ、幅、高さの3つの要素を持つリストで構成されています。

たとえば、total_volume([2,3,2],[6,6,7],[1,2,1])は、
（2 x 3 x 2）+（6 x 6 x 7）+（ 1 x 2 x 1）= 12 + 252 + 2 = 266。

例
total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]) ➞ 63

total_volume([2, 2, 2], [2, 1, 1]) ➞ 10

total_volume([1, 1, 1]) ➞ 1

備考：
少なくとも1つのボックスが与えられます。
各ボックスには常に3つの寸法が含まれます。
"""


def total_volume(*boxes):

    return sum([x * y * z for x, y, z in boxes])

    # vol = 0
    #
    # for box in boxes:
    #     vol += box[0] * box[1] * box[2]
    # return vol

print(total_volume([2,3,2],[6,6,7],[1,2,1]))
print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
print(total_volume([2, 2, 2], [2, 1, 1]))
print(total_volume([1, 1, 1]))































"""
Given a list of boxes, create a function that returns the total volume of all those boxes combined together. A box is represented by a list with three elements: length, width and height.

For instance, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1]) should return 266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.

Examples
total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]) ➞ 63

total_volume([2, 2, 2], [2, 1, 1]) ➞ 10

total_volume([1, 1, 1]) ➞ 1
Notes
You will be given at least one box.
Each box will always have three dimensions included.
"""

# from functools import reduce
#
#
# def total_volume(*boxes):
#
#     return sum(([reduce((lambda x, y: x * y), i) for i in boxes]))
#
# print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
# print(total_volume([5, 1, 10], [1, 9, 2]))





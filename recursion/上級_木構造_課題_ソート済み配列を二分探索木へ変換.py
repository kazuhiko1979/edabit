"""
ソート済み配列を二分探索木へ変換
easy
異なる整数値で構成されるソート済みのリスト numberList が与えられるので、平衡二分探索木を作成し、
その根ノードを返す、sortedArrToBST という関数を作成してください。


関数の入出力例

入力のデータ型： integer[] numberList

出力のデータ型： binaryTree<integer>

sortedArrToBST( [1,2,3] )--> [2,1,3]

sortedArrToBST( [1,2,3,5,6,9,10] )--> [5,2,9,1,3,6,10]

sortedArrToBST( [-1,0,3,10,13,19,22] )--> [10,0,19,-1,3,13,22]

sortedArrToBST( [1,3,4,5,8] )--> [4,1,5,null,3,null,8]

sortedArrToBST( [1,4,6,10,11,14,15,20,22,25,50,61,68,72] )--> [15,6,50,1,11,22,68,null,4,10,14,20,25,61,72]

ヒントを閉じる

中級コース / リスト / 分割統治法 、上級コース / 木構造 / 二分探索木(2) を復習しましょう。

"""

import math


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def sortedArrToBST(numberList):

    if not numberList:
        return None

    # find middle
    mid = (len(numberList) - 1) // 2

    # make the middle element the root
    root = BinaryTree(numberList[mid])
    # left subtree of root has all values < arr[mid]
    root.left = sortedArrToBST(numberList[:mid])

    # right subtree of root has all value > arr[mid]
    root.right = sortedArrToBST(numberList[mid+1:])

    return root









# def sortedArrToBST(numerList):
#     # 配列のstart, endを引数としてヘルパー関数を使います。
#     return sortedArrToBSTHelper(numerList, 0, len(numerList) - 1)


# def sortedArrToBSTHelper(list, start, end):
#     # ベースケースは要素が1つになった時
#     if start == end:
#         return BinaryTree(list[start])
#     # 配列の中心を決めます
#     mid = math.floor((start + end) / 2)
#
#     # startからmid-1までを左側、mid+1からendまでを右側の部分木にします。
#     left = None if start == mid else sortedArrToBSTHelper(list, start, mid - 1)
#     right = None if end == mid else sortedArrToBSTHelper(list, mid + 1, end)
#
#     # if start == mid:
#     #     left = None
#     # else:
#     #     sortedArrToBSTHelper(list, start, mid - 1)
#     #
#     # if end == mid:
#     #     right = None
#     # else:
#     #     sortedArrToBSTHelper(list, mid + 1, end)
#
#     # 配列の中心を根ノードとして、左右の部分木を合わせて新しいノードにします。
#     return BinaryTree(list[mid], left, right)


print(sortedArrToBST([1,2,3]))





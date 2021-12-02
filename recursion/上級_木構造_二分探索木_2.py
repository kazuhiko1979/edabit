"""
二分探索木の探索効率が最高になるのは、木の高さが最も低いケースです。つまり、根ノードから各葉までの高さができるだけ等しくなった場合であり、このような二分探索木は平衡二分探索木と呼ばれます。平衡二分探索木の計算量は O(
log
n
) になります。


平衡二分探索木を実装したデータ構造には、B 木、AA 木、AVL 木、赤黒木、Treap など数多く存在します。

平衡二分探索木を実装する 1 番簡単な方法は、ソート済みのリストを用意して、そこから再帰的に BST を構築することです。今回は set 型
（同じ値ではない要素のコレクション）を使います。リスト内に含まれる全ての要素が異なる値を取るので、
BST は一意のノードを持ち、順番通りに構築することができます。
同じ値の要素が複数あるケースを扱う場合は、スタックやリスト構造を使う必要があります。

では、ソート済みのリストを BST に移行するアルゴリズムを再帰的に実装していきます。
startIndex で始まり endIndex で終わる配列を入力として受け取り、中間の要素を根ノードに設定します。
その後、再帰関数を使って startIndex から mid-1 まで呼び出し左側の部分木として設定し、同様に mid+1 から endIndex までを右側の部分木として設定します。

sortedArrayToBST(arr, start, end)
要素が 1 つしかない場合は、それを根ノードとして設定します。
それ以外の場合は中間を floor((start+end)/2) とし、中間を根ノードとします。
左の BST を sortedArrayToBST(arr, start, mid-1) とし、右の BST を sortedArrayToBST(arr, mid+1,end) とします。

"""
# import math
#
# class BinaryTree:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         # 左の二分木
#         self.left = left
#         # 右の二分木
#         self.right = right
#
#
# def sortedArrayToBSTHelper(arr, start, end):
#     if start == end:
#         return BinaryTree(arr[start], None, None)
#
#     mid = math.floor((start+end / 2))
#
#     left = None
#     if mid-1 >= start:
#         left = sortedArrayToBSTHelper(arr, start, mid-1)
#
#     right = None
#     if mid-1 >= end:
#         right = sortedArrayToBSTHelper(arr, mid+1, end)
#
#     root = BinaryTree(arr[mid], left, right)
#
#     return root
#
#
# def sortedArrayToBST(nums):
#     if len(nums) == 0:
#         return None
#     return sortedArrayToBSTHelper(nums, 0, len(nums)-1)
#
# # balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
# # print(balancedBST)
#
# # BSTリストの中にキーが存在するかどうかによって、true、falseを返します。
# # 再帰
# # def keyExist(key, bst):
# #     if bst == None:
# #         return False
# #     if bst.data == key:
# #         return True
# #
# #     # 現在のノードよりキーが小さければ左に、大きければ右にめぐります。
# #     if bst.data > key:
# #         return keyExist(key, bst.left)
# #     else:
# #         return keyExist(key, bst.right)
#
# # BSTリストの中にキーが存在するかどうかによって、true、falseを返します。
# # イテレータ
# def keyExist(key, bst):
#     iterator = bst
#     while iterator is not None:
#         if iterator.data == key:
#             return True
#         # 現在のノードよりキーが小さければ左に、大きければ右に辿ります。
#         if iterator.data > key:
#             iterator = iterator.left
#         else:
#             iterator = iterator.right
#
#     return False
#
#
# balancedBST = sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# print(keyExist(6, balancedBST))
# print(keyExist(10, balancedBST))
# print(keyExist(45, balancedBST))

import math

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        # 左の二分木
        self.left = None
        # 右の二分木
        self.right = None

# BinarySearchTreeという構造体を作成してください。
class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(array):
        if len(array) == 0:
            return None
        return BinarySearchTree.sortedArrayToBSTHelper(array, 0, len(array)-1)


    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        if start == end:
            return BinaryTree(arr[start], None, None)

        mid = math.floor((start+end) / 2)

        left = None
        if mid-1 >= start:
            left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid-1)

        right = None
        if mid+1 <= end:
            right = BinarySearchTree.sortedArrayToBSTHelper(arr, mid+1, end)

        root = BinaryTree(arr[mid], left, right)
        return root

    def keyExist(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:
                return True
            if iterator.data > key:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return False

    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:
                return iterator
            if iterator.data > key:
                iterator = iterator.left
            else:
                iterator = iterator.right

        return None


balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
print(balancedBST.keyExist(6))
print(balancedBST.search(6).data)
print(balancedBST.keyExist(2))
print(balancedBST.search(2).data)
print(balancedBST.search(34))




"""
深さ優先走査(2)
前順走査、後順走査、逆間順走査をサポートするようにデータ構造を拡張してください。
"""

import math

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printPreOrder(self):
        self.preOrderwalk(self)
        print("")

    def printPostOrder(self):
        self.postOrderWalk(self)
        print("")

    def printReverseOrder(self):
        self.reverseOrderWalk(self)
        print("")

    # 前順 (pre-order) (NLR) 前順走査
    def preOrderwalk(self, tRoot):
        if tRoot is not None:
            print(str(tRoot.data), end=' ')
            self.preOrderwalk(tRoot.left)
            self.preOrderwalk(tRoot.right)

    # 後順（post-order）（LRN）後順走査
    def postOrderWalk(self, tRoot):
        if tRoot is not None:
            self.postOrderWalk(tRoot.left)
            self.postOrderWalk(tRoot.right)
            print(str(tRoot.data), end=' ')

    # 逆間順 (reverse-order) (RNL)
    def reverseOrderWalk(self, tRoot):
        if tRoot is not None:
            self.reverseOrderWalk(tRoot.right)
            print(str(tRoot.data), end= ' ')
            self.reverseOrderWalk(tRoot.left)


    def inOrderWalk(self, tRoot):
        if tRoot is not None:
            self.inOrderWalk(tRoot.left)
            print(str(tRoot.data), end=' ')
            self.inOrderWalk(tRoot.right)

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

        mid = math.floor((start + end) / 2)

        left = None

        if mid - 1 >= start:
            left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid-1)

        right = None

        if mid + 1 <= end:
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

        return None

    def printSorted(self):
        # self.root.printPostOrder()
        self.root.printReverseOrder()

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])

balancedBST.printSorted()
balancedBST2.printSorted()











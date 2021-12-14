"""
深さ優先走査(1)
二分木は、根ノード（N）、左（L）、右（R）の 3 つのノード値を持っており、再帰的に出力されます。
深さ優先走査では、ノードを調査する順序によって以下の 3 つに走査法が分類されます。
"""

import math

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printInOrder(self):
        self.inOrderWalk(self)
        print("")

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
        self.root.printInOrder()

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])

balancedBST.printSorted()
balancedBST2.printSorted()











"""
ST「挿入」
BST に値を挿入するには、BST のプロパティを維持する必要があります。
まずは、アルゴリズムのコンセプトを確認しましょう。

Insert(root, v) は、値 v および、根ルートを受け取り、v を挿入した新しい BST の
根ルートを返します。BST を辿りながら、各ノードで左に辿るか右に辿るかを判断して、v を挿入する葉ノードを見つけることを目的としています。
v が現在のノードの値よりも大きければ、右に辿り、値が小さい場合は、左に辿ります。


葉ノードに到達すると、この葉ノード p が v の親ノードとなり、v がその子ノードとなります。
v が親ノードより大きい場合は、v を p の右に挿入し、小さい場合は v を p の左に挿入します。

もし親ノードが存在しない場合、根ノードが空のノードであることを意味します。値 v は新しい BST の根ノードにならなければいけません。
"""

"""
では、実際に BST への挿入を実装してみましょう。
データ値を受け取り、BST プロパティを保持しながら BST に挿入する、insert(value) というメソッドを新たに追加し、BST のデータ構造を拡張してください。
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
        return BinarySearchTree.sortedArrayToBSTHelper(array, 0, len(array) - 1)

    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        if start == end:
            return BinaryTree(arr[start], None, None)

        mid = math.floor((start+end) / 2)

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

        return False

    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:
                return iterator
            if iterator.data > key:
                return iterator.left
            else:
                iterator.right

        return None


    def insert(self, value):
        iterator = self.root
        while iterator is not None:
            if iterator.data > value and iterator.left == None:
                iterator.left = BinaryTree(value)
            elif iterator.data < value and iterator.right == None:
                iterator.right = BinaryTree(value)
            iterator = iterator.left if iterator.data > value else iterator.right



    def printSorted(self):
        self.root.printInOrder()

balancedBST = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST.insert(5)
balancedBST.printSorted()
balancedBST.insert(47)
balancedBST.printSorted()
balancedBST.insert(0)
balancedBST.printSorted()














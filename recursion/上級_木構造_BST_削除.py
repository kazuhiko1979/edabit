import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
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
        if len(array) == 0: return None
        return BinarySearchTree.sortedArrayToBSTHelper(array, 0, len(array)-1)

    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        if start == end: return BinaryTree(arr[start], None, None)
        
        mid = math.floor((start+end)/2)
        
        left = None
        if mid-1 >= start: left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid-1)
        
        right = None
        if mid+1 <= end: right = BinarySearchTree.sortedArrayToBSTHelper(arr, mid+1, end)
        
        root = BinaryTree(arr[mid], left, right)
        return root

    def keyExist(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:return True
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right
        
        return False

    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key: return iterator
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right        
        return None

    def insert(self, value):
        iterator = self.root
        while iterator is not None:
            if iterator.data > value and iterator.left == None:
                iterator.left = BinaryTree(value)
            elif iterator.data < value and iterator.right == None:
                iterator.right = BinaryTree(value)    
            iterator = iterator.left if iterator.data > value else iterator.right    

    def transplant(self, nodeParent, node, target):
        if nodeParent == None: self.root = target
        elif nodeParent.left == node: nodeParent.left = target
        else: nodeParent.right = target

    def deleteNode(self, key):
        if self.root == None: return None
        node = self.search(key)
        if self.keyExist(key) == False: return self.root

        parent = self.findParent(node)
        # case 1: ノードNの左が空
        if node.left == None: self.transplant(parent, node, node.right)
        # case 2: ノードNの右が空
        elif node.right == None: self.transplant(parent, node, node.left)
        # case 3: 2つの子を持っている場合
        else:
            successor = self.findSuccessor(node)
            successorP = self.findParent(successor)

            # case 3 後続ノードSがすぐ右側にいる場合 : この場合、ノードNが後続ノードSの親になっているため、case4は必要ありません。単純にNの親であるPの部分木とSを移植すればokです。
            # 特別なケース (case 4) 後続ノードSがすぐ右側にいない場合 : この場合、後続Sの親も変更しなければいけません。
            if successor != node.right:
                # 後続ノードSをSの右部分木で移植します。Sをアップデートします。
                self.transplant(successorP, successor, successor.right)
                # Sの右側はノードNの右側になっている必要があります。
                successor.right = node.right

            # ノードNを後続Sで移植します。Sの左部分木をノードNの左部分木にします。
            self.transplant(parent, node, successor)
            successor.left = node.left   

    def findParent(self, node):
        iterator = self.root
        parent = None
        while iterator != node:
            parent = iterator
            iterator = iterator.left if iterator.data > node.data else iterator.right
        return parent

    def findSuccessor(self, node):
        # 部分木
        targetNode = node
        # keyがBST内に存在しない場合、nullを返します。
        if targetNode == None: return None
        # keyのノードの右にある最小値を探します。
        if targetNode.right != None: return self.minimumNode(targetNode.right)

        successor = None
        iterator = self.root

        while iterator != None:
            if targetNode.data == iterator.data: return successor
            # successorを左方向へずらしていきます。
            if targetNode.data < iterator.data and (successor == None or iterator.data < successor.data): successor = iterator
            if targetNode.data < iterator.data: iterator = iterator.left
            else: iterator = iterator.right
            
        return successor
    

    def minimumNode(self, node):
        iterator = node
        while iterator != None and iterator.left != None: iterator = iterator.left
        return iterator
    
    def printSorted(self):
        self.root.printInOrder()

balancedBST = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST.deleteNode(43)
balancedBST.printSorted()
balancedBST.deleteNode(7)
balancedBST.printSorted()
balancedBST.deleteNode(4)
balancedBST.printSorted()
balancedBST.deleteNode(1010)
balancedBST.printSorted()
# 存在しない0をdeleteNodeします。
balancedBST.deleteNode(0)
balancedBST.printSorted()
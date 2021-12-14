"""
二分探索木から削除
hard
異なる整数値で構成される二分探索木（BST）の根ノード root と整数 key が与えられるので、
BST から key を削除する bstDelete という関数を作成してください。もし key がすでに BST 内に存在しない場合は何も削除せず、
根ノードをそのまま返してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root, integer key

出力のデータ型： binaryTree<integer>

bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [0,-10,9,null,-3]

bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 20 )--> [0,-10,5,null,-3,null,9]

bstDelete( toBinaryTree([1,null,2]), 1 )--> [2]

bstDelete( toBinaryTree([5,3,6,2,4,null,7]), 3 )--> [5,4,6,2,null,null,7]

bstDelete( toBinaryTree([5,3,6,2,4,null,7]), 5 )--> [6,3,7,2,4]

bstDelete( toBinaryTree([5,3,6,2,4,null,7]), 15 )--> [5,3,6,2,4,null,7]

bstDelete( toBinaryTree([3,2]), 3 )--> [2]

bstDelete( toBinaryTree([1]), 0 )--> [1]

bstDelete( toBinaryTree([25,15,35,null,20,30,40]), 25 )--> [30,15,35,null,20,null,40]

bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 9 )--> [0,-10,5,null,-3]

bstDelete( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [0,-10,9,null,-3]

bstDelete( toBinaryTree([5,2,18,-4,3,null,null]), -4 )--> [5,2,18,null,3]
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def bstDelete(root, key):
    def removeNode(node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = removeNode(node.left, data)
            return node
        elif data > node.data:
            node.right = removeNode(node.right, data)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            minValue = minValueFromGivenNode(node.right)
            node.data = minValue
            node.right = removeNode(node.right, minValue)

        return node

    root = removeNode(root, key)
    return root


def minValueFromGivenNode(node):
    currentNode = node
    while currentNode.left:
        currentNode = currentNode.left
    return currentNode.data














#     def printInOrder(self):
#         self.inOrderWalk(self)
#         print("")
#
#     def inOrderWalk(self, tRoot):
#         if tRoot is not None:
#             self.inOrderWalk(tRoot.left)
#             print(str(tRoot.data), end=' ')
#             self.inOrderWalk(tRoot.right)
#
# def bstDelete(root, key):
#     if root is None:
#         return None
#
#     if key < root.data:
#         # 削除対象が自身より小さければ、左部分木から削除する
#         root.left = bstDelete(root.left, key)
#     elif key > root.data:
#         # 削除対象が自身より大きければ、右部分木をから削除する
#         root.right = bstDelete(root.right, key)
#     # 削除対象が自身と等しければ、自身を削除する
#     else:
#         # 子を持たない場合、自身をnullで置き換える
#         if root.left is None and root.right is None:
#             root = None
#         # 1つの子を持つ場合、自身をその子で置き換える
#         elif root.left is None and root.right is None:
#             root = root.left or root.right
#         else:
#             # 2つの子を持つ場合、自身をそのsuccessorの値で上書きし、元のsuccessorを削除する
#             root.data = successor(root)
#             root.right = bstDelete(root.right, root.data)
#
#         return root
#
#
#
# # nodeの右部分木からsuccessorの値を返す
# def successor(node):
#     node = node.right
#     while node.left:
#         node = node.left
#     return node.data







# def bstDelete(root, key):
#     def removeNode(node, data):
#         if node is None:
#             return node
#
#         if data < node.data:
#             node.left = removeNode(node.left, data)
#             return node
#         elif data > node.data:
#             node.right = removeNode(node.right, data)
#             return node
#         else:
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#
#             minValue = minValueFromGivenNode(node.right)
#             node.data = minValue
#             node.right = removeNode(node.right, minValue)
#
#         return node
#
#     root = removeNode(root, key)
#     return root
#
#
#
# def minValueFromGivenNode(node):
#     currentNode = node
#     while currentNode.left:
#         currentNode = currentNode.left
#     return currentNode.data







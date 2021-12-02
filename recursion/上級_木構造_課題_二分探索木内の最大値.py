"""
二分探索木内の最大値
easy
異なる整数値で構成される二分探索木（BST）の根ノード root が与えられるので、BST 内に存在する最大値を持つノードを返す、maximumNode という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： binaryTree<integer>

maximumNode( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [9]

maximumNode( toBinaryTree([5,3,6,2,4,null,7]) )--> [7]

maximumNode( toBinaryTree([5,3,7,2,4,6,9,null,null,null,null,null,null,8]) )--> [9,8]

maximumNode( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [25]

maximumNode( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [19]

maximumNode( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [19]

ヒントを閉じる

二分探索木は「左の子 ≤ 親 ≤ 右の子」という構造を持っています。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def maximumNode(root):

    iterator = root
    # 右側の子が null になるまで右に進めます
    while iterator.right != None:
        iterator = iterator.right

    # 右側の子がnullになったらノードを返します。
    return iterator

# def maximumNode(root):
#
#     iterator = root
#     while iterator.right:
#         iterator = iterator.right
#     return iterator











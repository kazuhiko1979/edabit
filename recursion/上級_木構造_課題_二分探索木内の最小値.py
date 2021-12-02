"""
二分探索木内の最小値
easy
異なる整数値で構成される二分探索木（BST）の根ノード root が与えられるので、BST 内に存在する最小値を持つノードを返す、minimumNode という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： binaryTree<integer>

minimumNode( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [-10,null,-3]

minimumNode( toBinaryTree([5,3,6,2,4,null,7]) )--> [2]

minimumNode( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [-18]

minimumNode( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10]

minimumNode( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [-9,null,-6]

ヒントを閉じる

二分探索木は「左の子 ≤ 親 ≤ 右の子」という構造を持っています。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimumNode(root):
    # ベースケース　左の子がnullになったらrootを返します。
    if root.left == None:
        return root
    # rootを左へ進めて再帰的に繰り返します。
    return minimumNode(root.left)


# def minimumNode(root):
#     # iteratorにrootを入れます。
#     iterator = root
#     # iterator と iterator.left が None になるまで左へ進めます。
#     while iterator != None and iterator.left != None:
#         iterator = iterator.left
#
#     # 左の子が None　になるノードが最小値です。
#     return iterator


# def minimumNode(root):
#     iterator = root
#     while iterator.left:
#         iterator = iterator.left
#     return iterator








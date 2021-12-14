"""
前順（二分木）
easy
整数で構成される二分木の根ノード root が与えられるので、前順を表す配列を返す、preOrderTraversal という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： integer[]

preorderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [0,-10,-3,5,9]

preorderTraversal( toBinaryTree([5,3,6,2,4,null,7]) )--> [5,3,2,4,6,7]

preorderTraversal( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [-2,-17,-18,-11,-4,8,3,19,25]

preorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [3,-3,-7,-10,-4,1,0,2,13,6,5,8,18,15,19]

preorderTraversal( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [1,-5,-9,-6,-4,0,15,10,14,17,16,19]

preorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [3,-3,-7,-10,-4,1,0,2,13,6,5,8,18,15,19]

ヒントを閉じる

上級コース / 木構造 / 深さ優先走査(1)(2) を復習しましょう。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorderTraversalHelper(root, arr):
    # ベースケース、根ノードがNoneになると終了します。
    if root is None:
        return None

    # 根ノードのdataをarrにappendします。
    arr.append(root.data)
    # 左側のノードへ移動します。
    preorderTraversalHelper(root.left, arr)
    # 右側のノードへ移動します。
    preorderTraversalHelper(root.right, arr)

    return arr

def preorderTraversal(root):
    # ヘルパー関数を使います。
    return preorderTraversalHelper(root, [])


print(preorderTraversal([0,-10,5,None,-3,None,9]))











# def preoderHelper(root, output):
#     if root is not None:
#         output.append(root.data)
#         preoderHelper(root.left, output)
#         preoderHelper(root.right, output)
#
#     return output
#
# def preorderTraversal(root):
#
#     return preoderHelper(root, [])

# ans = list()
#
# def preorderTraversal(root):
#     if root is not None:
#         ans.append(root.data)
#         preorderTraversal(root.left)
#         preorderTraversal(root.right)
#     return ans

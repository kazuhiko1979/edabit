"""
間順（二分木）
easy
整数で構成される二分木の根ノード root が与えられるので、間順を表す配列を返す、inorderTraversal という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： integer[]

inorderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [-10,-3,0,5,9]

inorderTraversal( toBinaryTree([5,3,6,2,4,null,7]) )--> [2,3,4,5,6,7]

inorderTraversal( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [-18,-17,-11,-4,-2,3,8,19,25]

inorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10,-7,-4,-3,0,1,2,3,5,6,8,13,15,18,19]

inorderTraversal( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [-9,-6,-5,-4,0,1,10,14,15,16,17,19]

inorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10,-7,-4,-3,0,1,2,3,5,6,8,13,15,18,19]
"""


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorderTraversalHelper(root, arr):
    # ベースケース、根ノードがNoneになると終了します。
    if root is None:
        return None

    # 根ノードのdataをarrにappendします。
    arr.append(root.data)

    # 右側のノードへ移動します。
    inorderTraversalHelper(root.right, arr)

    # 左側のノードへ移動します。
    inorderTraversalHelper(root.left, arr)

    return arr

def inorderTraversal(root):
    # ヘルパー関数を使います。
    return inorderTraversalHelper(root, [])


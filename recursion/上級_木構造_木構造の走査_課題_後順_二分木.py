"""
後順（二分木）
easy
整数で構成される二分木の根ノード root が与えられるので、後順を表す整数の配列を返す、postorderTraversal という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： integer[]

postorderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [-3,-10,9,5,0]

postorderTraversal( toBinaryTree([5,3,6,2,4,null,7]) )--> [2,4,3,7,6,5]

postorderTraversal( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]) )--> [-18,-4,-11,-17,3,25,19,8,-2]

postorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10,-4,-7,0,2,1,-3,5,8,6,15,19,18,13,3]

postorderTraversal( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]) )--> [-6,-9,0,-4,-5,14,10,16,19,17,15,1]

postorderTraversal( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]) )--> [-10,-4,-7,0,2,1,-3,5,8,6,15,19,18,13,3]

ヒントを閉じる

上級コース / 木構造 / 深さ優先走査(1)(2) を復習しましょう。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def postorderTraversalHelper(root, arr):
    # ベースケース、根ノードがNoneになると終了します。
    if root is None:
        return None

    # 左側のノードへ移動します。
    postorderTraversalHelper(root.left, arr)

    # 右側のノードへ移動します。
    postorderTraversalHelper(root.right, arr)

    # 根ノードのdataをarrにappendします。
    arr.append(root.data)

    return arr

def postorderTraversal(root):
    # ヘルパー関数を使います。
    return postorderTraversalHelper(root, [])


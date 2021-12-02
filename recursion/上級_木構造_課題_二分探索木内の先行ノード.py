"""
二分探索木内の先行ノード
medium
異なる整数値で構成される二分探索木（BST）の根ノード root と BST 内に存在する整数 key が与えられるので、根ノードが先行ノードである部分木を返す、predecessor という関数を作成してください。もし、そのようなノードが存在しない場合は null を返してください。ノード N の値を x とした時、先行ノードとは木の中に存在する x よりも小さい最大の値を持つノードのことを指します。後続ノードと先行ノードの操作は対称的です。


関数の入出力例

入力のデータ型： binaryTree<integer> root, integer key

出力のデータ型： binaryTree<integer>

predecessor( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [0,-10,5,null,-3,null,9]

predecessor( toBinaryTree([5,3,6,2,4,null,7]), 5 )--> [4]

predecessor( toBinaryTree([10,6,12,4,8,null,null,2]), 12 )--> [10,6,12,4,8,null,null,2]

predecessor( toBinaryTree([10,6,12,4,8,null,null,2]), 2 )--> []

predecessor( toBinaryTree([5,null,7]), 5 )--> []

predecessor( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]), 8 )--> [3]

predecessor( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]), 6 )--> [5]

predecessor( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]), 10 )--> [1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]

ヒントを閉じる

このアルゴリズムを解く前に、後続ノードの問題を解いて練習しましょう。
"""

"""
二分探索木内の先行ノードの解説と解答
まずは findNode 関数を使って key のノードを探します。ID199 二分探索木内探索の問題を参考に findNode 関数を定義しましょう。key のノードを targetNode とします。

次にターゲットとなるノードに左側の子があるかどうかで 2 つのケースに分けて考えます。

(1) targetNode が左の子を持っていた場合
(2) targetNode が左の子を持っていない場合
(1) のケース
targetNode が左側の子を持っていたら、左側部分木の中の最大値が先行ノードになります。
二分探索木から最大値を探す関数は、ID202 二分探索木内の最大値を参考に定義しましょう。
(2) のケース
targetNode の左側に子がない場合、先行ノードは存在しないか、もしくは targetNode の祖先の内の 1 つになります。
祖先のノードを保存しておくため、変数 predecessor を用意し最初は null を入れておきます。

探索と同じ要領でルートから木を降りていきます。
targetNode が現在の iterator よりも大きい場合、現在の iterator は先行ノードである可能性があるので、
predecessor に iterator を代入し、iterator を右へ進めます。

targetNode が現在の iterator よりも小さい場合は先行ノードになる可能性はありません。そのまま次へ進みます。
targetNode まで iterator が進んだら、保存していた predecessor を返します。それではコードを見てみましょう。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def predecessor(root, key):
    # keyのノードを探し、変数targetNodeに代入します。
    targetNode = findNode(root, key)
    # keyがBST内に存在しない場合、Noneを返します。
    if targetNode == None:
        return None
    # targetNodeに左側の子がある場合は、その部分木の最大値を返します。
    if targetNode.left is not None:
        return maximumNode(targetNode.left)

    predecessor = None
    iterator = root
    # rootをiteratorに代入し、探索と同じ要領でtargetNodeがiteratorよりも小さい時には左へ、大きい時には右へ進みます。
    while iterator is not None:
        # ターゲットとiteratorのdataが同じだったら、その時のpredecessorを返します。
        if iterator.data == targetNode.data:
            return predecessor

        # 右側に進むときは、現在のiteratorが先行ノードである可能性があるので、predecessorを更新します。
        if iterator.data < targetNode.data:
            predecessor = iterator
            iterator = iterator.right

        # 左側に進むときはpredecessorを更新する必要はありません。
        else:
            iterator = iterator.left

    return predecessor








# keyのノードを探す関数
def findNode(root, key):
    iterator = root

    while iterator is not None:
        if iterator.data == key:
            return iterator
        if iterator.data < key:
            iterator = iterator.right
        else:
            iterator = iterator.left

    return iterator


# 最大値を探す関数
def maximumNode(root):
    iterator = root
    while iterator is not None and iterator.right is not None:
        iterator = iterator.right
    return iterator






# class BinaryTree:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
# def predecessor(root, key):
#     iterator = root
#     # dataがkeyと一致するノードを探索
#     while iterator is not None:
#         if iterator.data == key:
#             return predecessorHelper(root, iterator, key)
#         if iterator.data > key:
#             iterator = iterator.left
#         else:
#             iterator = iterator.right
#
#     return None
#
#
#
# # 先行ノード (keyよりも小さい、最大の値を持つノード）を探索する関数
# def prodecessorHelper(root, iterator, key):
#     # 値がkeyのノードの左側に部分木を持つ場合、その右端が後続ノード
#     if iterator.left is not None:
#         iterator = iterator.left
#         while iterator.right is not None:
#             iterator = iterator.right
#         return iterator
#     # 値がkeyのノードの左側に部分木が持たない場合、上から探索
#     else:
#         iterator2 = root
#         while iterator2.data >= key or iterator2.right.data < key:
#             if iterator2.right is not None and iterator2.right.data < key:
#                 iterator2 = iterator2.right
#             if iterator2.data > key:
#                 iterator2 = iterator2.left
#                 # 値がkeyのノードが最小値の場合、Noneを返す
#                 if iterator2.data == key:
#                     return None
#
#         return iterator2





# def predecessor(root, key):
#     if root == None:
#         return None
#     if root.data < key:
#         node = predecessor(root.right, key)
#         if node == None:
#             return root
#         else:
#             return node
#     elif root.data > key:
#         return predecessor(root.left, key)
#     else:
#         iterator = root.left
#         if iterator == None:
#             return None
#         while iterator.right is not None:
#             iterator = iterator.right
#         return iterator




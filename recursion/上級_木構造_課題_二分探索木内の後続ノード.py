"""
二分探索木内の後続ノード
medium
異なる整数値で構成される二分探索木（BST）の根ノード root と BST 内に存在する整数 key が与えられるので、
根ノードが後続ノードである部分木を返す、successor という関数を作成してください。
もし、そのようなノードが存在しない場合は null を返してください。
ノード N の値を x とした時、後続ノードとは木の中に存在する x よりも大きい最小の値を持つノードのことを指します。


関数の入出力例

入力のデータ型： binaryTree<integer> root, integer key

出力のデータ型： binaryTree<integer>

successor( toBinaryTree([0,-10,5,null,-3,null,9]), 5 )--> [9]

successor( toBinaryTree([5,3,6,2,4,null,7]), 5 )--> [6,null,7]

successor( toBinaryTree([10,6,12,4,8,null,null,2]), 12 )--> []

successor( toBinaryTree([10,6,12,4,8,null,null,2]), 2 )--> [4,2]

successor( toBinaryTree([5,4,null]), 5 )--> []

successor( toBinaryTree([-2,-17,8,-18,-11,3,19,null,null,null,-4,null,null,null,25]), 8 )--> [19,null,25]

successor( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]), 6 )--> [8]

successor( toBinaryTree([3,-3,13,-7,1,6,18,-10,-4,0,2,5,8,15,19]), 3 )--> [5]

successor( toBinaryTree([1,-5,15,-9,-4,10,17,null,-6,null,0,null,14,16,19]), 10 )--> [14]

ヒントを閉じる

ノード A が右側に部分木を持つ場合、それは後続ノードがその部分木の中の最左端のノードであることを意味します。
右部分木で最小検索を行うと、後継ノードを検索することができます。
では、ノード A が右側に部分木を持たない場合はどうすればよいでしょうか？

ヒントを閉じる

ノード A が右側に部分木を持っていない場合、それは後続ノードが A の先祖の 1 つであるという事実を排除するものではありません。
ノード A よりも大きい最小値をツリー全体で探索してみましょう。探索の範囲内に後続ノードが存在しない場合はどうなるでしょうか？
"""

"""
ロジック

二分探索木内の後続ノードの解説と解答
まずは findNode 関数を使って key のノードを探します。ID199 二分探索木内探索の問題を参考に findNode 関数を定義しましょう。
key のノードを targetNode とします。
次にターゲットとなるノードに右側の子があるかどうかで 2 つのケースに分けて考えます。

(1) targetNode が右の子を持っていた場合
(2) targetNode が右の子を持っていない場合

(1) のケース
targetNode が右側の子を持っていたら、右側部分木の中の最小値が後続ノードになります。
二分探索木から最小値を探す関数は、ID201 二分探索木内の最小値を参考に定義しましょう。

(2) のケース
targetNode の右側に子がない場合、後続ノードは targetNode の祖先の内の 1 つになります。
祖先のノードを保存しておくため、変数 successor を用意し、最初は null を入れておきます。

探索と同じ要領でルートから木を降りていきます。
targetNode が現在の iterator よりも小さい場合、現在の iterator は後続ノードである可能性があるので、
successor に iterator を代入し、iterator を左へ進めます。

targetNode が現在の iterator よりも大きい場合は、iterator が後続ノードになる可能性はありません。そのまま次へ進みます。
targetNode まで iterator が進んだら、保存していた successor を返します。それではコードを見てみましょう。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def successor(root, key):
    # keyのノードを探し、変数targetNodeに代入します。
    targetNode = findNode(root, key)

    # keyがBST内に存在しない場合、Noneを返します。
    if targetNode == None:
        return None

    # targetNodeに右側の子がある場合、その部分木の最小値を返します。
    if targetNode.right is not None:
        return minimumNode(targetNode.right)

    successor = None
    iterator = root
    # rootをiteratorに代入し、探索と同じ要領でtargetNodeがiteratorよりも小さい時には左へ、大きい時は右へ進みます。
    while iterator is not None:
        # ターゲットとiteratorのdataが同じだったら、その時のsuccessorを返します。
        if targetNode.data == iterator.data:
            return successor

        # 左側に進むときは、現在のiteratorが後続ノードである可能性があるのでsuccessorで更新します。
        if targetNode.data < iterator.data:
            successor = iterator
            iterator = iterator.left

        # 右側に進むときはsuccessorを更新する必要はありません。
        else:
            iterator = iterator.right

    return successor


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

# 最小値を探す関数
def minimumNode(root):
    iterator = root
    while iterator is not None and iterator.left is not None:
        iterator = iterator.left
    return iterator







# class BinaryTree:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#
# def successor(root, key):
#     if root == None:
#         return None
#     if root.data > key:
#         node = successor(root.left, key)
#         return root if node == None else node
#     elif root.data < key:
#         return successor(root.right, key)
#     else:
#         currentNode = root.right
#         if currentNode == None:
#             return None
#         while currentNode.left is not None:
#             currentNode = currentNode.left
#
#         return currentNode


# def successor(root, key):
#     if maxBST(root).data <= key:
#         return None
#     if maxBST(root).data == root.data:
#         return root
#
#     if root.data == key:
#         return minBST(root.right)
#     elif root.data > key:
#         return successor(root.left, key)
#     elif root.data < key:
#         return successor(root.right, key)
#
#
# def minBST(root):
#     if root.left == None:
#         return root
#     return minBST(root.left)
#
# def maxBST(root):
#     if root.right == None:
#         return root
#     return maxBST(root.right)


"""
対称的な二分木
medium
二分木 root が与えられるので、それが左右対称かどうかを確かめる、symmetricTree という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： bool

symmetricTree( toBinaryTree([10,25,25,33,45,45,33]) )--> true

symmetricTree( toBinaryTree([10,25,25,33,45,45,32]) )--> false

symmetricTree( toBinaryTree([1,2,2,3,4,4,3]) )--> true

symmetricTree( toBinaryTree([]) )--> true

symmetricTree( toBinaryTree([1,9,9,15,19,19,15]) )--> true

symmetricTree( toBinaryTree([1,2,2,null,3,null,3]) )--> false

symmetricTree( toBinaryTree([3,6,6,9,12,12,9]) )--> true

symmetricTree( toBinaryTree([3,6,7,9,12,12,9]) )--> false

symmetricTree( toBinaryTree([1,2,2,2,null,2]) )--> false

symmetricTree( toBinaryTree([1,2,3]) )--> false

どのようにして対称性を判断するかを考えてみましょう。根ノードの左右の部分木に異なる探索アルゴリズムを適用することが1つの戦略として考えられるでしょう。

"""

"""
root の左右の子を引数に取るヘルパー関数を用意します。
このヘルパー関数は、部分木が対称である場合は true を返し、対称でない場合は false を返す再帰関数です。
2 つの部分木が対称であるためには、次の 3 つの条件が true でなければなりません。

1 - 両者の根ノードの値が同じであること
2 - 左の木の左の子と、右の木の右の子が対称であること。
3 - 左の木の右の子と、右の木の左の子が対称であること。
ベースケースとして、左右のノードがどちらも null になったら true 、どちらか一方だけが null なら false を返すようにします。

再帰的に、左の木の左の子、右の木の右の子と、左の木の右の子、右の木の左の子が対称であるかを調べます。
両者がどちらも true だった場合に true を返します。それではコードを見てみましょう。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def symmetricTree(root):
    # 根ノードがNone の時には True を返します。
    if root == None:
        return True
    # ヘルパー関数を使い左右の子を根ノードとする部分木が同じかどうかチェックします。
    return symmetricTreeHelper(root.left, root.right)


def symmetricTreeHelper(leftNode, rightNode):
    # ベースケース
    if leftNode == None and rightNode == None:
        return True
    if leftNode == None or rightNode == None:
        return False
    # ２つの部分木の根ノードの値が違ったらFalse
    if leftNode.data != rightNode.data:
        return False
    # 「左の木の左」と「右の木の右」、「左の木の右」と「右の木の左」
    # が対称であるか再帰的に調べます。
    return symmetricTreeHelper(leftNode.left, rightNode.right) \
        and symmetricTreeHelper(leftNode.right, rightNode.left)




# def symmetricTree(root):
#     if root == None:
#         return True
#
# def isMirror(t1, t2):
#     if t1 == None and t2 == None:
#         return True
#     elif t1 == None or t2 == None:
#         return False
#
#     # 左右の部分木に対して、（左の部分木の左部分）= (右の部分木の右部分）
#     # かつ（左の部分木の右部分）= (右の部分木の左部分）が成立しているかを
#     # 再帰的に確認する
#     if t1.data == t2.data:
#         return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
#     else:
#         return False



# def symmetricTree(root):
#     if not root:
#         return True
#     return symmetricTreeHelper(root, root)
#
# def symmetricTreeHelper(left, right):
#     if left and right:
#         return left.data == right.data and  \
#                symmetricTreeHelper(left.left, right.right) and \
#                symmetricTreeHelper(left.right, right.left)
#     else:
#         return left == right




# def symmetricTree(root):
#     return symmetricTreeHelper(root, root, True)
#
#
# def symmetricTreeHelper(froot, broot, isSymmetric):
#     if froot != None:
#         if broot == None:
#             return False
#         elif froot.data != broot.data:
#             return False
#
#         isSymmetric = symmetricTreeHelper(froot.right, broot.left, isSymmetric)
#         isSymmetric = symmetricTreeHelper(froot.left, broot.right, isSymmetric)
#
#     return isSymmetric






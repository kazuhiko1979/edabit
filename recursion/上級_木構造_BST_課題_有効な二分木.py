"""
有効な二分木
medium
二分木 root が与えられるので、それが二分探索木（BST）かどうか確かめる、validateBST という関数を作成してください。ただし、有効な BST とは以下の条件を指します。

- ノードの左部分木にはノードのキーより小さい値を含みます。

　
- ノードの右部分木にはノードのキーより大きい値を含みます。

　
- 左右の部分木も BST である必要があります。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： bool

validateBST( toBinaryTree([0,null,-1]) )--> false

validateBST( toBinaryTree([4,1,5]) )--> true

validateBST( toBinaryTree([15,10,20,8,12,16,25]) )--> true

validateBST( toBinaryTree([30,15,60,7,22,45,75,null,null,17,27]) )--> true

validateBST( toBinaryTree([5,1,2,3,4]) )--> false

validateBST( toBinaryTree([5,1,4,null,null,3,6]) )--> false

validateBST( toBinaryTree([]) )--> true

validateBST( toBinaryTree([5,3,9,1,6,8]) )--> false

validateBST( toBinaryTree([1]) )--> true

validateBST( toBinaryTree([1,2]) )--> false
"""

"""
有効な二分木の解説と解答
親ノードのデータと左右の子のデータを比較するため、ヘルパー関数を使って親ノードのデータを渡します。ヘルパー関数の引数を、root, min, max とし、最初は null を入れておきます。左の子へ進む場合は親ノードを max の位置に入れて再帰し、右の子へ進む場合は親ノードのデータを min の位置に入れて再帰します。子が null になるまで進むことができたら true を、途中正しい構造でない場所があったら false を変数に代入します。最後に二つの変数がどちらも true だったら true を返します。

この再帰の流れを具体的に [5,1,2,3,4] の例で説明します。この例は正しい構造になっていないので false を返します。番号はコードのコメントにある番号、インデントは再帰の入れ子を意味します。

(1) 根ノード 5 から始めます。現在のノードのデータは 5、min は null、max も null です。
(2) min が null なのでスルー
(3) max が null なのでスルー
(4) 左の子があるので再帰。引数には (root.left, min, 5)を渡します。
    (1) 現在のノードのデータは 1、min は null、max は 5 です。
    (2) min が null なのでスルー
    (3) max は 5 です。data と比較し max の方が大きいので正しいノードです。
    (4) 現在のノード 1 に左の子があるので再帰。引数には (root.left, min, 1) を渡します。
        (1) 現在のノードのデータは 3、min は null、max は 1 です。
        (2) min が null なのでスルー
        (3) max は 1 です。data と比較し max の方が小さいので false を返し呼び出し元へ戻ります。
    三項演算子で変数 left に false が入ります。
    (5) 現在のノード 1 に右の子があるので再帰。引数には (root.right, 1, max) を渡します。
        (1) 現在のノードのデータは 4、min は 1、max は null です。
        (2) min は 5 です。data と比較し min の方が小さいので正しいノードです。
        (3) max は null なのでスルー
        (4) 現在のノード 4 には左の子がないので left に true
        (5) 現在のノード 4 には右の子がないので right に true
        (6) left も right も true なので true を返して呼び出し元へ戻る
    三項演算子で変数 right に true が入ります。
    (6) left は false、right は true なので、false を返して呼び出し元へ戻ります。
三項演算子で三項演算子で変数 left に false が入ります。
(5) 現在のノード 5 に右の子があるので再帰。引数には (root.right, 5, max) を渡します。
    (1) 現在のノードのデータは 2、min は 5、max は null です。
    (2) min は 5。data と比較し min の方が大きいので false を返し呼び出し元へ戻ります。
三項演算子で変数 right に false が入ります。
(6) left は false、right も false なので、false を返します。有効な二分木の解説と解答
親ノードのデータと左右の子のデータを比較するため、ヘルパー関数を使って親ノードのデータを渡します。ヘルパー関数の引数を、root, min, max とし、最初は null を入れておきます。左の子へ進む場合は親ノードを max の位置に入れて再帰し、右の子へ進む場合は親ノードのデータを min の位置に入れて再帰します。子が null になるまで進むことができたら true を、途中正しい構造でない場所があったら false を変数に代入します。最後に二つの変数がどちらも true だったら true を返します。

この再帰の流れを具体的に [5,1,2,3,4] の例で説明します。この例は正しい構造になっていないので false を返します。番号はコードのコメントにある番号、インデントは再帰の入れ子を意味します。

(1) 根ノード 5 から始めます。現在のノードのデータは 5、min は null、max も null です。
(2) min が null なのでスルー
(3) max が null なのでスルー
(4) 左の子があるので再帰。引数には (root.left, min, 5)を渡します。
    (1) 現在のノードのデータは 1、min は null、max は 5 です。
    (2) min が null なのでスルー
    (3) max は 5 です。data と比較し max の方が大きいので正しいノードです。
    (4) 現在のノード 1 に左の子があるので再帰。引数には (root.left, min, 1) を渡します。
        (1) 現在のノードのデータは 3、min は null、max は 1 です。
        (2) min が null なのでスルー
        (3) max は 1 です。data と比較し max の方が小さいので false を返し呼び出し元へ戻ります。
    三項演算子で変数 left に false が入ります。
    (5) 現在のノード 1 に右の子があるので再帰。引数には (root.right, 1, max) を渡します。
        (1) 現在のノードのデータは 4、min は 1、max は null です。
        (2) min は 5 です。data と比較し min の方が小さいので正しいノードです。
        (3) max は null なのでスルー
        (4) 現在のノード 4 には左の子がないので left に true
        (5) 現在のノード 4 には右の子がないので right に true
        (6) left も right も true なので true を返して呼び出し元へ戻る
    三項演算子で変数 right に true が入ります。
    (6) left は false、right は true なので、false を返して呼び出し元へ戻ります。
三項演算子で三項演算子で変数 left に false が入ります。
(5) 現在のノード 5 に右の子があるので再帰。引数には (root.right, 5, max) を渡します。
    (1) 現在のノードのデータは 2、min は 5、max は null です。
    (2) min は 5。data と比較し min の方が大きいので false を返し呼び出し元へ戻ります。
三項演算子で変数 right に false が入ります。
(6) left は false、right も false なので、false を返します。
"""

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validateBST(root):
    return validateBSTHelper(root, None, None)


# ヘルパー関数で再帰します。
def validateBSTHelper(root, minValue, maxValue):

    # 木が空の時はTrueを返します。
    if root == None:
        return True
    # 現在のノードのデータを代入します。
    data = root.data

    # 現在のノードのデータと引数で渡された親ノードのデータを比較します。
    # 再帰によって右の子へ進んだ場合、現在のデータよりもminValueに
    # 入っている親ノードのデータが大きかったらFalse
    if minValue is not None and minValue >= data:
        return False
    if maxValue is not None and maxValue <= data:
        return False

    # 現在のノードのdataを再帰的に繰り返します。
    # 葉ノードまでたどり着いたらそれぞれの変数にTrueを代入します。
    left = validateBSTHelper(root.left, minValue, data) if root.left is not None else True
    right = validateBSTHelper(root.right, data, maxValue) if root.right is not None else True

    return left and right















# def validateBST(root):
#
#     return isBST(root, None, None)
#
# def isBST(root, l, r):
#
#     if root == None:
#         return True
#
#     if l != None and root.data <= l.data:
#         return False
#
#     if r != None and root.data >= r.data:
#         return False
#
#     return isBST(root.left, l, root) and isBST(root.right, root, r)





# def validateBST(root):
#     if root == None:
#         return True
#     else:
#         return validateBSTHelper(root, None, None)
#
# # mtValue: 下限値 node.left の値はこれより大きい必要がある。
# # itValue: 上限値 node.rightの値はこれより小さい必要がある
# def validateBSTHelper(node, mtValue, itValue):
#     if node.left == None and node.right == None:
#         return True
#     elif node.left == None:
#         if node.data < node.right.data and (itValue == None or node.right.data < itValue):
#             return validateBSTHelper(node.right, node.data, itValue)
#         else:
#             return False
#     elif node.right == None:
#         if node.data > node.left.data and (mtValue == None or node.left.data > mtValue):
#             return validateBSTHelper(node.left, mtValue, node.data)
#         else:
#             return False
#     elif (node.data > node.left.data and (mtValue == None or node.left.data > mtValue)) and \
#             (node.right.data and (itValue == None or node.right.data < itValue)):
#         return validateBSTHelper(node.left, mtValue, node.data) and validateBSTHelper(node.right, node.dat,itValue)
#     else:
#         return False





# def validateBST(root):
#
#     return valid(root, float("-inf"), float("inf"))
#
#
# def valid(root, left, right):
#     if not root:
#         return True
#     if not root.data < right and root.data > left:
#         return False
#     return valid(root.left, left, root.data) and valid(root.right, root.data, right)
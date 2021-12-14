"""
二分木の最大の深さ
medium
二分木 root が与えられるので、最大の深さを返す、maximumDepth という関数を作成してください。ここでの最大の深さとは、根ノードから最も遠い葉ノードまでの最長経路に沿ったノードの数を指します。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： integer

maximumDepth( toBinaryTree([0]) )--> 1

maximumDepth( toBinaryTree([0,1,null]) )--> 2

maximumDepth( toBinaryTree([0,-10,5,null,-3,null,9]) )--> 3

maximumDepth( toBinaryTree([5,2,18,-4,3]) )--> 3

maximumDepth( toBinaryTree([27,14,35,10,19,31,42]) )--> 3

maximumDepth( toBinaryTree([30,15,60,7,22,45,75,null,null,17,27]) )--> 4

maximumDepth( toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]) )--> 4

maximumDepth( toBinaryTree([50,17,76,9,23,54,null,null,14,19,null,null,72]) )--> 4

maximumDepth( toBinaryTree([16,14,10,8,7,9,3,2,4,1]) )--> 4

ヒントを閉じる

再帰を使って左右の部分木の深さを比較しましょう。
"""
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def maximumDepth(root):
    return maximumDepthHelper(root, 1)


def maximumDepthHelper(root, depth):

    leftDepth = depth
    rightDepth = depth

    if root.left != None:
        leftDepth = maximumDepthHelper(root.left, depth+1)
    if root.right != None:
        rightDepth = maximumDepthHelper(root.right, depth+1)

    return max(leftDepth, rightDepth)


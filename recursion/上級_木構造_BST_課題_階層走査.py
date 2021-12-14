"""
階層走査
medium
二分木 root が与えられるので、階層ごとに左->右で配列で返す、levelOrderTraversal という関数を作成してください。


関数の入出力例

入力のデータ型： binaryTree<integer> root

出力のデータ型： integer[]

levelOrderTraversal( toBinaryTree([0,-10,5,null,-3,null,9]) )--> [0,-10,5,null,-3,null,9]

levelOrderTraversal( toBinaryTree([5,2,18,-4,3]) )--> [5,2,18,-4,3]

levelOrderTraversal( toBinaryTree([27,14,35,10,19,31,42]) )--> [27,14,35,10,19,31,42]

levelOrderTraversal( toBinaryTree([30,15,60,7,22,45,75,null,null,17,27]) )--> [30,15,60,7,22,45,75,null,null,17,27]

levelOrderTraversal( toBinaryTree([90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]) )--> [90,50,150,20,75,95,175,5,25,66,80,92,111,166,200]

levelOrderTraversal( toBinaryTree([50,17,76,9,23,54,null,null,14,19,null,null,72]) )--> [50,17,76,9,23,54,null,null,14,19,null,null,72]

levelOrderTraversal( toBinaryTree([16,14,10,8,7,9,3,2,4,1]) )--> [16,14,10,8,7,9,3,2,4,1]

ヒントを閉じる

階層ごとに要素を取得するには、キューを使って幅優先探索を行います。nullの場合があることに注意しましょう。
"""
import queue

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    queue = [root]
    results = []

    while not len(queue) == 0:
        curr = queue.pop(0)
        if curr == None:
            results.append('null')

        else:
            queue.append(curr.left)
            queue.append(curr.right)
            results.append(curr.data)

    while len(results) > 0 and results[len(results)-1] == 'null':
        results.pop()

    return results



# def levelOrderTraversal(root):
#
#     if root is None:
#         return root
#     arr = []
#     queue = [root]
#
#     while len(queue) != 0:
#         if queue[0] is None:
#             arr.append('null')
#         else:
#             queue.append(queue[0].left)
#             queue.append(queue[0].right)
#             arr.append(queue[0].data)
#         queue.pop(0)
#
#     while arr[len(arr)-1] == 'null':
#         arr.pop()
#
#     return arr



# def levelOrderTraversal(root):
#
#     q = queue.Queue()
#     q.put(root)
#     arr = []
#
#     return levelOrderTraversalHelper(q, arr)
#
# def levelOrderTraversalHelper(q, arr):
#     # キューが空になるまで繰り返し
#     while not q.empty():
#         # キューの先頭要素を取り出し（キューはFIFO）
#         node = q.get()
#         # 取り出した要素がnullなら、配列にnullを追加し、その後の処理はスキップ
#         if node == None:
#             arr.append(None)
#             continue
#         # 取り出した要素の左側をキューへ追加
#         if node.left == None:
#             q.put(None)
#         else:
#             q.put(node.left)
#
#         # 取り出した要素の右側をキューへ追加
#         if node.right == None:
#             q.put(None)
#         else:
#             q.put(node.right)
#
#         # 配列に取り出した要素の値を格納
#         arr.append(node.data)
#
#     # 配列の最後尾がnullであれば、削除
#     while len(arr) > 0 and arr[-1] == None:
#         arr.pop(-1)
#
#     return arr



# def levelOrderTraversal(root):
#
#     queue, arr, object_address = [], [], []
#     queue.append(root)
#     object_address.append(root)
#
#     while len(queue):
#         node = queue.pop(0)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#
#         object_address.append(node.left)
#         object_address.append(node.right)
#
#     firstData = 0
#
#     for i in range(len(object_address)-1, -1, -1):
#         if firstData == 0 and object_address[i] == None:
#             continue
#         else:
#             firstData = 1
#             if object_address[i]:
#                 arr.append(object_address[i].data)
#             else:
#                 arr.append(object_address[i])
#
#     arr.reverse()
#     return arr

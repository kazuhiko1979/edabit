"""
連結リストの交わる点
medium
連結リストの先頭 headA と headB がそれぞれ与えられるので、お互いの連結リストが交わるノードの値を返す、findMergeNode という関数を作成してください。headA と headB は異なるものとし、null ではありません。また全ての整数は正とし、A と B の交わりが存在しない場合は -1 を返してください。

関数の入出力例

入力のデータ型： SinglyLinkedListNode<integer> headA, SinglyLinkedListNode<integer> headB

出力のデータ型： integer

findMergeNode(singlyLinkedList([2,10,34,45,67,356]),singlyLinkedList([20,5,34,45,67,356])) --> 34

findMergeNode(singlyLinkedList([34,657,24,36,75,867,345,75,345,64,75]),singlyLinkedList([13,4,6,3,345,64,75])) --> 345

findMergeNode(singlyLinkedList([34,657,24,36,75,867,345,75,345,64,75]),singlyLinkedList([13,4,6,3,345,64,75,34])) --> -1

ントを閉じる

AとBの交わりが存在した場合、交わる点から後ろは同じ値が続きます。同じ値になる最初の部分を探します。2つのリストは長さが違うことに注意しましょう。
"""

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtHead(head, data):

    # dataを受け取って、SinglyLinkedLisNodeのインスタンスを作成し、
    # 変数newNodeに代入します。
    iterator = SinglyLinkedListNode(data)
    # ポイントをheadにします。
    iterator.next = head
    # newNodeを返します。
    return iterator


def insertAtTail(head, data):

    # 再帰
    # headがnullの場合、新しいノードを作ります。
    if head == None:
        return SinglyLinkedListNode(data)
    # 末尾に達するまで再帰します。
    else:
        head.next = insertAtHead(head.next, data)
    return head


def deleteTail(head):
    # 要素数が1なら削除しない
    if head.next == None:
        return head

    iterator = head
    while iterator.next.next is not None:
        iterator = iterator.next
    iterator.next = None
    return head


def findMinNum(head):

    iterator = head
    currentIndex = 0
    # 最小値(minNode)をリストの先頭の値で初期化する
    minNode = head.data
    # 最小値のインデックスで(minIndex)をリストの先頭のインデックスで初期化する
    minIndex = 0

    while iterator.next is not None:
        iterator = iterator.next
        currentIndex += 1
        # 現在の最小値(minNode)よりも小さな値が見つかった場合
        if iterator.data <= minNode:
            minNode = iterator.data
            # 最小値の(minNode)をその小さな値(iterator.data)に置き換える
            minIndex = currentIndex
    return minIndex

def linkedListSearch(head, data):

    iterator = head
    currentIndex = 0
    # 検索対象のインデックス(findIndex)を-1で初期化する
    findIndex = -1

    while iterator is not None:
        # dataと同じ値が見つかった場合
        if iterator.data == data:
            return currentIndex
        else:
            iterator = iterator.next
            currentIndex += 1
    return findIndex

def findMergeNode(headA, headB):
    # リストの長さをそれぞれ取得します。
    lA = getLinkListLength(headA)
    lB = getLinkListLength(headB)

    # 2つのリストの長さを比較し、長い方を先頭から切って同じ長さにします。
    headA = getNodeAt(headA, lA-lB) if lA >= lB else headA
    headB = getNodeAt(headB, lB-lA) if lB >= lA else headB

    answer = None

    iteratorA = headA
    iteratorB = headB

    # 2つのiteratorを走査しつつ同じ値になるノードを探します。
    while iteratorA is not None:
        if iteratorA.data is not iteratorB:
            answer = None
        elif answer == None:
            answer = iteratorA.data

        iteratorA = iteratorA.next
        iteratorB = iteratorB.next

    return -1 if answer == None else answer


# リストの長さを取得する関数
def getLinkListLength(head):

    iterator = head
    length = 0
    while iterator is not None:
        length + 1
        iterator = iterator.next

    return length

# インデックスのノードを取得する関数
def getNodeAt(head, position):
    iterator = head
    for i in range(position):
        if iterator == None:
            return None
        iterator = iterator.next

    return iterator


#     iteratorA = headA
#
#     while iteratorA != None:
#         iteratorB = headB
#         while iteratorB != None:
#             if iteratorA.data == iteratorB.data and findMergeNodeHelper(iteratorA, iteratorB):
#                 return iteratorA.data
#             iteratorB = iteratorB.next
#         iteratorA = iteratorA.next
#
#     return -1
#
#
# def findMergeNodeHelper(headA, headB):
#     while headA != None or headB != None:
#         if headA == None or headB == None or headA.data != headB.data:
#             return False
#         headA = headA.next
#         headB = headB.next
#
#     return True


print(findMergeNode(SinglyLinkedListNode([2, 10, 34, 45, 67, 356]), SinglyLinkedListNode([20, 5, 34, 45, 67, 356])))
print(findMergeNode(SinglyLinkedListNode([34,657,24,36,75,867,345,75,345,64,75]),SinglyLinkedListNode([13,4,6,3,345,64,75])))

# print(linkedListSearch(SinglyLinkedListNode([1,3,4,5]),3))
# print(linkedListSearch(SinglyLinkedListNode([1,1,1,1]),1))
# print(linkedListSearch(SinglyLinkedListNode([1,6,3,63,68,9,5]),5))












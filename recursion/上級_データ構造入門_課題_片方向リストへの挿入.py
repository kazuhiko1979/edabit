"""
片方向リストへの挿入
easy
連結リストの先頭 head、位置 position、データ data が与えられるので、特定の位置の後にデータを挿入した連結リストを返す、insertNodeAtPosition という関数を作成してください。

関数の入出力例

入力のデータ型： SinglyLinkedListNode<integer> head, integer position, integer data

出力のデータ型： SinglyLinkedListNode<integer>

insertAtPosition(singlyLinkedList([2,10,34,45,67,356]),2,5) --> 2➡10➡34➡5➡45➡67➡356➡END

insertAtPosition(singlyLinkedList([2,10,34,45,67,356]),2,3) --> 2➡10➡34➡3➡45➡67➡356➡END

insertAtPosition(singlyLinkedList([2,10,34,45,67,356]),5,3) --> 2➡10➡34➡45➡67➡356➡3➡END

insertAtPosition(singlyLinkedList([20,-5,34,45,67,356]),34,50) --> 20➡-5➡34➡45➡67➡356➡END

insertAtPosition(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5]),20,54) --> 20➡-5➡34➡45➡67➡356➡34➡687➡31➡-34➡5➡END

insertAtPosition(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5]),4,54) --> 20➡-5➡34➡45➡67➡54➡356➡34➡687➡31➡-34➡5➡END

片方向リスト - 挿入を復習しましょう。
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


def insertAtPosition(head,position,data):

    # # for文を利用した場合
    #
    # # dataを入れた新しいノードを作ります。
    # node = SinglyLinkedListNode(data)
    #
    # # 先頭に挿入
    # if position == 0:
    #     node.next = head
    #     head = node
    #     return head
    #
    # # iterator に headを入れます。
    # iterator = head
    # # 与えられた位置の１つ前までリストを走査します。
    # for i in range(position):
    #     # もしiterator.next がnullだったらheadを返します。
    #     if iterator.next == None:
    #         return head
    #     # iteratorをnextへ進めます。
    #     iterator = iterator.next
    #
    # # tempに現在のiterator.nextを入れます
    # temp = iterator.next
    # # iterator.nextを新しいノードにします。
    # iterator.next = node
    # # 新しいノードのnextをtempにします。
    # node.next = temp
    #
    # return head


    # While文を利用した場合
    i = 0
    iterator = head
    if position == 0:
        newNode = SinglyLinkedListNode(data)
        newNode.next = head
        head = newNode
        return head

    while iterator is not None:
        if i == position:
            temp = iterator.next
            iterator.next = SinglyLinkedListNode(data)
            iterator.next.next = temp
        iterator = iterator.next
        i+=1
    return head









print(insertAtPosition(SinglyLinkedListNode([2,10,34,45,67,356]),2,5))
print(insertAtPosition(SinglyLinkedListNode([2,10,34,45,67,356]),0,5))










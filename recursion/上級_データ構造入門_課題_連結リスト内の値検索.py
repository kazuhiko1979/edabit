"""
連結リスト内の値検索
easy
連結リストの先頭 head と整数 data が与えられるので、リスト内に存在する data のインデックスを返す、linkedListSearch という関数を作成してください。もし、data が存在しない場合は、-1 を返してください。

関数の入出力例

入力のデータ型： SinglyLinkedListNode<integer> head, integer data

出力のデータ型： integer

linkedListSearch(singlyLinkedList([1,3,4,5]),3) --> 1

linkedListSearch(singlyLinkedList([1,1,1,1]),1) --> 0

linkedListSearch(singlyLinkedList([1,6,3,63,68,9,5]),5) --> 6

linkedListSearch(singlyLinkedList([3,3,2,10,34,45,67,356]),67) --> 6

linkedListSearch(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5]),-5) --> 1

linkedListSearch(singlyLinkedList([71,8,16,33]),71) --> 0

linkedListSearch(singlyLinkedList([71,8,16,33]),686) --> -1

linkedListSearch(singlyLinkedList([101,54,822,93,131,1800,99]),1800) --> 5

linkedListSearch(singlyLinkedList([580,781]),781) --> 1

linkedListSearch(singlyLinkedList([2,4,52,108]),52) --> 2

linkedListSearch(singlyLinkedList([61,73,27,3001]),45) --> -1

リストを走査してdataを探します。nextへ進めるごとにインデックスをカウントします。
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


print(linkedListSearch(SinglyLinkedListNode([1,3,4,5]),3))
print(linkedListSearch(SinglyLinkedListNode([1,1,1,1]),1))
print(linkedListSearch(SinglyLinkedListNode([1,6,3,63,68,9,5]),5))












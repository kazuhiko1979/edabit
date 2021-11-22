"""
先頭に挿入
easy
連結リストの先頭 head と整数 data が与えられるので、リストの先頭にデータを挿入した新しい連結リストを返す、
insertAtHead という関数を作成してください。

関数の入出力例

入力のデータ型： SinglyLinkedListNode<integer> head, integer data

出力のデータ型： SinglyLinkedListNode<integer>

insertAtHead(singlyLinkedList([3,3,2,10,34,45,67,356]),367) --> 367➡3➡3➡2➡10➡34➡45➡67➡356➡END

insertAtHead(singlyLinkedList([3,3,2,10,34,45,67,356]),4) --> 4➡3➡3➡2➡10➡34➡45➡67➡356➡END

insertAtHead(singlyLinkedList([56]),50) --> 50➡56➡END

insertAtHead(singlyLinkedList([3,32,2,10,34,45,67,356]),46) --> 46➡3➡32➡2➡10➡34➡45➡67➡356➡END

insertAtHead(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5]),75) -->
75➡20➡-5➡34➡45➡67➡356➡34➡687➡31➡-34➡5➡END

insertAtHead(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5]),96) -->
96➡20➡-5➡34➡45➡67➡356➡34➡687➡31➡-34➡5➡END

nextは次のノードオブジェクトの参照を指します。dataのノードを新しく作り、そのnextをheadへと変更します。
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

    # while newNode is not None:
    #     print(newNode.data, end="➡")
    #     newNode = newNode.next
    # # print("END")

def insertAtTail(head, data):

    # 再帰
    # headがnullの場合、新しいノードを作ります。
    if head == None:
        return SinglyLinkedListNode(data)
    # 末尾に達するまで再帰します。
    else:
        head.next = insertAtHead(head.next, data)

    return head




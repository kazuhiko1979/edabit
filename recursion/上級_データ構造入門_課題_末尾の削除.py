"""
末尾の削除
easy
連結リストの先頭 head が与えられるので、リストの末尾のノードを削除した新しい連結リストを返す、deleteTail という関数を作成してください。

関数の入出力例

入力のデータ型： SinglyLinkedListNode<integer> head

出力のデータ型： SinglyLinkedListNode<integer>

deleteTail(singlyLinkedList([3,3,2,10,34,45,67,356])) --> 3➡3➡2➡10➡34➡45➡67➡END

deleteTail(singlyLinkedList([8,7,21,3,2,7])) --> 8➡7➡21➡3➡2➡END

deleteTail(singlyLinkedList([8,8,7,7,5])) --> 8➡8➡7➡7➡END

deleteTail(singlyLinkedList([8,6,3,5,7])) --> 8➡6➡3➡5➡END

deleteTail(singlyLinkedList([8,8,7,7,6,6,5,5,4,4])) --> 8➡8➡7➡7➡6➡6➡5➡5➡4➡END

deleteTail(singlyLinkedList([2,5,10,25,50])) --> 2➡5➡10➡25➡END

deleteTail(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5])) --> 20➡-5➡34➡45➡67➡356➡34➡687➡31➡-34➡END

ヒントを閉じる

末尾の一つ前のノードを探し、そのノードが指すnextへの参照を外します。
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









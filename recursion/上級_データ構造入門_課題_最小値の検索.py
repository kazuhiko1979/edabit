"""
連結リストの先頭 head が与えられるので、リストの中の最小値のインデックスを返す、findMinNum という関数を作成してください。

関数の入出力例

入力のデータ型： SinglyLinkedListNode<integer> head

出力のデータ型： integer

findMinNum(singlyLinkedList([1,2,3,4,-1,2])) --> 4

findMinNum(singlyLinkedList([1,1,1])) --> 2

findMinNum(singlyLinkedList([3,3,2,10,34,45,67,356])) --> 2

findMinNum(singlyLinkedList([20,-5,34,45,67,356,34,687,31,-34,5])) --> 9

findMinNum(singlyLinkedList([71,8,16,33])) --> 1

findMinNum(singlyLinkedList([101,54,82002,93,1207,131,1800,99])) --> 1

findMinNum(singlyLinkedList([580,781])) --> 0

findMinNum(singlyLinkedList([2,4,52,108])) --> 0

findMinNum(singlyLinkedList([61,73,27,3001])) --> 2

リストを走査して最小値を探します。
"""
import itertools

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







    # counter = 0
    # min_index = 0
    # min_data = head.data
    # while head is not None:
    #     if head.data < min_data:
    #         min_index = counter
    #         min_data = head.data
    #     counter += 1
    #     head = head.next
    # return min_index

    # counter = 0
    # linked_list = []
    # while head is not None:
    #     linked_list.append(head.data)
    #     head = head.next
    # return linked_list.index(min(linked_list))


    # counter = 0
    # linked_list = []
    # while head is not None:
    #     linked_list.append(head.data)
    #     head = head.next
    #     linked_list = list(itertools.chain(*linked_list))
    #
    # if len(set(linked_list)) == 1:
    #     return max([i for i, x in enumerate(linked_list)])
    #     # return linked_list.index(linked_list[-1])
    # return linked_list.index(min(linked_list))

print(findMinNum(SinglyLinkedListNode([1,2,3,4,-1,2])))
print(findMinNum(SinglyLinkedListNode([1,1,1])))
print(findMinNum(SinglyLinkedListNode([3,3,2,10,34,45,67,356])))
print(findMinNum(SinglyLinkedListNode([20,-5,34,45,67,356,34,687,31,-34,5])))











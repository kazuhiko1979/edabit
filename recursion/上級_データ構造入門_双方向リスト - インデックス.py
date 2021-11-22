"""
双方向リストにおいても、リスト内の要素にアクセスするには、線形探索を用います。
つまり、片方向リストの時に実装した、i 番目のインデックスを受け取り
i+1 番目のノードを返す at 関数、キーを受け取って要素の中から最初のキーを検索する
find 関数と同じ処理を双方向リストでも実装します。時間計算量は片方向リストの時と同様に O(n) になります。
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, arr):
        # 今回は末尾を追跡します。
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        # このcurrent Nodeは最後のnodeです。
        self.tail = currentNode

    def at(self, index):
        iterator = self.head
        # 片方向リストと同じ処理
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None:
                return None
        return iterator


    def reverse(self):
        reverse = self.tail
        iterator = self.tail.prev

        currentNode = reverse
        while iterator is not None:
            currentNode.next = iterator

            iterator = iterator.prev
            if iterator is not None:
                iterator.next = None
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        self.tail = currentNode
        self.head = reverse
        self.head.prev = None

    def printInReverse(self):
        iterator = self.tail
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.prev
        print()

    def printList(self):
        iterator = self.head
        while iterator != None:
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()



numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
numList.printList()
numList.printInReverse()

numList.printList()
numList.reverse()
numList.printList()
numList.printInReverse()



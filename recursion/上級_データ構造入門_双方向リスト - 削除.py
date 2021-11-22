"""
双方向リスト - 削除
双方向リストが片方向リストより優れている点は、前のポインタを持っているため、
ノードの削除を O(1) で実行することができるところです。
ノード A、B、C と並んでいるノード B を削除するには、
ノード A とノード C を連結するだけで問題ありません。
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, arr):
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

        self.tail = currentNode

    def at(self, index):
        iterator = self.head
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None:
                return None
        return iterator

    # リストの先頭から要素をpopします。0(1)
    def popFront(self):
        self.head = self.head.next
        self.head.prev = None

    # リストの末尾から要素をpopします。0(1)
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    # 与えられたノードを0(1)で削除します。
    def deleteNode(self, node):
        if node is self.tail:
            return self.pop()
        if node is self.head:
            return self.popFront()

        node.prev.next = node.next
        node.next.prev = node.prev

    # リストの先頭に追加します。
    def preappend(self, newNode):
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode

    # リストの最後に追加します。
    def append(self, newNode):
        self.tail.next = newNode
        newNode.next = None
        newNode.prev = self.tail
        self.tail = newNode

    # 与えられたノードの次に追加します。必要であれば末尾を更新してください。
    # 処理を紙に書いて確認しましょう。オブジェクトなので、=はメモリのアドレスを指します。
    def addNextNode(self, node, newNode):
        tempNode = node.next
        node.next = newNode
        newNode.next = tempNode
        newNode.prev = node
        # もし与えられたノードが末尾なら、その後ろに新しいノードが追加されるので、末尾をアップデート
        # それ以外の場合は、tempNodeの前をnewNodeに設定してください。
        if node is self.tail:
            self.tail = newNode
        else:
            tempNode.prev = newNode


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

# pop
numList.printList()

numList.popFront()
numList.pop()

numList.printList()
numList.printInReverse()

# 要素を削除します。
print("Deleting in O(1)")
numList.printList()

numList.deleteNode(numList.at(3))
numList.deleteNode(numList.at(9))
numList.deleteNode(numList.at(0))

numList.printList()






# 45をpreappend
# numList.preappend(Node(45))
# print(numList.head.data)
# numList.printList()

# # 71をappend
# numList.append(Node(71))
# print(numList.tail.data)
# numList.printList()
#
# # ノードの後に新しいノードを追加
# numList.addNextNode(numList.at(3), Node(4))
# numList.printList()
# print(numList.tail.data)
#
# numList.addNextNode(numList.at(15), Node(679))
# numList.printList()
# print(numList.tail.data)
#
# numList.printInReverse()

# numList.printInReverse()
#
# numList.printList()
# numList.reverse()
# numList.printList()
# numList.printInReverse()



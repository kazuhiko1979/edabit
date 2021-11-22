"""
双方向リストへの挿入も片方向リストの時と同様に、O(1) で実行することができます。双方向リストでは、
末尾の情報を追跡しているので、末尾にデータが挿入された場合は、
末尾を更新しなければいけない点に注意してください。
ノードをリストの末尾に追加する append も O(1) で計算することができます。
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

# 45をpreappend
numList.preappend(Node(45))
print(numList.head.data)
numList.printList()

# 71をappend
numList.append(Node(71))
print(numList.tail.data)
numList.printList()

# ノードの後に新しいノードを追加
numList.addNextNode(numList.at(3), Node(4))
numList.printList()
print(numList.tail.data)

numList.addNextNode(numList.at(15), Node(679))
numList.printList()
print(numList.tail.data)

numList.printInReverse()

# numList.printInReverse()
#
# numList.printList()
# numList.reverse()
# numList.printList()
# numList.printInReverse()



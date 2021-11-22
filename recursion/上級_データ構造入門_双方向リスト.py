"""
双方向リスト（doubly linked list）とは、次のポインタと前のポインタの2つを持つ、
連結リストのことを指します。双方向リストでは、片方向リストが可能なことは全てでき、
さらに前方向へアクセスできる機能を持っています。
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# リストは少なくとも1つのノードを持っている必要があります。
# nullリストをサポートしたい場合は、それに応じてコードを追加してください。
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
            # 次のノードの前のノードをcurrent Nodeに割り当てます。
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        # このcurrent Nodeは最後のnodeです。
        self.tail = currentNode

    def printList(self):
        iterator = self.head
        while iterator != None:
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()

numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])

numList.printList()
print(numList.head.data)
print(numList.head.next.data)
print(numList.tail.data)
print(numList.tail.prev.data)





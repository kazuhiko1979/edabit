"""
両端キュー(2)
では、両端キューの実用例の 1 つを見てみましょう。
両端キューを使って、リストの最大値を求めます。リストを反復しながら、現在の最大値を先頭に置き、
そうでなければ先頭よりも小さい値はリストの後ろに置くことができます。
反復が終了したのち、最大値を保持する両端キューの一番上の項目を返します。
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None:
            return None
        return self.head.data

    def peekBack(self):
        if self.tail == None:
            return None
        return self.tail.data

    def enqueueFront(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node

    def enqueueBack(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeueFront(self):
        if self.head == None:
            return None

        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return temp.data

    def dequeueBack(self):
        if self.tail == None:
            return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return temp.data

def getMax(arr):

    deque = Deque()
    # 最初の要素を両端キューの最初に追加します。
    deque.enqueueFront(arr[0])

    # 最大値は両端キューの先頭へ、そのほかの値は末尾へ向かいます。
    for i in arr[1:]:
        if i > deque.peekFront():
            deque.enqueueFront(i)
        else:
            deque.enqueueBack(i)

    print(deque.peekFront())
    # print(deque.peekBack())


print(getMax([34,35,64,34,10,2,14,5,353,23,35,63,23]))















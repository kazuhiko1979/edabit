"""
キュー
コンピュータサイエンスでは、キュー（Queue）とは FIFO（First-In-First-Out）
を実装した構造体のことを指します。
"""

"""
キューにおけるリストは、FIFO 方式で要素を追跡します。基本的な機能は、enqueue、dequeue の 2 つです。

Enqueue - リストの末尾に要素を挿入する関数（人が列に入って待つのと同じ）
Dequeue - リストの先頭を取得して削除する関数（列に入っている人が次の人になるのと同じ）
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None:
            return None
        return self.head.data

    def peekBack(self):
        if self.tail == None:
            return self.peekFront()
        return self.tail.data

    # Enqueue - リストの末尾に要素を挿入する関数（人が列に入って待つのと同じ）
    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data)
        elif self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    # Dequeue - リストの先頭を取得して削除する関数（列に入っている人が次の人になるのと同じ
    def dequeue(self):
        if self.head == None:
            return None
        temp = self.head

        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return temp.data

q = Queue()
print(q.peekFront())
print(q.peekBack())

q.enqueue(4)
print(q.peekFront())
print(q.peekBack())

q.enqueue(50)
print(q.peekFront())
print(q.peekBack())

q.enqueue(64)
print(q.peekFront())
print(q.peekBack())

print("dequeued : " + str(q.dequeue()))
print(q.peekFront())
print(q.peekBack())

















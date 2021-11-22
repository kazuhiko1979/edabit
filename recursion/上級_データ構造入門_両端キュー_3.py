"""
両端キュー(3)
以下の応用問題を解いてみましょう。


配列と整数 k が与えられたとき、サイズ k の連続する部分配列の最大値を求めてください。

例:
入力: [1, 2, 3, 1, 4, 5, 2, 3, 6], K = 3
出力: 3, 3, 4, 5, 5, 5, 6

1, 2, 3 の最大値は 3 です。
2, 3, 1 の最大値は 3 です。
3, 1, 4 の最大値は 4 です。
1, 4, 5 の最大値は 5 です。
4, 5, 2 の最大値は 5 です。
5, 2, 3 の最大値は 5 です。
2, 3, 6 の最大値は 6 です。
"""

"""
ではこのアルゴリズムを両端キューを用いて実装してください。
両端キュー deque をウィンドウとして扱い、アルゴリズムのルールのように値を保存、
削除してください。
最初にインデックス 0 番目から k-1 番目まで for 文で処理を行い deque に初期値を保存した後、k 番目から
 n 番目までウィンドウをスライドする for 文を実装してみましょう。
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

    def enqueueFront(self):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
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

def getMaxWindows(arr, k):
    if k > len(arr):
        return []

    results = []
    deque = Deque()

    # dequeの初期化
    for i, num in enumerate(arr[:k]):
        # 新しい値と、既存の値を比較して、新しい値以下はすべて削除するので、
        # dequeの末尾は新しい値より大きい値になります。
        # dequeの先頭は最大値です。（新しい値より大きいので削除されないから）
        while deque.peekBack() is not None and arr[deque.peekBack()] < num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    for i, num in enumerate(arr[k:], k):
        # dequeの先頭は最大値
        results.append(arr[deque.peekFront()])
        # ウィンドウ外にある要素は取り除きます。
        while deque.peekFront() is not None and deque.peekFront() <= i-k:
            deque.dequeueFront()
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()

        deque.enqueueBack(i)
    # 最後のmax
    results.append(arr[deque.peekFront()])

    return results


print(getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 3))







"""
サイズkの部分配列の最小値
medium
配列 intArr と整数 k が与えられるので、サイズ k の連続する部分配列の最小値を返す、minWindowArrK を作成してください。


関数の入出力例

入力のデータ型： integer[] intArr, integer k

出力のデータ型： integer[]

minWindowArrK([2,3,1,1,12,3,10],1) --> [2,3,1,1,12,3,10]

minWindowArrK([2,3,1,1,12,3,10],3) --> [1,1,1,1,3]

minWindowArrK([2,3,1,1,12,3,10],4) --> [1,1,1,1]

minWindowArrK([3,9,10,2,4,5],3) --> [3,2,2,2]

minWindowArrK([3,9,10,2,4,5],5) --> [2,2]

minWindowArrK([30,50,60,20,30,64,80],3) --> [30,20,20,20,30]

minWindowArrK([30,50,60,20,30,64,80],2) --> [30,50,20,20,30,64]

minWindowArrK([24,5,67,60,24,64,23,536,345],3) --> [5,5,24,24,23,23,23]

上級コース / データ構造入門 / 両端キュー(3)でスライディングウィンドウについて復習しましょう。

"""

# スタック・キューの場合
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

# def minWindowArrK(intArr,k):
    # ここから書きましょう

def minWindowArrK(arr, k):
    if k > len(arr):
        return []

    results = []
    deque = Deque()

    # dequeの初期化
    for i, num in enumerate(arr[:k]):
        # 新しい値と、既存の値を比較して、新しい値以下はすべて削除するので、
        # dequeの末尾は新しい値より大きい値になります。
        # dequeの先頭は最大値です。（新しい値より大きいので削除されないから）
        while deque.peekBack() is not None and arr[deque.peekBack()] > num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    for i, num in enumerate(arr[k:], k):
        # dequeの先頭は最大値
        results.append(arr[deque.peekFront()])
        # ウィンドウ外にある要素は取り除きます。
        while deque.peekFront() is not None and deque.peekFront() <= i-k:
            deque.dequeueFront()
        while deque.peekBack() is not None and arr[deque.peekBack()] >= num:
            deque.dequeueBack()

        deque.enqueueBack(i)
    # 最後のmax
    results.append(arr[deque.peekFront()])

    return results


print(minWindowArrK([2,3,1,1,12,3,10],1))




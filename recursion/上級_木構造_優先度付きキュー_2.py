"""
優先度付きキュー(2)
二分ヒープを構築し、最優先度の高い値にアクセスできるようになったので、次は pop() の実装方法を見てみましょう。

最優先度の高い値を削除するには、根ノードの値を削除し、新しい木がヒーププロパティを持っていることを確認する必要があります。

そこで、根ノードを二分ヒープの最後の葉ノードと入れ替え、最後の葉ノードを pop し、新しい根ノードで maxHeapify を呼び出します。
この処理は、ヒープソートで行った処理と非常に類似しています。

処理の時間計算量は O(
log
n
) です。以下の Pseudo code を参考にしてください。

pop
pop(heapArr):
    popped = heapArr[0]
    heapArr[0] = heapArr[heapArr.length-1]
    heapArr.pop()
    maxHeapify(heapArr, heapArr.length-1, 0)
    return popped
では、pop() メソッドを PriorityQueue 構造に追加してみましょう。
"""

"""

"""

import math
import copy


class HeapLibrary:

    @staticmethod
    def buildMaxHeap(arr):
        mid = HeapLibrary.parent(len(arr) - 1)

        for i in range(mid, -1, -1):
            HeapLibrary.maxHeapify(arr, len(arr)-1, i)


    @staticmethod
    def maxHeapify(arr, heapEnd, i):
        l = HeapLibrary.left(i)
        r = HeapLibrary.right(i)
        biggest = i

        if l <= heapEnd and arr[l] > arr[biggest]:
            biggest = l
        if r <= heapEnd and arr[r] > arr[biggest]:
            biggest = r

        if i != biggest:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            return HeapLibrary.maxHeapify(arr, heapEnd, biggest)


    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    @staticmethod
    def parent(i):
        return math.floor((i-1) / 2)


class PriorityQueue:

    def __init__(self, arr):
        self.maxHeap = copy.deepcopy(arr)
        HeapLibrary.buildMaxHeap(self.maxHeap)

    def top(self):
        return self.maxHeap[0]

    # 根ノードを二分ヒープの最後の葉ノードと入れ替え、最後の葉ノードをpopし、新しい根ノードで maxHeapify を呼び出します。
    def pop(self):
        popped = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[len(self.maxHeap) - 1]
        self.maxHeap.pop()
        HeapLibrary.maxHeapify(self.maxHeap, len(self.maxHeap)-1, 0)
        return popped

    def insert(self, x):
        self.maxHeap.append(x)
        i = len(self.maxHeap) - 1
        parent = HeapLibrary.parent(i)
        while parent >= 0 and self.maxHeap[parent] < x:
            self.maxHeap[i], self.maxHeap[parent] = self.maxHeap[parent], self.maxHeap[i]
            i = parent
            parent = HeapLibrary.parent(i)


pq = PriorityQueue([2,3,43,2,53,6,75,10])
print(pq.maxHeap)
pq.insert(5)
print(pq.maxHeap)
pq.insert(5)
print(pq.maxHeap)
pq.insert(79)
print(pq.maxHeap)
pq.pop()
print(pq.maxHeap)






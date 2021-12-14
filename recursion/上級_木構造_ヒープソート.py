"""
ヒープソート
では今度はリストの並べ替えを二分ヒープを用いて実装していきます。


最大値を繰り返し取得し、それをヒープの最後の葉ノードと入れ替えてヒープサイズを1減らし、根ノードからヒープサイズまでの配列をヒープ化します。


未整列のリストから最大ヒープを作成します。このときヒープのサイズを把握するための変数を用意しておきます。最初のヒープのサイズは配列全体のサイズで、この後ゆっくりとゼロまで減少していきます。


次に根ノード（最大値）と最後の葉ノードを入れ替えて、サイズを小さくします。そして、最大の要素が根ノードとなるように、二分ヒープを maxHeapify します。

これをヒープサイズがゼロになるまで繰り返します。配列内のヒープの右側にあるデータはすべてソートされた配列になります。ヒープサイズが 0 になったとき、ソートされた配列を取得することができます。


このアルゴリズムを要素交換によって実行されるので二分ヒープをいつ終了するか把握するために、maxHeapify 関数を更新してヒープサイズを常に追跡しておかなければいけない点に注意してください。


Pseudo code は以下のようになります。

Pseudo-Code
heapSort(arr):
    buildMaxHeap(arr)
    heapEnd = arr.length - 1
    while(heapEnd > 0):
        # 最大値であるヒープの根ルートと葉ノードを入れ替えます。
        temp = arr[heapEnd]
        arr[heapEnd] = arr[0]
        arr[0] = temp
        heapEnd--
        maxHeapify(arr, heapEnd, 0)
このアルゴリズムは合計 n 回の maxHeapify 呼び出しとスワップを行います。maxHeapify は O(
log
n
) なので、ヒープソートの時間計算量は O(
n
log
n
) になります。配列の要素交換を繰り返す操作のため、空間計算量は O(1) になります。では、ヒープソートアルゴリズムを実装してみましょう。
"""

import math

class Heap:

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    @staticmethod
    def parent(i):
        return math.floor((i-1) / 2)

    @staticmethod
    def maxHeapify(arr, heapEnd, i):
        l = Heap.left(i)
        r = Heap.right(i)

        biggest = i

        if l <= heapEnd and arr[l] > arr[biggest]:
            biggest = l
        if r <= heapEnd and arr[r] > arr[biggest]:
            biggest = r

        if biggest != i:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            Heap.maxHeapify(arr, heapEnd, biggest)


    @staticmethod
    def buildMaxHeap(arr):
        middle = Heap.parent(len(arr))
        for i in range(middle, -1, -1):
            Heap.maxHeapify(arr, len(arr)-1, i)


    # ヒープソートを実装します。
    @staticmethod
    def heapSort(arr):
        # まずは buildMaxHeap で arr をヒープ構造にします。1番上は最大値になっています。

        Heap.buildMaxHeap(arr)

        # ヒープサイズを追跡するために heapEnd を配列の最後の要素にします。
        heapEnd = len(arr) - 1
        while heapEnd > 0:
            # 最大値であるヒープの根ルートと葉ノード heapEnd を入れ替えます。
            arr[0], arr[heapEnd] = arr[heapEnd], arr[0]

            # 一番最後はソートされているので、heapEnd から1引きます。
            heapEnd -= 1
            Heap.maxHeapify(arr, heapEnd, 0)

heap1 = [2,42,11,30,10,7,6,5,9]
print(heap1)
Heap.heapSort(heap1)
print(heap1)

heap2 = [56,4,51,10,12,5,12,4,6,5]
print(heap2)
Heap.heapSort(heap2)
print(heap2)




"""
ヒープソート
medium
整数によって構成される intArr が与えられるので、ヒープソートアルゴリズムによって、昇順ソートする、heapsort という関数を作成します。配列の要素間の入れ替えをすることによって、空間計算量 O(1) で実装してください。

関数の入出力例

入力のデータ型： integer[] intArr

出力のデータ型： integer[]

heapsort([1,2,3]) --> [1,2,3]

heapsort([1,2,3,4]) --> [1,2,3,4]

heapsort([1,2,3,4,5]) --> [1,2,3,4,5]

heapsort([6,5,4,3,2,1,0,-1,-2,-3,-4,-5]) --> [-5,-4,-3,-2,-1,0,1,2,3,4,5,6]

heapsort([3,4,5,5,5,6,7,2,10,2,1,-10,2,-2,0,-1]) --> [-10,-2,-1,0,1,2,2,2,3,4,5,5,5,6,7,10]
"""
import math

class Heap:

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return math.floor((i - 1) / 2)

    # ヒープのサイズを追跡するために maxHeapify を拡張します
    @staticmethod
    def maxHeapify(arr, heapEnd, i):
        l = Heap.left(i)
        r = Heap.right(i)
        biggest = i

        # heapEnd より後ろはすでにソートされているので、l, rのインデックスは heapEnd までを比較します
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

    # ヒープソートを実装します

def heapsort(arr):
    # buildMaxでarrをヒープ構造にします。1番上は最大値になっています。
    Heap.buildMaxHeap(arr)

    # ヒープサイズを追跡するため、heapEndを配列の最後の要素にします。
    heapEnd = len(arr) - 1
    while heapEnd > 0:
        # 最大値であるヒープの根ルートと葉ノード heapEndを入れ替えます。
        arr[0], arr[heapEnd] = arr[heapEnd], arr[0]

        # 一番最後はソートされているので、heapEndから1引きます。
        heapEnd -= 1
        Heap.maxHeapify(arr, heapEnd, 0)
    return arr



# import math
#
#
# def heapsort(intArr):
#
#     results = []
#     for i in range(len(intArr)-1, -1, -1):
#         buildMinHeap(intArr, i)
#         temp = intArr[0]
#         intArr[0] = intArr[i]
#         results.append(temp)
#
#     return results
#
# def buildMinHeap(arr, heapEnd):
#
#     parent = heapParent(heapEnd)
#     for i in range(parent, -1, -1):
#         minHeapify(arr, heapEnd, i)
#
#     return arr
#
#
# def minHeapify(arr, heapEnd, i):
#     l = left(i)
#     r = right(i)
#     smallest = i
#
#     if l <= heapEnd and arr[l] < arr[smallest]:
#         smallest = l
#     if r <= heapEnd and arr[r] < arr[smallest]:
#         smallest = r
#
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#
#         return minHeapify(arr, heapEnd, smallest)
#
#
# def left(i):
#     return 2 * i + 1
#
# def right(i):
#     return 2 * i + 2
#
# def heapParent(i):
#     return math.floor((i-1) / 2)






# import math
#
#
# def minHeapify(arr, heapEnd, i):
#
#     l = 2 * i + 1
#     r = 2 * i + 2
#     smallest = i
#
#     if l <= heapEnd and arr[l] > arr[smallest]:
#         smallest = l
#     if r <= heapEnd and arr[r] > arr[smallest]:
#         smallest = r
#
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         minHeapify(arr, heapEnd, smallest)
#
#
# def buildMinHeap(arr):
#     middle = math.floor((len(arr)-1) / 2)
#     while middle >= 0:
#         minHeapify(arr, len(arr)-1, middle)
#         middle -= 1
#
# def heapsort(intArr):
#
#     buildMinHeap(intArr)
#     heapEnd = len(intArr) - 1
#     while heapEnd > 0:
#         intArr[0], intArr[heapEnd] = intArr[heapEnd], intArr[0]
#         heapEnd -= 1
#         minHeapify(intArr, heapEnd, 0)
#     return intArr


print(heapsort([1,2,3]))
print(heapsort([1,2,3,4]))
print(heapsort([6,5,4,3,2,1,0,-1,-2,-3,-4,-5]))
print(heapsort([3,4,5,5,5,6,7,2,10,2,1,-10,2,-2,0,-1]))











"""
K個の最小値
medium
整数によって構成される intArr と整数 k（0 < k <= intArr.length）が与えられるので、配列から k 個の最小値を返す、minKElements という関数を作成してください。

関数の入出力例

入力のデータ型： integer[] intArr, integer k

出力のデータ型： integer[]

minKElements([3,2,1,5,6,4],2) --> [1,2]

minKElements([3,2,1,5,6,4],3) --> [1,2,3]

minKElements([7,8,2,3,1,7,8,11,4,3,2],5) --> [1,2,2,3,3]

minKElements([6,4,6,2,4,8,10,10,12],5) --> [2,4,4,6,6]

minKElements([8,4,13,10,18],4) --> [4,8,10,13]

minKElements([3,100,201,56,8,591,985,291],4) --> [3,8,56,100]

minKElements([879,487,98,397,610,150,474,977,404,478,623,554,306],6) --> [98,150,306,397,404,474]
"""

import math

def minKElements(intArr, k):

    maxHeap = buildMaxHeap(intArr)
    topKEleList = []
    while len(topKEleList) < k:
        topKEleList.append(pop(maxHeap))
    return topKEleList


def pop(maxHeap):
    popped = maxHeap[0]
    maxHeap[0] = maxHeap[len(maxHeap)-1]
    maxHeap.pop()
    maxHeapify(maxHeap, len(maxHeap)-1, 0)
    return popped


def buildMaxHeap(arr):
    middle = parent(len(arr))
    for i in range(middle, -1, -1):
        maxHeapify(arr, len(arr)-1, i)
    return arr


def maxHeapify(arr, heapEnd, i):

    l = left(i)
    r = right(i)
    biggest = i

    if l <= heapEnd and arr[l] < arr[biggest]:
        biggest = l
    if r <= heapEnd and arr[r] < arr[biggest]:
        biggest = r

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        maxHeapify(arr, heapEnd, biggest)


def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(n):
    return math.floor((n-1)/2)





# import math
#
# def topKElements(intArr, k):
#
#     buildMaxHeap(intArr)
#     heapEnd = len(intArr) - 1
#
#     results = []
#     # 最大ヒープを都度更新、根ノードと最後尾葉ノードを入れ替え
#     while k > 0:
#         maxHeapify(intArr, heapEnd, 0)
#         # intArr[0], intArr[heapEnd] = intArr[heapEnd], intArr[0]
#         temp = intArr[0]
#         intArr[0] = intArr[heapEnd]
#         results.append(temp)
#
#         heapEnd -= 1
#         k -= 1
#
#     return results
#
# def buildMaxHeap(arr):
#
#     mid = parent(len(arr)-1)
#
#     for i in range(mid, -1, -1):
#         maxHeapify(arr, len(arr)-1, i)
#     return arr
#
#
# def maxHeapify(arr, heapEnd, i):
#     l = left(i)
#     r = right(i)
#     biggest = i
#
#     if l <= heapEnd and arr[l] > arr[biggest]:
#         biggest = l
#     if r <= heapEnd and arr[l] > arr[biggest]:
#         biggest = r
#
#     if biggest != i:
#         arr[i], arr[biggest] = arr[biggest], arr[i]
#
#         return maxHeapify(arr, heapEnd, biggest)
#
#
# def left(i):
#     return 2 * i + 1
#
#
# def right(i):
#     return 2 * i + 2
#
#
# def parent(i):
#     return math.floor((i-1) / 2)





# import math
#
#
# class Heap:
#
#
#     @staticmethod
#     def left(i):
#         return 2 * i + 1
#
#     @staticmethod
#     def right(i):
#         return 2 * i + 2
#
#     @staticmethod
#     def parent(i):
#         return math.floor((i - 1) / 2)
#
#     # ヒープのサイズを追跡
#     @staticmethod
#     def maxHeapify(arr, heapEnd, i):
#         l = Heap.left(i)
#         r = Heap.right(i)
#         biggest = i
#
#         if l <= heapEnd and arr[l] > arr[biggest]:
#             biggest = l
#         if r <= heapEnd and arr[r] > arr[biggest]:
#             biggest = r
#
#         if biggest != i:
#             arr[i], arr[biggest] = arr[biggest], arr[i]
#             Heap.maxHeapify(arr, heapEnd, biggest)
#
#     @staticmethod
#     def buildMaxHeap(arr):
#         middle = Heap.parent(len(arr))
#         for i in range(middle, -1, -1):
#             Heap.maxHeapify(arr, len(arr) - 1, i)
#
#     # Heapsort
#     @staticmethod
#     def heapSort(arr):
#         # buildMaxHeap で arr をヒープ構造にし、先頭は最大値になります。
#         Heap.buildMaxHeap(arr)
#
#         # ヒープサイズ追跡  heapEndを配列の最後尾に指定
#         heapEnd = len(arr) - 1
#         while heapEnd > 0:
#             # 最大値であるヒープの根ルートと葉ノードを heapEndを入れ替えます。
#             arr[heapEnd], arr[0] = arr[0], arr[heapEnd]
#
#             # 最後尾はソートされているので、heapEndから1引きます。
#             heapEnd -= 1
#             Heap.maxHeapify(arr, heapEnd, 0)
#
# # 配列から k 個の最大値を返します
# def topKElements(intArr, k):
#     Heap.heapSort(intArr)
#     intArr.reverse()
#     return intArr[0:k]


print(minKElements([3,2,1,5,6,4],2))
print(minKElements([3,2,1,5,6,4],3))




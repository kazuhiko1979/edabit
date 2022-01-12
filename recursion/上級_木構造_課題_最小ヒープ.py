"""
最小ヒープ
medium
整数によって構成される intArr が与えられるので、最小値が先頭に配置される最小ヒープを表す配列を返す、buildMinHeap という関数を作成してください。

関数の入出力例

入力のデータ型： integer[] intArr

出力のデータ型： integer[]

buildMinHeap([3,2,1]) --> [1,2,3]

buildMinHeap([10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3]) --> [-3,0,-2,2,1,-1,4,3,7,9,6,10,5,8]

buildMinHeap([7,8,2,3,1,4,3,2]) --> [1,2,2,3,8,4,3,7]

buildMinHeap([8,4,13,10,18]) --> [4,8,13,10,18]

buildMinHeap([3,100,201,56,8,591,985,291]) --> [3,8,201,56,100,591,985,291]

buildMinHeap([879,487,98,397,610,150,474,977,404,478,623,554,306]) --> [98,397,150,404,478,306,474,977,487,610,623,554,879]
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

    @staticmethod
    def minHeapify(arr, i):
        l = Heap.left(i)
        r = Heap.right(i)
        smallest = i

        if l < len(arr) and arr[l] < arr[smallest]:
            smallest = l
        if r < len(arr) and arr[r] < arr[smallest]:
            smallest = r

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            Heap.minHeapify(arr, smallest)

def buildMinHeap(intArr):

    middle = Heap.parent(len(intArr) - 1)
    # 最後の葉ノードの親ノードから根ノード minHeapfyします
    for i in range(middle, -1, -1):
        Heap.minHeapify(intArr, i)

    return intArr





# import math
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
# def maxHeapify(arr, i):
#     l = left(i)
#     r = right(i)
#     biggest = i
#
#     if l <= len(arr) - 1 and arr[l] > arr[biggest]:
#         biggest = l
#     if r <= len(arr) - 1 and arr[r] > arr[biggest]:
#         biggest = r
#
#     if biggest != i:
#         arr[i], arr[biggest] = arr[biggest], arr[i]
#         maxHeapify(arr, biggest)
#
# def buildMaxHeap(intArr):
#
#     middle = math.floor((len(intArr)-1) / 2)
#     while middle >= 0:
#         maxHeapify(intArr, middle)
#         middle -= 1
#     return intArr


print(buildMinHeap([3, 2, 1]))
print(buildMinHeap([10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3]))






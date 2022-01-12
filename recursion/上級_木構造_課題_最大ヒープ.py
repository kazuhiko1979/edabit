"""
最大ヒープ
medium
整数によって構成される intArr が与えられるので、最大値が先頭に配置される最大ヒープを表す配列を返す、buildMaxHeap という関数を作成してください。

関数の入出力例

入力のデータ型： integer[] intArr

出力のデータ型： integer[]

buildMaxHeap([1,2,3]) --> [3,2,1]

buildMaxHeap([-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]) --> [10,7,9,5,6,8,3,4,0,-2,1,-3,2,-1]

buildMaxHeap([7,8,2,3,1,4,3,2]) --> [8,7,4,3,1,2,3,2]

buildMaxHeap([8,4,13,10,18]) --> [18,10,13,8,4]

buildMaxHeap([3,100,201,56,8,591,985,291]) --> [985,291,591,100,8,3,201,56]

buildMaxHeap([879,487,98,397,610,150,474,977,404,478,623,554,306]) --> [977,879,554,487,623,306,474,397,404,478,610,150,98]
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
    def maxHeapify(arr, i):
        l = Heap.left(i)
        r = Heap.right(i)
        biggest = i

        if l < len(arr) and arr[l] > arr[biggest]:
            biggest = l
        if r < len(arr) and arr[r] > arr[biggest]:
            biggest = r

        if biggest != i:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            Heap.maxHeapify(arr, biggest)

def buildMaxHeap(intArr):

    middle = Heap.parent(len(intArr))
    # 最後の葉ノードの親ノードから根ノード maxHeapfyします
    for i in range(middle, -1, -1):
        Heap.maxHeapify(intArr, i)

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


print(buildMaxHeap([1, 2, 3]))
print(buildMaxHeap([-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]))






class Heap:

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

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

            # temp = arr[i]
            # arr[i] = arr[biggest]
            # arr[biggest] = temp

            Heap.maxHeapify(arr,biggest)

heap1 = [2,42,11,30,10,7,6,5,9]
Heap.maxHeapify(heap1, 0) # 根ノードが2で 2 > 42のため、最大ヒープではありません。
print(heap1)

heap2 = [56,4,51,10,12,5,12,4,6,5]
Heap.maxHeapify(heap2, 1) # インデックス1が4で、4 < 10のため、最大ヒープではありません。
print(heap2)

"""
優先度付きキュー(1)
ヒープは、優先度付きキューに最適なデータ構造です。


優先度付きキューは、「キューに対して要素を優先度付きで追加する」、「最も高い優先度を持つ要素をキューから取り除く」ことをサポートしたデータ構造です。


優先度付きキューは、要素を優先度に従って整理し、以下の操作をサポートするデータ構造として定義することができます。

Insert(x): // 要素xをキューの適切な位置に挿入します。
Top(): // 最も高い優先度を持つ要素を取得します。
Pop(): // 優先度の高い要素を削除して取得します。

二分ヒープを使うと、Top() は O(1)、Pop() は O(
log
n
)、Insert は O(
log
n
) で実現することができます。最も高い優先度を持つキューや、最も低い優先度を持つキューは、最大ヒープや最小ヒープを用いて実装することができます。


最大値を優先する場合、優先度を決定したり、誰が何にアクセスするかを制御したり、スケジュール管理システムを必要とするアプリケーションの実装には欠かせません。一方、最小値を優先する場合、イベント駆動型のアプリケーションに使用することができ、そこではイベントがキューに追加され、割り当てられた発生時刻までに実行されます。


それでは二分ヒープを使って、最大値を優先するケースのデータ構造を構築していきましょう。O(1) で末尾に pop、push することができる動的配列の内部に全ての要素を保持する構造体を作り、ヒーププロパティを維持するために必要な演算を適用します。最大値を優先する場合は、値が大きいほど優先度が高くなるので、最大ヒープを使って実装を行っていきます。


まずはデータ構造体の設定と初期化から始めてみましょう。この構造体は、与えられた配列で初期化することができます。その配列を二分ヒープにして、Top() を呼び出すことができます。
"""
import math
# deepcopyを使用するためcopyライブラリをimportします。
import copy

# ヒープのためのライブラリ
class HeepLibrary:

    # 配列を受け取り、要素間を入れ替えて、配列を最大ヒープへ変換
    @staticmethod
    def buildMaxHeap(arr):
        mid = HeepLibrary.parent(len(arr)-1)

        for i in range(mid, -1, -1):
            HeepLibrary.maxHeapify(arr, len(arr)-1, i)


    # 要素iが最大ヒーププロパティを満たすように確認してください。
    @staticmethod
    def maxHeapify(arr, heapEnd, i):
        l = HeepLibrary.left(i)
        r = HeepLibrary.right(i)
        biggest = i

        if l <= heapEnd and arr[l] > arr[i]:
            biggest = l
        if r <= heapEnd and arr[r] > arr[i]:
            biggest = r

        if i != biggest:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            return HeepLibrary.maxHeapify(arr, heapEnd, biggest)


    @staticmethod
    def left(i):
        return i*2+1

    @staticmethod
    def right(i):
        return i*2+2

    @staticmethod
    def parent(i):
        return math.floor((i-1)/2)

class PriorityQueue:

    def __init__(self, arr):
        # 配列のディープコピーを行います。これによって、arrの状態の変更を防ぎます。
        self.maxHeap = copy.deepcopy(arr)
        HeepLibrary.buildMaxHeap(self.maxHeap)

    # 最も優先度の高い値を返します。最大ヒープを使用しているので、根ノードは常に最大値になります。
    def top(self):
        return self.maxHeap[0]

pq = PriorityQueue([2,3,43,2,53,6,75,10])
print(pq.maxHeap)
print(pq.top())





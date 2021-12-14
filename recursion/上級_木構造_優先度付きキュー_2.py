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


"""
最良計算量において、挿入ソートが選択ソートより優れていることはわかったでしょう。
このケースはすでに配列がソートされているケースに適用されるのでした。
つまり、ほとんどのケースでは最悪計算量 O(n2) の速度で計算しなければいけないことになります。
果たしてこれがベストなのでしょうか？数学者やコンピュータ科学者は、この問題を解決するためにさまざまな方法を考え出しました。
そして分割統治法という方法が誕生しました。

分割：問題全体を同じ構造の小さな問題に分割します。
統治：それ以上分割できない規模になったら、これを解いて部分問題の解を求めます。
合併：求めた多数の部分問題の解を分割と逆方向に順番に併合していき、全体を一つに統合します。
"""

"""
mergeSort 関数は配列 A を受け取り、以下のような処理を行います。

1. A が 1 つの要素しか持たないとき、A を返します。
2. それ以外の場合、A を leftArray と rightArray に分けます。leftArray と rightArray の両方を mergeSort という関数を使ってソートします。
3. leftArray と rightArray はソートされています。
4. leftArray と rightArray は両方ソートされているはずなので、その 2 つを結合して combinedArray を作成してください。
結合には以下の反復を使ってください。
   - leftArray と rightArray の先頭を比べて、どちらが先に combinedArray に入るか決めます。
   - これを leftArray と rightArray の全ての値が combinedArray に入るまで繰り返します。"""

import math


def merge(arr):
    return mergeHelper(arr, 0, len(arr) - 1)

def mergeHelper(arr, start, end):
    if start == end:
        return [arr[start]]
    middle = math.floor((start+end) / 2)
    leftArr = mergeHelper(arr, start, middle)
    rightArr = mergeHelper(arr, middle+1, end)

    leftArr.append(math.inf)
    rightArr.append(math.inf)
    l = len(leftArr) + len(rightArr) - 2
    li = 0
    ri = 0
    merged = []

    while (li+ri) < l:
        if leftArr[li] <= rightArr[ri]:
            merged.append(leftArr[li])
            li = li + 1
        else:
            merged.append(rightArr[ri])
            ri = ri + 1


    return merged

arr1 = [34,4546,32,3,2,8,6,76,56,45,34,566,1]
print(arr1)
print(merge(arr1))





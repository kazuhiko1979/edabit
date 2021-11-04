"""
ライブラリを呼び出してソートすることもできます。
"""
arr = [34,4546,32,3,2,8,6,76,56,45,34,566,1]
# print(arr)

# sortedは状態を変更しません。ソートされた配列を返します。
# print(sorted(arr))
# print(arr)

# sortメソッドは状態を更新します。配列をソートします。
# arr.sort()
# print(arr)

# sortを使用しないアルゴリズム(選択ソート）
def selectionSort(list):
    n = len(list)
    for i in range(n):
        minIndex = i # i番目の値を暫定の最小値とします。

        for j in range(i + 1, n):
            if list[j] <= list[minIndex]: # 暫定の最小値以下なら最小値を更新
                minIndex = j # 最小値を持つ

        # list[i] とA[minIndex]の入れ替え
        temp = list[i]
        list[i] = list[minIndex]
        list[minIndex] = temp


# print(arr)
# selectionSort(arr) # 昇順に並び替え
# print(arr) # ソートされた配列

# sortを使用しないアルゴリズム(挿入ソート）
arr = [34,4546,32,3,2,8,6,76,56,45,34,566,1]

def insertionSort(arrList):
    n = len(arrList)
    # 配列を左から右へと処理します。
    for i in range(n):
        # currentValueは配列の左端に挿入される項目です。
        currentValue = arrList[i]
        # jは右から左へインデックスを追跡します。
        for j in range(i-1, -1, -1):
            # もし、currentValueが小さい場合は、左右の値を入れ替えます。
            if currentValue <= arrList[j]:
                arrList[j+1] = arrList[j]
                arrList[j] = currentValue

            # 現在の値がA[j]よりも大きい場合、それは正しい位置にあるので、
            # ループを終了してi+1にします。

            else:
                break

print(arr)
insertionSort(arr) # 昇順に並び替え
print(arr) # ソートされた配列

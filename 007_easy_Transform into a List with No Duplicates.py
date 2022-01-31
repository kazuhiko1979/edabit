"""
リストを並べ替えて、重複するアイテムをリストから削除する関数を作成します。

Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

setify([4, 4, 4, 4]) ➞ [4]

setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]

setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

"""

def setify(lst):

    # Bubble sort
    for i in range(len(lst), 1, -1):
        for j in range(0, i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                pass
    # print(lst)
    # setを利用しない場合
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res


    # return sorted(set(lst))

print(setify([10, 3, 3, 5, 5]))
print(setify([10, 7, 9, 8, 5, 15]))





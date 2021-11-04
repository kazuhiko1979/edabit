"""
配列の重複（区別あり）
easy
整数で構成される配列 num1 と num2 が与えられるので、両方の配列に表示されている要素を小さい順で配列で返す、intersectionOfArraysRepeats という関数を作成してください。

関数の入出力例

入力のデータ型： integer[] intList1, integer[] intList2

出力のデータ型： integer[]

intersectionOfArraysRepeats([3,2,1],[3,2,1]) --> [1,2,3]

intersectionOfArraysRepeats([1,1,1],[1,2,3,2,1]) --> [1,1]

intersectionOfArraysRepeats([3,2,2,2,1,10,10],[3,2,10,10,10]) --> [2,3,10,10]

intersectionOfArraysRepeats([2,19,11,2,6,8],[10,23,5,8,19]) --> [8,19]

intersectionOfArraysRepeats([4,22,100,88,6,8],[1,2,3]) --> []

intersectionOfArraysRepeats([-1,-2,-1,-1],[-1,-1,-2,-2]) --> [-2,-1,-1]

intersectionOfArraysRepeats([1,2,2,1],[2,2,2,1]) --> [1,2,2]

intersectionOfArraysRepeats([4,9,5],[9,4,9,8,4]) --> [4,9]

ヒントを閉じる

ハッシュマップを使いましょう。片方の配列の値をキーとし、値の個数をハッシュマップの値として格納します。
その後、もう一つの配列を 1 要素ずつ確認し、キーの存在と値の個数に気をつけながら重複している数値を探しましょう。
"""

def intersectionOfArraysRepeats(listA, listB):

    # listAのリストをハッシュマップにします。
    hashmap = {}

    for key in listA:
        if key not in hashmap:
            hashmap[key] = 1
        else:
            hashmap[key] += 1

    res = []

    for i in listB:
        if i in hashmap:
            if hashmap[i] > 0:
                res.append(i)
                hashmap[i] -= 1

    return sorted(res)

print(intersectionOfArraysRepeats([3,2,1],[3,2,1]))
print(intersectionOfArraysRepeats([1,1,1],[1,2,3,2,1]))
print(intersectionOfArraysRepeats([3,2,2,2,1,10,10],[3,2,10,10,10]))
print(intersectionOfArraysRepeats([2,19,11,2,6,8],[10,23,5,8,19]))
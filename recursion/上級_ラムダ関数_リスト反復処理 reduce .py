"""
リスト反復処理 reduce
reduce 高階関数は、リスト、コールバック、初期値を受け取り、各リスト要素にコールバックを反復的に適用し、最終的に 1 つの値に評価する関数です。
コールバックは、現在の要素と前の要素の戻り値、初期値（最初の要素の時のみ）を受け取り、リストは、単一の値に "縮小" されます。
"""

"""
コールバックは、累積値を処理し、次の要素に対して、新たな累積値を返す必要があることに注意してください。
reduce 関数を作成して、階乗の処理を実行してみましょう。
"""

from functools import reduce

def myReduce(reduceCallback, arr, initial):
    lastResult = initial
    for i in arr:
        result = reduceCallback(i, lastResult)
        lastResult = result
    return lastResult

list1 = [1,2,3]
list2 = [1,2,3,4,5,6,7,8,9,10]

# 3!
# 1 * 1 -> 1
# 1 * 2 -> 2
# 2 * 3 -> 6
# print(myReduce((lambda x, total: x*total), list1, 1))
#
# # 10!
# print(myReduce((lambda x, total: x*total), list2, 1))

# 文字列のリストを reduce 関数を使って結合してみましょう。

from functools import reduce

list1 = ["hello", "world", "and", "hello", "jupiter"]
# reduce(累積値、現在の値）
print(reduce((lambda totalStr, currStr: totalStr + ", " + currStr), list1))

# Pythonには、すべての配列を1つの文字列に結合するためのjoin関数も用意されています。
print(",".join(list1))

# joinの逆であるsplitは区切りを取り、区切りに基づいて文字列を配列要素に分割する
print(",".join(list1).split())

array2d = [[2,3,4,5],[5,22,34,4,5],[12,13,45,67,84]]

# 平坦化して1次元配列にします。
flatten = reduce((lambda flattenList, arr: flattenList+arr), array2d)

print(flatten)
print(flatten[1])


def reduceMap(f, list):
    return [f(num) for num in list]


def reduceFilter(predicateF, list):
    return [predicateF(num) for num in list if num % 2]

list1 = [1,2,3,4,5,6,7,8,9,10]
print(reduceMap(lambda x: x*x, list1))
print(reduceFilter(lambda x: x, list1))













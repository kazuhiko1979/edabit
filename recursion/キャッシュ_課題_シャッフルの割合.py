"""
配列のシャッフル
easy
mith は間違い探しゲームに参加しました。異なる数字が並べられているボード arr と同じ数字がシャッフルされたボード shuffledArr が与えられるので、shuffledArr に対して arr がどこのインデックスへ移動したかを返す、shuffledPositions という関数を定義してください。

関数の入出力例

入力のデータ型： integer[] arr, integer[] shuffledArr

出力のデータ型： integer[]

shuffledPositions([2,32,45],[45,32,2]) --> [2,1,0]

shuffledPositions([10,11,12,13],[12,10,13,11]) --> [1,3,0,2]

shuffledPositions([10,11,12,13],[10,11,12,13]) --> [0,1,2,3]

shuffledPositions([1350,181,1714,375,1331,943,735],[1714,1331,735,375,1350,181,943]) --> [4,5,0,3,1,6,2]

ヒントを閉じる

shuffledArrの要素とインデックスを記録するハッシュマップを作りましょう。
"""
import math

def shuffleSuccessRate(arr, shuffledArr):




    # count = 0
    #
    # for i in range(len(arr)):
    #         if arr[i] == shuffledArr[i]:
    #             continue
    #         else:
    #             count += 1
    #
    # return math.floor(count / len(arr) * 100)


    # ハッシュマップを作ります。
    # hashmap_shuffledArr = {}
    # # shuffledArrをループして、要素とそのインデックスをハッシュマップに保存します。
    # for i in range(len(shuffledArr)):
    #     hashmap_shuffledArr[shuffledArr[i]] = i
    #
    # # ハッシュマップを作ります。
    # beforeMove_Arr = {}
    # for i in range(len(arr)):
    #     beforeMove_Arr[arr[i]] = i



    # indexが変更された要素数をカウントして、変更割合を計算します
    # count = 0
    #
    # for i in range(len(arr)):
    #         if arr[i] == shuffledArr[i]:
    #             continue
    #         else:
    #             count += 1
    #
    # return math.floor(count / len(arr) * 100)


print(shuffleSuccessRate([2,32,45],[45,32,2]))
print(shuffleSuccessRate([2,32,45],[45,2,32]))
print(shuffleSuccessRate([2,32,45],[2,32,45]))
print(shuffleSuccessRate([2,32,45,67],[2,32,67,45]))
print(shuffleSuccessRate([2,32,45,67,89],[2,89,67,45,32]))
print(shuffleSuccessRate([119,726,398,187,943,486,728,305,968,754,650,536,969,305,111,225,708,806,40,969],[708,969,111,398,754,726,536,943,486,305,969,40,650,806,187,225,968,119,728,305]))
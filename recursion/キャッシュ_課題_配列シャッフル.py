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
def shuffledPositions(arr, shuffledArr):

    # ハッシュマップを作ります。
    hashmap = {}
    # shuffledArrをループして、要素とそのインデックスをハッシュマップに保存します。
    for i in range(len(shuffledArr)):
        hashmap[shuffledArr[i]] = i
    # print(hashmap)

    # 答え入れる配列を初期化します。
    res = []
    # arrをループしてハッシュマップに保存した要素のインデックスを0
    # (1)で取得します。
    for i in range(len(arr)):
        res.append(hashmap[arr[i]])

    return res





    # hashmap_shuffledArr = [0] * len(shuffledArr)
    # index = 0
    #
    # for i in arr:
    #     if i in shuffledArr:
    #         hashmap_shuffledArr[index] = shuffledArr.index(i)
    #         index += 1
    #     else:
    #         return 'False'
    # return hashmap_shuffledArr

print(shuffledPositions([2,32,45],[45,32,2]))
print(shuffledPositions([10,11,12,13],[12,10,13,11]))





# res = []

# print(shuffledArr.index(32))

# for i in arr:
#     if i in shuffledArr:
#         res.append(shuffledArr.index(i))
# print(res)



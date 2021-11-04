"""
ショッピングリスト
easy
Whalum は兄が買うものはなんでも欲しがる性格です。
兄弟で一緒にネットショッピングをするときも、兄が買うものと同じものを買おうとしていました。
兄の注文リスト listA と Whalum の注文リスト listB が与えられるので、
兄が買うもので Whalum の注文リストに入ってないものを返す、
missingItems という関数を作成してください。
もし、被りが一切存在しない時は、兄の注文リストをそのまま返してください。

関数の入出力例

入力のデータ型： integer[] listA, integer[] listB

出力のデータ型： integer[]

missingItems([1,2,3,4,5,6,7,8],[1,3,5]) --> [2,4,6,7,8]

missingItems([1,2,3,4,5],[1,2]) --> [3,4,5]

missingItems([1,1],[2,2]) --> [1,1]

missingItems([9,8,7,6,5],[1,2]) --> [9,8,7,6,5]

missingItems([1,2],[9,8,7,6,5]) --> [1,2]

missingItems([3,4,5,1,2],[1,2]) --> [3,4,5]

missingItems([8,3,45,67,23,9,3],[5,7]) --> [8,3,45,67,23,9,3]

missingItems([8,3,45,67,23,9,3],[5,45]) --> [8,3,67,23,9,3]

missingItems([8,3,45,67,23,9,3],[3]) --> [8,45,67,23,9]

missingItems([8,3,45,67,23,9,3],[]) --> [8,3,45,67,23,9,3]

ヒントを閉じる

弟のリストでハッシュマップを作成し、兄のリストの要素が存在するかチェックします。
"""

def missingItems(listA, listB):

    # 弟のリストをハッシュマップにします。
    hashmap = {}
    for key in listB:
        if key not in hashmap:
            hashmap[key] = key
    # print(hashmap)

    res = []
    # 兄のリストの要素がハッシュマップになかったらresに追加します
    for item in listA:
        if item not in hashmap:
            res.append(item)

    return res


    # hashMap = {}
    # ans = []
    #
    # for x in range(len(listB)):
    #     hashMap[listB[x]] = listB[x]
    # # print(hashMap)
    #
    # for i in range(len(listA)):
    #     if listA[i] not in hashMap:
    #         ans.append(listA[i])
    #
    # return ans


print(missingItems([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 5]))
print(missingItems([1,1],[2,2]))
print(missingItems([8,3,45,67,23,9,3],[]))
print(missingItems([8,3,45,67,23,9,3],[5,45]))


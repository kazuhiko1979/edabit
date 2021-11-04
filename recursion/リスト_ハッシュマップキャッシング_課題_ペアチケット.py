"""
ペアチケット
easy
ある学校では文化祭のときに、生徒全員に数字をランダムに配っています。そして同じ数字同士を持つペアが現れたら、テーマパークのペアチケットをプレゼントしています（3 人以上いたら適応外になります）。生徒たちが持っている数字 numbers が与えられるので、ペアになる生徒たちの数字を返す findPairs という関数を作成してください。配列は昇順で返してください。

関数の入出力例

入力のデータ型： integer[] numbers

出力のデータ型： integer[]

findPairs([10,12,13,14,15,16,16,7,7,8]) --> [7,16]

findPairs([1,1]) --> [1]

findPairs([1,2]) --> []

findPairs([1,2,3,4,5,6,6,7,7,8]) --> [6,7]

findPairs([1,3,6,3,1,4,6,4]) --> [1,3,4,6]

findPairs([3,3,-1,-1,1,6,6,4,4]) --> [-1,3,4,6]

findPairs([30,30,30,30,1,600,600,40,40,40]) --> [600]

ヒントを閉じる

配列の要素をキー、要素の数を値としてハッシュマップを作成しましょう。
"""

def findPairs(numbers):

    # numbersの要素をキー、その数を値としてハッシュマップを作成
    hashmap = {}
    res = []

    for number in numbers:
        if number not in hashmap:
            hashmap[number] = 1
        else:
            hashmap[number] += 1
    # return hashmap

    # 値が2の時にキーをresへappendします
    for key in hashmap:
        if hashmap[key] == 2:
            res.append(key)

    return sorted(res)



    # hashmap = {}
    #
    # for i in numbers:
    #     if i not in hashmap:
    #         hashmap[i] = 1
    #     else:
    #         hashmap[i] += 1
    #
    # return sorted([key for key, val in hashmap.items() if val == 2])


print(findPairs([10,12,13,14,15,16,16,7,7,8]))
print(findPairs([1,2,3,4,5,6,6,7,7,8]))
print(findPairs([30,30,30,30,1,600,600,40,40,40]))
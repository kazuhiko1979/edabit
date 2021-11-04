"""
x回出現
easy
Block は野球のリーグ戦で運営を行なっており、試合の組み合わせを考えています。
a チームから z チームまでの 26 チームが存在し、
全チームが同じ数だけ試合をするようにしなければいけません。
]Block は試合が行われるチームを発見するたびに、
そのチーム名を記録しています（a チームを発見した場合は a が追加され、
"aabcbcdda" のような記録ができます）。
試合を行なったチーム一覧 teams が与えられるので、
全てのチームが同じ数だけ試合をしているかどうか判定する findXTimes という関数を作成してください。

関数の入出力例

入力のデータ型： string teams

出力のデータ型： bool

findXTimes("bacddc") --> false

findXTimes("babcddc") --> false

findXTimes("babacddc") --> true

findXTimes("aaabbbcccddd") --> true

findXTimes("aaabbccdd") --> false

findXTimes("zadbchvwxbwhdxvcza") --> true

findXTimes("zadbchvwxbwhdxvczb") --> false

findXTimes("zab") --> true

findXTimes("z") --> true

ヒントを閉じる

ハッシュマップを作りましょう。
すべての種類の文字が同じ数であることを効率よく確かめるには
どうしたらいいか考えてみましょう。
"""

def findXTimes(teams):

    hashmap = {}
    # ハッシュマップを作成し、teamsの要素をキー、その数を値として保存します。

    for i in range(len(teams)):
        if teams[i] not in hashmap:
            hashmap[teams[i]] = 1
        else:
            hashmap[teams[i]] += 1

    # return hashmap

    # ハッシュマップの値のみを取得するにはvalue()を使います。
    # 最大値と最小値が同じならtrueです。
    return max(hashmap.values()) == min(hashmap.values())

    # hashmap = {}
    #
    # for i in teams:
    #     if i not in hashmap:
    #         hashmap[i] = 1
    #     else:
    #         hashmap[i] += 1
    #
    # return len(set([val for key, val in hashmap.items()])) == 1

print(findXTimes("bacddc"))
print(findXTimes("babcddc"))
print(findXTimes("babacddc"))
print(findXTimes("zadbchvwxbwhdxvcza"))


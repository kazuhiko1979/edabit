"""
復習のお知らせ機能
medium
Zollar は算数の計算練習ができるサイトを立ち上げました。
そのサイトは a 問題から z 問題まで 26 個の問題があります。
このサイトには復習機能がついており、
1 回しか解いていない問題をトップページの一番上に表示するようにしました。
あるユーザーが解いたことのある問題一覧を表す小文字によって構成される文字列 s が与えられるので、
その中で 1 番最初に出てくる 1 回しか解いたことがない問題をインデックスで返す、
firstNonRepeating という関数を定義してください。当てはまる文字がない場合は -1 を返してください。

関数の入出力例

入力のデータ型： string s

出力のデータ型： integer

firstNonRepeating("aabbcdddeffg") --> 4

firstNonRepeating("abcdabcdf") --> 8

firstNonRepeating("abcddaebcdf") --> 6

firstNonRepeating("aabbbccdd") --> -1

firstNonRepeating("ddecdfgf") --> 2

firstNonRepeating("abcdeeff") --> 0

firstNonRepeating("zzcbdefghafhgbbcd") --> 5

ヒントを閉じる

sの文字をキー、その数を値としてハッシュマップを作成します。ハッシュマップの中から値が1の要素を探し、見つからなかったら-1を、見つかったらそのインデックスを返します。それではコードを見てみましょう。
"""
def firstNonRepeating(string):

    # s の文字をキー、その数を値としてハッシュマップ作製
    hashmap = {}
    # 当てはまる文字がない場合に返す-1を入れておく
    ans = -1

    for c in string:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    # sをループして、ハッシュマップの値が1のキーを探します。
    for i in range(len(string)):
        # 最初に出てくる文字を発見したらbreak
        if hashmap[string[i]] == 1:
            ans = i
            break
    return ans

    # hashmap = {}
    #
    # for i in string:
    #     if i not in hashmap:
    #         hashmap[i] = 1
    #     else:
    #         hashmap[i] += 1
    #
    # res = [string.index(key) for key, value in hashmap.items() if value == 1]
    #
    # return min(res) if res else -1


print(firstNonRepeating("aabbcdddeffg"))
print(firstNonRepeating("abcdabcdf"))
print(firstNonRepeating("abcddaebcdf"))
print(firstNonRepeating("aabbbccdd"))
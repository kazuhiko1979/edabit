"""
パングラム
easy
Faraone は宿題で英文を作るように頼まれました。ただし、a - z までの全てのアルファベットを含まなければいけない条件がついています。英文 string が与えられるので、a - z までの全ての文字を含んでいるか判定する、isPangram という関数を作成してください。

関数の入出力例

入力のデータ型： string string

出力のデータ型： bool

isPangram("we promptly judged antique ivory buckles for the next prize") --> true

isPangram("We promptly judged Antique ivory buckles for the next prize") --> true

isPangram("a quick brown fox jumps over the lazy dog") --> true

isPangram("sphinx of black quartz judge my vow") --> true

isPangram("the five boxing wizards jump quickly") --> true

isPangram("sheep for a unique zebra when quick red vixens jump over the yacht") --> false

isPangram("the Japanese yen for commerce is still well-known") --> false

isPangram("dan took the deep dive down the rabbit hole") --> false
"""


string = "we promptly judged antique ivory buckles for the next prize"
string = "We promptly judged Antique ivory buckles for the next prize"
string = "a quick brown fox jumps over the lazy dog"

def isPangram(string):
    # キャッシュを作成
    cache = [0] * 26

    # 1文字ずつ取得し、文字コードを使って、キャッシュを更新します
    for char in string:
        ascii = ord(char.lower())
        if ascii >= 97 and ascii <= 122:
            cache[ascii - 97] = 1

    # 0が1つもなかったらすべての文字が存在することになります。
    return not min(cache) == 0


    # list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', \
    #                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # cache = []
    #
    # for i in string:
    #     if i != " ":
    #         if i.lower() not in cache:
    #             cache.append(i.lower())
    #         else:
    #             continue
    #
    # return sorted(cache) == list_alphabet

print(isPangram("we promptly judged antique ivory buckles for the next prize"))


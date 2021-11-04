"""
マッチングアプリ
medium
Redd はマッチングアプリを開発しています。ユーザーの属性をアルファベットで記録しており、アルファベットの並ぶパターンが同じユーザーは相性が良いと判定しています。ユーザー1 の属性 user1、ユーザー2 の属性 user2 が与えられるので、この 2 つが同じパターンをしているかどうか判定する、hasSameType という関数を定義してください。

関数の入出力例

入力のデータ型： string user1, string user2

出力のデータ型： bool

hasSameType("aabb","yyza") --> false

hasSameType("aappl","bbtte") --> true

hasSameType("aappl","bbttb") --> false

hasSameType("aabb","abab") --> false

hasSameType("aappl","bktte") --> false

hasSameType("aaapppl","bbbttke") --> false

hasSameType("abcd","tso") --> false

hasSameType("abcd","jklm") --> true

hasSameType("aaabbccdddaa","jjjddkkpppjj") --> true

hasSameType("aaabbccdddaa","jjjddkkpppjd") --> false

ヒントを閉じる

user1の文字をキー、user2の文字を値としてハッシュマップを作成します。
"""

def hasSameType(user1,user2):

    # 文字列の長さが違う場合を最初に除きます。
    if len(user1) != len(user2):
        return False
    # ハッシュマップを作成
    hashmap = {}

    res = ''

    for i in range(len(user1)):
        # values() メソッドは、ハッシュマップの値だけを取り出します。

        # user1, user2それぞれのi番目の文字が、
        # どちらもハッシュマップにまだ存在しなかったら保存します。
        if user1[i] not in hashmap and user2[i] not in hashmap.values():
            hashmap[user1[i]] = user2[i]

    # return hashmap

    # ハッシュマップのキーにuser1の要素が存在したら、
    # その値をresに追加します。

        if user1[i] in hashmap:
            res += hashmap[user1[i]]

    return res == user2



    # hashmap = {}
    #
    # if len(user1) != len(user2):
    #     return False
    #
    # for i in range(len(user1)):
    #     if user1[i] not in hashmap and user2[i] not in hashmap.values():
    #         hashmap[user1[i]] = user2[i]
    #
    # res = ""
    # for x in user1:
    #     if x in hashmap:
    #         res += hashmap[x]
    #
    # return user2 == res



print(hasSameType("aabb", "yyza")) # --> false
print(hasSameType("aappl","bbtte")) # --> true
print(hasSameType("aappl","bbttb")) # --> false
print(hasSameType("aabb","abab")) # --> false
print(hasSameType("aappl","bktte")) # --> false
print(hasSameType("aaapppl","bbbttke")) # --> false
print(hasSameType("abcd","tso")) # --> false
print(hasSameType("abcd","jklm")) # --> true
print(hasSameType("aaabbccdddaa","jjjddkkpppjj")) # --> true
print(hasSameType("aaabbccdddaa","jjjddkkpppjd")) #  --> false



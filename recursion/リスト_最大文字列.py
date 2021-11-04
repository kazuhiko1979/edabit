"""
最大文字列
easy
Miles は英単語カードを持って勉強していましたが、手元にある単語を文字コードへ変換した時、最も大きい値が何になるか気になりました。英単語カード stringList が与えられるので、最も値が大きくなった単語が何枚目にあるかを返す maxAscilString という関数を定義してください（ここでは初めの値を 0 枚目とします）。ただし、以下の条件に気をつけてください。

- 文字列に含まれるそれぞれの文字を文字コードによって 10 進数へと変換し、足し合わせる。（例："abc" は文字コードによって、a = 97、b = 98、c = 99 へと変換され、全部足し合わせて 294 と計算されます）

　
- 大文字と小文字の区別はありません。（例：'A' == 'a' == 97となる）

関数の入出力例

入力のデータ型： string[] stringList

出力のデータ型： integer

maxAscilString(["Fantastic","Bridge","Superior","Fantastic","Operator"]) --> 0

maxAscilString(["HeLlo","HelLo","bridge"]) --> 2

maxAscilString(["eatDjrPNbj","IehUUSEMVe","hpcbBvlTOc","egvnPZgyCh"]) --> 3

maxAscilString(["egvnPZgyCh","bridge","Fantastic"]) --> 0
"""

def maxAscilString(stringList):
    # 最大値とそのインデックスを格納、0番目の文字列を初期値に設定
    maxValue = sumOfAscii(stringList[0])
    maxIndex = 0

    # 各文字列の文字コードの和を確認し、最大値を見つけます。
    for i, s in enumerate(stringList):
        # 文字コードの和を取得
        curr = sumOfAscii(s)
        # maxValueを超えたら更新します
        if maxValue < curr:
            maxValue = curr
            maxIndex = i
    return maxIndex
    # 文字列を文字コードの合計へ変換する関数
def sumOfAscii(string):
    # 文字列を小文字に変換し、各文字の文字コードをtotalに足します。
    total = 0
    for i in string.lower():
        total += ord(i)
    return total





    # res = []
    # stringList_index = 0
    #
    # while stringList_index < len(stringList):
    #     add_value = [int(str(ord(i.lower()))) for i in stringList[stringList_index]]
    #     res.append(sum(add_value))
    #     stringList_index += 1
    # return res.index(max(res))

print(maxAscilString(["Fantastic","Bridge","Superior","Fantastic","Operator"]))
print(maxAscilString(["HeLlo","HelLo","bridge"]))
print(maxAscilString(["eatDjrPNbj","IehUUSEMVe","hpcbBvlTOc","egvnPZgyCh"]))
print(maxAscilString(["egvnPZgyCh","bridge","Fantastic"]))
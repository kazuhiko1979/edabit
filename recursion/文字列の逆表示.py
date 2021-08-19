"""
Catherine は与えられた単語や文章を逆側から読み上げる遊びを友達とやっています。文字列 string が与えられるので、string を反転した文字列を返す reverseString という関数を再帰を使って定義してください。


関数の入出力例

入力のデータ型： string string

出力のデータ型： string

reverseString("abcd") --> dcba

reverseString("recursion") --> noisrucer

reverseString("I am a software engineer") --> reenigne erawtfos a ma I
"""


def reverseString(string):

    if len(string) == 1:
        return string
    else:
        buttom_string = string[-1]
        least_strings = string[:-1]

        return buttom_string + reverseString(least_strings)

print(reverseString("abcd"))
print(reverseString("I am a software engineer"))
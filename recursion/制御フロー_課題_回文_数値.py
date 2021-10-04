"""
Jack はある会社に入社し、新しい社員 ID を発行することになりました。ID は数字のみで作られ、
必ず回文でなければならないという制約がついています。新しい ID である自然数 n が与えられるので、
それが回文になっているかどうかを調べる isPalindromeInteger という関数を作成してください。

関数の入出力例

入力のデータ型： integer n
出力のデータ型： bool

isPalindromeInteger(12222) --> false
isPalindromeInteger(12321) --> true
isPalindromeInteger(22782) --> false
isPalindromeInteger(189981) --> true
isPalindromeInteger(1) --> true
isPalindromeInteger(987823) --> false
"""

# def isPalindromeInteger(n):

    # max_index = len(str(n)) - 1
    # res = []
    #
    # while max_index >= 0:
    #     res.append(str(n)[max_index])
    #     max_index -= 1
    #
    # return int(''.join(res)) == n

import math


def isPalindromeInteger(n):

    s = str(n)
    length = len(s)
    mid = math.floor(length / 2)

    for i in range(mid + 1):
        # i番目と反対側が等しいかどうかをチェック
        if s[i] != s[length - 1 - i]:
            return False

    return True


print(isPalindromeInteger(12222))
print(isPalindromeInteger(12321))
print(isPalindromeInteger(22782))
print(isPalindromeInteger(189981))
print(isPalindromeInteger(987823))




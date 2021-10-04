"""
パーフェクトナンバー
easy
Mayer は、6 と 6 以外の約数 1, 2, 3 を全てを足した値が一致することに気が付きました。
他にもあるのではないかと思い、同様の値を見つけようとしています。
自然数 n が与えられるので、1 から n のうち perfect number
（自然数 n と、その数自身を除く自然数 n の約数を全て足し上げたものが一致する値）を返す、
perfectNumberList という関数を作成してください。
perfect が存在しない場合は、none と返してください。

関数の入出力例

入力のデータ型： integer n
出力のデータ型： string

perfectNumberList(3) --> none
perfectNumberList(6) --> 6
perfectNumberList(28) --> 6-28
perfectNumberList(100) --> 6-28
perfectNumberList(496) --> 6-28-496
perfectNumberList(1000) --> 6-28-496
perfectNumberList(10000) --> 6-28-496-8128
"""

# def isPerfect(n):
#
#     sum = 1
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             sum = sum + i + n / i
#         i += 1
#
#     return True if sum == n and n != 1 else False
#
#
# def perfectNumberList(n):
#
#     res = []
#
#     for k in range(n+1):
#         if isPerfect(k):
#             res.append(str(k))
#     if not res:
#         return "none"
#     return '-'.join(res)

# ------------------------------------------------

import math

def perfectNumberList(n):
    numbers = ""
    for i in range(2, n+1):
        # パーフェクトナンバーのときだけ追加する
        if isPerfect(i):
            numbers += str(i) + '-'

    # 文字列が空のとき、つまりパーフェクトナンバーが存在しないときは、noneを返す
    # それ以外の時は、-を除いて返す
    return numbers[0:-1] if numbers != '' else 'none'


def isPerfect(x):
    # 以下の処理で1とxを除くので、あらかじめ1を足しておく
    divisors = 1
    n = math.ceil(math.sqrt(x))
    # 約数を足し上げる（1とxを除く）
    for i in range(2, n):
        if x % i == 0:
            # 割り切れるとき、その数とそのペアを足す
            divisors += i
            divisors += x / i
    # xと合計値が同じかどうかチェックする
    return x == int(divisors)


print(perfectNumberList(3))
print(perfectNumberList(6))
print(perfectNumberList(28))
print(perfectNumberList(100))
print(perfectNumberList(496))
print(perfectNumberList(1000))
print(perfectNumberList(10000))



# print(perfectNumberList(3))
# print(perfectNumberList(6))
# print(perfectNumberList(28))
# print(perfectNumberList(100))
# print(perfectNumberList(496))
# print(perfectNumberList(1000))
# print(perfectNumberList(10000))

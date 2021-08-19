"""
Juan は小学 1 年生の息子に足し算を教える方法として、桁数を分解して足し合わせるという方法を思いつきました。
自然数 digits が与えられるので、桁数を分解して足し合わせる、splitAndAdd という関数を再帰を使って作成してください。
例えば、98 は、9 + 8 = 17 となり、9728 は、9 + 7 + 2 + 8 = 26 となります。

splitAndAdd(19) --> 10
splitAndAdd(898) --> 25
splitAndAdd(23387) --> 23
splitAndAdd(1066) --> 13
splitAndAdd(546125) --> 23

ヒント
digit % 10 を使って末尾の数字を抜き出し、
digit / 10 と floor 関数（小数を切り捨てる関数）を使って末尾の桁を排除します。この処理を繰り返して解いてみましょう。
"""
import math

def splitAndAdd(digits):

    # new_list = list(str(digits))
    # return sum([int(i) for i in new_list])

    # recursive

    # ベースケース（1桁になるまで継続）
    if digits < 10:
        return digits
    return digits % 10 + splitAndAdd(math.floor(digits / 10))

print(splitAndAdd(898))
print(splitAndAdd(23387))

#

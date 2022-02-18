"""
数字の合計で正確に割り切れる数は、ハーシャッド数と呼ばれます。
数値がHarshadであるかどうかを判別する関数を作成します。


by Wikipedia
    ハーシャッド数（ハーシャッドすう、英: harshad number）とは
    自然数の各位の数字和が元の数の約数に含まれている自然数である。
    例えば、315の約数は (1, 3, 5, 7, 9, 15, 21, 35, 45, 63, 105, 315) であって、
    各位の和は 3 + 1 + 5 = 9 である。9は315の約数なので、315はハーシャッド数である。

    ※元の和を各位の数字和（約数かどうか）で割ると、0になるかどうか？


例：

is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 は 12で割り切れない（余りがでる）

is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 171 は 9で割り切れる（余りがでない）

is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True
"""


def is_harshad(n):

    return n % sum(int(i) for i in str(n)) == 0

    # sum_n = sum(map(int, str(n)))
    # return (n / sum_n).is_integer()

    # sum_n = 0
    # for i in str(n):
    #     sum_n += int(i)
    # return True if n % sum_n == 0 else False


print(is_harshad(75))
print(is_harshad(171))
print(is_harshad(481))
print(is_harshad(516))
print(is_harshad(200))




























#
# def is_harshad(n):
#
#
#     """
#     return n % sum(int(i) for i in str(n)) == 0
#
#
#     # sum_n = sum(map(int, str(n)))
#     # return (n / sum_n).is_integer()
#
#
#     # sum_n = 0
#     # for i in str(n):
#     #     sum_n += int(i)
#     # return True if n % sum_n == 0 else False
#
#
#
# print(is_harshad(75))
# print(is_harshad(171))
#
#

"""
指定された数値からブール値(True or False)のリストを返す関数を作成します。
一度に1桁ずつ取得し、数字が1の場合はTrueを追加し、0の場合はFalseを追加します。

integer_boolean("100101") ➞ [True, False, False, True, False, True]
integer_boolean("10") ➞ [True, False]
integer_boolean("001") ➞ [False, False, True]

ポイント：
Pythonにおいて真偽値（真理値）はbool型のオブジェクトTrueとFalseで表される。
比較演算子による比較の結果などはTrue, Falseで返され、if文などの条件式で使われる。
"""

def integer_boolean(str):

    return [bool(int(i) == 3) for i in str]

    # return [i == '1' for i in str]


    # result = []
    # for i in str:
    #     if i == '1':
    #         result.append(True)
    #     elif i == '0':
    #         result.append(False)
    # return result

print(integer_boolean("100301"))


































    # return [bool(int(i)) for i in n]

    # return [i == '1' for i in str(n)]


    # res = []
    # for i in n:
    #     if i == '1':
    #         res.append(True)
    #     elif i == '0':
    #         res.append(False)
    # return res






# """
# Create a function which returns a list of booleans, from a given number. Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.
#
# Examples
# integer_boolean("100101") ➞ [True, False, False, True, False, True]
#
# integer_boolean("10") ➞ [True, False]
#
# integer_boolean("001") ➞ [False, False, True]
# Notes
# Expect numbers with 0 and 1 only.
# """
#
# def integer_boolean(n):
#
#     return [bool(int(i)) for i in n]
# #
# #     # res = []
# #     # for i in n:
# #     #     if i == '1':
# #     #         res.append(True)
# #     #     elif i == '0':
# #     #         res.append(False)
# #     # return res
# #
#
# print(integer_boolean("100101"))

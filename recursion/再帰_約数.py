"""
天才小学生の Julia ちゃんは学校で出された約数を求める問題に対して
1 問 1 問素因数分解するのが面倒に感じたため、独自でプログラムを開発することにしました。
ある数値 number が与えられるので、number の約数を小さい順に返す
divisor という関数を再帰を使って定義してください。

関数の入出力例

入力のデータ型： integer number

出力のデータ型： string

divisor(28) --> 1-2-4-7-14-28

divisor(29) --> 1-29

divisor(720) --> 1-2-3-4-5-6-8-9-10-12-15-16-18-20-24-30-36-40-45-48-60-72-80-90-120-144-180-240-360-720
"""



def divisor(number):

    return divisorHelper(number, 1)

    # i = 1
    # table = []
    #
    # while i * i <= number:
    #     if number % i == 0:
    #         table.append(i)
    #         table.append(number//i)
    #     i += 1
    #
    # table = list(map(str, sorted(table)))
    # return '-'.join(table)

    # Recursive

def divisorHelper(number, i):
    # i が numberと等しくなった再帰を終了する
    if number <= i:
        return str(number)
    if number % i == 0:
        return str(i) + '-' + divisorHelper(number, i + 1)
    else:
        return divisorHelper(number, i + 1)


print(divisor(28))
# print(divisor(720))

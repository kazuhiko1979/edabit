"""
アサーション
アサーション（assertion）は、開発者がプログラムを意図的に停止させたり、
何かが正しくない場合にエラーを強制的に発生させたりすることができる、
シンプルかつ強力でよく使われるテストツールです。

アサーションは述語関数であり、アサーションが true を返す限り、プログラムは通常通りに実行を続けます。
一方、アサーションが false を返す場合は、アサーションエラーが発生し、プログラムのクラッシュおよび停止が行われます。
"""

# // エラーが発生した場合にメッセージをスローするAssertionクラスを作成します。
# 例外のスローについては、後で詳しく学習します。

# では、四捨五入のアルゴリズムを適用してエラーを解消してみましょう。
# 浮動小数点数ではなく文字列のように動作する 10 進数ライブラリを追加して、四捨五入を行います。

import decimal


def formatDecimal(num):
    # round関数は、バンカーズラウンディングを使用
    # result = int(round(num, 2) * 100)
    result = decimal.Decimal(str(num)).quantize(decimal.Decimal('.01'), \
                                                decimal.ROUND_HALF_UP) * 100
    print("rounding {}... {}".format(num, result))
    return result

assert(formatDecimal(86.258) == 8626)
assert(formatDecimal(86.253) == 8625)


# 四捨五入が目標
# しかし、Pythonのround関数は、バンカーズラウンディングを使用します。
assert(formatDecimal(20.355) == 2036)
assert(formatDecimal(20.345) == 2035)
assert(formatDecimal(54.075) == 5408)
assert(formatDecimal(54.065) == 5407)

assert(formatDecimal(54.775) == 5478)


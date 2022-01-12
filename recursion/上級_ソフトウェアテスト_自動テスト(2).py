"""
実行時エラー
実行時エラー（runtime error）とは、プログラム実行時に発生し、プログラム全体を即座にクラッシュさせるものを指します。プログラム実行時とは、コードが実行されている間のことを意味し、コードがコンパイルされた後、
あるいはコンパイラやインタプリタによってそれぞれ解釈された後のことになります。
これらのエラーは、コードが実行される前に発生するので、構文エラーではありません。
"""

# 実行時に間違ったインデックスにアクセスしてしまう例を見てみましょう。

# def accessFault(l):
#     # エラー。本来ならlen(l)であるはず。
#     return l[len(l)]
#
# print(accessFault([3,4,5,3,10,23]))

"""
動的言語は、型チェックがなく、データ型が混在した状態でのデータ操作が行われやすいため、実行時エラーが頻繁に発生します。
よくある例として、オブジェクト、文字列、整数等の異なるデータ型に対して、+ 演算子を使用してしまうことです。
他にも、オブジェクト参照が null のメンバ変数にアクセス演算子（object.member）を使用すると参照するものが何もなく、
実行時エラーが発生しまうことがあります。

その他の実行時エラーは、ユーザーとプログラムとのやりとりによっても発生します。
例えば、accessFault のシナリオで、ユーザーがインデックスを入力したり、ハッシュマップでキーを入力できるという状況下で、
プログラムの入力範囲内の値を入力しなかった場合、システムがクラッシュしてしまう可能性があります。

コード内でエラーが発生した場合、プログラミング言語は、セキュリティ対策としてシステムを強制的に停止させてクラッシュさせます。
例として、中級「再帰」の節で学習した、x の平方根を推定する再帰的な計算である squareRoot 関数を見てみましょう。
この関数は常に正の整数を返します。負の数が渡された場合、負の数の平方根は虚数になりますが、
関数の出力が他の整数を入力として受けとる計算に使われるため、この関数は -1、False、NaN、null を返すことはできません。
同様に関数が 0 を返す場合も正しくありません。それは、0 の squareRoot だけが 0 を返すべきであり、致命的な問題を引き起こすためです。

その場合、実行時エラーであるアサーションエラーが発生しますが、独自のカスタムエラーを発生させることによって対処してみましょう。
"""

class SquareRootError(Exception):
    pass

# xの平方根を小数点6桁以下を丸めて返します。
def squareRoot(x):
    # xが0の時、0を返します。
    if x == 0:
        return 0

    # 負の数値に対してはエラーを発生させます。
    # Pythonでは多くのエラーを消します。NameError, AssertionError, EOFError, FloatingPointError, IndexError etc
    # ここでは例外クラスを継承したSquareRootError(Exception)というクラスを作成して、独自のエラーを定義します。
    # エラーを発生させるために、raiseキーワードを使用し、例外を定義するクラスで従います。
    if x < 0:
        raise SquareRootError

    def isSquareRootCloseEnough(a, b):
        return abs(a / b - b) < (b * 0.000001)

    def squareRootHelper(x, guess):
        if isSquareRootCloseEnough(x, guess):
            return round(guess, 5)
        return squareRootHelper(x, (guess + x / guess) / 2)

    return squareRootHelper(x, 1)

print(squareRoot(65))
print(squareRoot(4))
print(squareRoot(25))
print(squareRoot(16))
print(squareRoot(36))
print(squareRoot(353))

print(squareRoot(-9))



















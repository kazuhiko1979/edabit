"""
例外
処理がエラーを引き起こし、開発者が実行時にエラーを対処することができる場合、
このエラーは例外（exception）と呼ばれます。関数がエラーや例外を吐くことができる場合、
その関数にスローアブル（throwable）が含まれていると表現されます。
"""

"""
エラーの場合、開発者は実行時にその問題に対して何もできず、プログラムがクラッシュしてしまいます。
これは致命的なエラー（fatal error）と呼ばれます。一方、例外の場合は、実行時に問題を処理することができます。

例外を吐く関数の処理を考えてみましょう。正常に動作し、何もエラーがなければ、コードは通常通りに動作し続けます。
しかし、仮に例外が吐かれ、その例外を処理している場合、例外をキャッチしていると表現されます。
この処理は try-catch 文と呼ばれる制御フローによって行われます。

スローアブルを含む関数の呼び出しが try-catch 文でラップされていない場合、例外処理をしないという選択を取ったとみなされ、
実行された関数が例外を吐くと自動的に致命的なエラーになります。
この制御フローの仕組みによって、開発者が例外を上手く処理したり、例外をエラーとして処理することができます。

例えば、スローアブルな関数 squareRoot は、負の整数を入力として受け取った時にエラーを吐きます。
仮に、他の開発者がこの関数を使用したい際には、その開発者にどのようにエラーに対処するか委ねることができます。
例外として処理するか、致命的なエラーとして処理するかはこの開発者によることになります。

では、関数の呼び出し squareRoot(-9) を try-catch 文で囲み、例外をキャッチすることでコードを拡張してみましょう
。今回、squareRoot が全く重要な役割を持っておらず、存在しなくても特に何も発生しないと仮定し、
致命的なエラーを発生させずに例外として処理します。
"""

class SquareRootError(Exception):
    pass


def squareRoot(x):
    if x == 0:
        return 0

    # 例外をインスタンスオブジェクトとしてメッセージと共に渡すこともできます。
    if x < 0:
        raise SquareRootError(f"Square root error for the squareRoot function, line, 48!!!" \
        f"This function cannot contain a negative integer and {x} was passed in!")

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

# try-catch文の周りで、例外エラーを返す可能性があるステートメントをラップします。
# Pythonではcatchの代わりに[except]キーワードが使われます。except {ExceptionName].

# tryの中で以下の分を実行してい見てください。
try:
    print(squareRoot(-9)) # Error

# tryに失敗した場合は例外をキャッチします。
# キャッチしようとしているのはSquareRootErrorです。制御フローはこのインスタンスオブジェクトを作成し、errに割り当てます。

except SquareRootError as err:
    # エラーは発生しません。試したステートメントが重要でないことがわかります。
    # 致命的なエラーを起こさずに、起きたことをログ情報にして、プログラムを実行し続けます。
    print("Error occured and it looks like it was a SquareRoot Error..." + str(err))

print(squareRoot(90))
print(squareRoot(81))
print(squareRoot(54442))


try:
    print(squareRoot(-456))

except Exception as err:
    print("Error occured and it looks like it was an I am not sure, this is a generic exception with the message:" + str(err))








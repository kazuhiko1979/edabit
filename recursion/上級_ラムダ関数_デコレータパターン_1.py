"""
デコレータパターン
ソフトウェアを構築する際、コードの設計やリファクタリングは重要な作業です。
開発者は、一般的なプラクティスやパターンに従って、問題を効率的に解決しようとします。
デザインパターン（design pattern）とは、頻繁にテストされ、
採用されるソフトウェア設計の中でよく発生する問題に対して再利用可能な解決策のことを指します。
これらは、ソフトウェアを構築する際に開発・識別された抽象化に対するラベルのようなものであり、
言語ライブラリやフレームワークで一般的に提供・採用されています。

これらのラベルの一つに、デコレータパターン（decorator pattern）というものがあります。
特定のオブジェクトに動的に機能を変更したり追加したりするものをデコレータ（decorator）と呼びます。

では、デコレータを使って呼び出し可能オブジェクトに機能を追加していきます。今回のケースでは、デコレータは関数になります。
この関数は関数を取り込み、その関数に新しい機能を追加します。

簡単な例を使って、これを試してみましょう。
零項関数（入力を受け取らない関数）f を取り込み、f を実行する前に "runing f..." を表示する新しい関数（新しい機能が追加された関数 f）を返します。
"""

def simpleDecorator(f):
    def inner():
        print("Running f....")
        return f()
    return inner()

def helloword():
    return "Hello world"

newFunc1 = simpleDecorator(helloword)
print(newFunc1)

newFunc2 = simpleDecorator(lambda : "Hello Jupiter")
print(newFunc2)

# 単項関数 (unary function) fを受け取り、新しい機能が追加された関数fを作成
# 実行するたびにタイマーを使用し、fの実行時間がどれくらいを計算します。

import datetime


def timerDecorator(f):
    def function(arg):
        start = datetime.datetime.now()
        print(start)
        result = f(arg)
        end = datetime.datetime.now()
        print("This function took: " + str(end-start) + "ms")
        return result
    return function

# O(1)
print(timerDecorator(lambda x: x*2)(2424))

# 0(n^2)
def on2func(x):
    finalResult = 1
    for i in range(x):
        result = i
        for j in range(i):
            result += j
        finalResult += result
    return finalResult

# print(timerDecorator(on2func)(10000))


# O(2^2)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# O(n)
def fibonacciFast(fib1, fib2, n):
    if n <= 0:
        return fib1
    return fibonacciFast(fib2, fib1+fib2, n-1)


timeFibonacci = timerDecorator(fibonacci)
print(timeFibonacci(20))


timeFibonacciFast = timerDecorator(lambda n: fibonacciFast(0, 1, n))
print(timeFibonacciFast(20))

# capitalizeDecorator:
# 文字列を受け取る単項関数 f を受け取り、入力されされた先頭文字を大文字にする機能を追加して、f を返します。
def capitalizeDecorator(f):
    def func(str):
        str = str[0].upper() + str[1:]
        result = f(str)
        return result
    return func

print(capitalizeDecorator(lambda str: str + " world!")("hello"))

# lowercaseResultDecorator:
# 文字列を受け取る単項関数 f を受け取り出力を小文字にする機能を追加して、f を返します。
def lowercaseResultDecorator(f):
    def func(str):
        str = str.lower()
        result = f(str)
        return result
    return func

print(lowercaseResultDecorator(lambda str: str + " world!")("HELLO"))

# printInfoDecorator:
# 2つの入力を受け取る関数 f を受け取り、結果を返す前に、f の引数と出力を、コンソール上に出力するを追加してfを返します。

def printInfoDecorator(f):
    def func(input1, input2):
        print("input1: " + input1)
        print("input2: " + input2)
        result = f(input1, input2)
        return result
    return func

print(printInfoDecorator(lambda str1, str2: "[" + str1 + "," + str2 + "]")("Hello", "world"))


# simple decorator
def simpleDecorator(str1, str2):
    s = str1[::1]
    s += str2
    return s
myFunc = printInfoDecorator(simpleDecorator)

print(myFunc("Thunder", "Ranger"))

# decorator syntax
@printInfoDecorator
def decoratorSyntax(x, y):
    result = x + y
    # result = int(x) + int(y)
    return result

print(decoratorSyntax("2", "3"))
print(decoratorSyntax("Thunder", "Ranger"))
















# 数字のカウント
def countUpToNWhile(n):

    i = 0

    while i < n:
        print(i)
        i = i + 1

# countUpToNWhile(15)


# フラグを使った総和計算
def summationWhileLoopIterationFlag(n):

    flag = True
    total = 0

    while flag:
        total += n
        n = n - 1

        if n < 0:
            flag = False

    return total

# print(summationWhileLoopIterationFlag(10))

# 最大公約数GCD(ユークリッド互除法）

# 再帰
def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


# while方法１
def gcdwhileLoopIteration(n1, n2):
    while n1 % n2 != 0:
        prevN1 = n1
        n1 = n2
        n2 = prevN1 % n2

    return n2

# while方法2
def gcdWhileLoopIterationFlag(n1, n2):

    found = False

    while not found:

        if n1 % n2 == 0:
            found = True
        else:
            prevN1 = n1
            n1 = n2
            n2 = prevN1 % n2

    return n2


# while方法3
def gcdWhileLoopIterationReturn(n1, n2):
    # ブロック文の中でreturnが返されるまで繰り返し処理を実行します
    while True:
        # 最大公約数が見つかり次第、n2を返します
        if n1 % n2 == 0:
            return n2
        else:
            prevN1 = n1
            n1 = n2
            n2 = prevN1 % n2

# print(gcd(44, 242))
# print(gcdwhileLoopIteration(44, 242))
# print(gcdWhileLoopIterationFlag(44, 242))
# print(gcdWhileLoopIterationReturn(44, 242))

# 平方根の推定

def isSquareRootCloseeEnough(a, b):
    # 近似精度が0.1未満であればtrueを返し、
    # 0.01%以上であればfalseを返します。
    return abs(a / b - b) < b * 0.0001

# x / guessを計算します。
# もしx / guessがguessに近ければ、guessを返します。
# そうでない場合は、条件により近い推定値guessを探します。
def squareRootWhile(x):
    # xから推定値をスタートします
    squareRoot = x

    # 条件を満たすまで繰り返し推定値を探し続けます。
    while not isSquareRootCloseeEnough(x, squareRoot):
        # 新しい推定値を格納します
        squareRoot = (squareRoot + x / squareRoot) / 2

    return squareRoot

# print(squareRootWhile(10))


# 例題1
# 自然数nが与えられるので、1からnまで文字列として出力するfizzbuzzという
# 関数をwhile文を使って作成してください。
# ただし、3の倍数の時にはfizz、5の倍数の時にはbuzz、
# 15の倍数の時にはfizzbuzzと出力してください。

def fizzbuzz(n):

    n_start = 1

    while n_start <= n:
        if n_start % 15 == 0:
            print("fizzbuzz")
        elif n_start % 5 == 0:
            print("buzz")
        elif n_start % 3 == 0:
            print("fizz")
        else:
            print(n_start)

        n_start += 1

# fizzbuzz(15)
# fizzbuzz(36)


# 例題2
# 自然数digitsが与えられるので、桁数を分解して足し合わせる、
# splitAndAddという関数をwhile文を使って作成してください。
import math

def splitAndAdd(digit):

    # while digit < 10:
    #     return digit
    # return digit % 10 + splitAndAdd(math.floor(digit / 10))

    total = 0

    while digit >= 10:
        total += digit % 10
        digit //= 10

    return total + digit

# print(splitAndAdd(19))
# print(splitAndAdd(23387))
# print(splitAndAdd(546125))

# 例題3
# 数字を1桁ずつ分解して、それぞれの値を合計し、
# その値が1桁になるまで同じ作業を繰り返した時、
# それぞれの合計値を足し合わせて得られる値を返す、
# whileDigitsAddedという関数を例題2を使って作成してください。

def whileDigitsAdded(digits):

    total = 0

    while splitAndAdd(digits) > 10:
        digits = splitAndAdd(digits)
        total += digits

    return total + splitAndAdd(digits)

print(whileDigitsAdded(5462))
print(whileDigitsAdded(45622943))
print(whileDigitsAdded(9514599))





















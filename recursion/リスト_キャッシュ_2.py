"""
n 未満の全ての素数を求めてみましょう。ここでは、エラトステネスのふるいと呼ばれる古典的なアルゴリズムを使用します。このアルゴリズムにはキャッシュが不可欠です。


エラトステネスのふるいにはいくつかのステップがあります。

1. サイズ n のブーリアン値 true のリストを生成します。
2. 最初の素数を 2 と設定します。
3. 1~n の中から 2 で割り切れるものを全て false にします。
4. 素数 3 に対しても同じ処理を行います。
5. これを √n まで繰り返します。
6. キャッシュ内に残った全ての真の値のインデックスは素数になります。
"""

import math

# エラトステネスのふるいのアルゴリズム
def allPrimesSieve(n):
    # サイズnのブーリンアン値trueを持つリストを生成します。キャッシュ
    cache = [True] * n
    # ステップを✓n回繰り返します。nが素数でないと仮定すると、n = a * bと表すことができるので
    # aとbの両方が✓n以上になることはありえません。
    # したがって、✓n * ✓n = は最大合成組み合わせになります。
    for currentPrime in range(2, math.ceil(math.sqrt(n))):
        # キャッシュ内の素数(p)の倍数をすべてfalseにしていきます。
        # iは2からスタートします。
        if not cache[currentPrime]:
            continue
        i = 2
        ip = i * currentPrime
        while ip < n:
            cache[ip] = False
            # i*pをアップデートします。
            i += 1
            ip = i * currentPrime

    # キャッシュ内のすべてのtrueのインデックスは素数です。
    primeNumbers = []
    # enumerateは現在の位置のペアの値を返します。
    for index, predicate in enumerate(cache):
        if predicate:
            primeNumbers.append(index)
    return primeNumbers[2:]

print(allPrimesSieve(53))


def sumPrimeUpToN(n):
    n = n + 1
    # サイズnのブーリンアン値trueを持つリストを生成します。キャッシュ
    cache = [True] * n
    # ステップを✓n回繰り返します。nが素数でないと仮定すると、n = a * bと表すことができるので
    # aとbの両方が✓n以上になることはありえません。
    # したがって、✓n * ✓n = は最大合成組み合わせになります。
    for currentPrime in range(2, math.ceil(math.sqrt(n))):
        # キャッシュ内の素数(p)の倍数をすべてfalseにしていきます。
        # iは2からスタートします。
        if not cache[currentPrime]:
            continue
        i = 2
        ip = i * currentPrime
        while ip < n:
            cache[ip] = False
            # i*pをアップデートします。
            i += 1
            ip = i * currentPrime

    # キャッシュ内のすべてのtrueのインデックスは素数です。
    primeNumbers = []
    # enumerateは現在の位置のペアの値を返します。
    for index, predicate in enumerate(cache):
        if predicate:
            primeNumbers.append(index)
    return sum(primeNumbers[2:])

print(sumPrimeUpToN(53))
print(sumPrimeUpToN(89))
print(sumPrimeUpToN(97))










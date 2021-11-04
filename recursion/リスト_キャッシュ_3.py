# 末尾再帰を使って、n番目のフィボナッチを返す関数を作成します。
def fibonacciNumberTailHelper(fn1, fn2, n):
    if n < 1:
        return fn1

    return fibonacciNumberTailHelper(fn2, fn1 + fn2, n-1)

def fibonacciNumber(n):
    # この関数が1つのパラメータを受け取れるように、ヘルパー関数を使います。
    # そうすることによって、関数の再利用をより簡単に行うことができます。
    # 0と1からスタートします。
    return fibonacciNumberTailHelper(0, 1, n)

# print(fibonacciNumber(20))
# print(fibonacciNumber(50))

# メモ化は、ツリー構造が上から下へと続くアルゴリズムでのキャッシングです。
# フィボナッチのツリーを見てみると、nから始まり、n-1、n-2、n-3と下に向かって計算していきます。
def memoizationFib(totalFibNumbers):
    # これはキャッシュではあり、すでに計算したフィボナッチ数をすべて保存します。全てをNoneに設定してください。
    cache = [None] * (totalFibNumbers+1)

    # キャッシュを更新するには、このローカルスコープ内の関数を使用します。
    def innerMemoizationFib(n):
        # キャッシュされていないフィボナッチ数を処理するだけです。
        # フィボナッチのnを再帰的に計算し、キャッシュに追加します。
        if cache[n] is None:
            if n == 0:
                cache[n] = 0
            elif n == 1:
                cache[n] = 1
            else:
                cache[n] = innerMemoizationFib(n - 1) + innerMemoizationFib(n - 2)

        # フィボナッチはすでに計算されているのでただ返すだけで問題ありません。
        return cache[n]
    return innerMemoizationFib(totalFibNumbers)

# print(memoizationFib(50))

"""
反対に、ツリー構造の結果を下から上にキャッシュする方法もあり、
動的計画法では一般的なやり方です。
"""

# タビュレーションは、ツリー構造が下から上へと続くアルゴリズムでのキャッシングです。
# フィボナッチ5のツリーを見ると、0から始まり、上に向かって計算が行われます。
# fib1...fib2...fib3...fibn
# タビュレーションは、ほとんどの場合、不必要な計算がないため、メモ化よりもはるかに効果的です。
def tabulationFib(n):
    # これはキャッシュであり、計算済みのフィボナッチ数をすべて保存します。全てを0に設定します。
    cache = [0] * (n+1)
    # キャッシュの最初の2つは0と1です。fib0は0、fib1は1であり、他のすべての数字は
    # fib(n) = fib(n-1) + fib(n-2)となります
    cache[0] = 0
    cache[1] = 1

    # 再帰の代わりに反復を使用します。0,1,2,3,....nから始まります。
    # 2からnまでのすべてのfib数を計算します。
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]

    # n番目のフィボナッチを返します。
    return cache[n]

print(tabulationFib(50))
















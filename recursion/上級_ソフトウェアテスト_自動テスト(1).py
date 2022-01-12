"""
自動テスト(1)
自動テスト（automatic test）では、QA チームのメンバーや開発者がスクリプトを書き、専用のソフトウェアを使用してエラーの識別を自動化します。
多くの場合、QA テスターの専門チームによって行われ、実際のコードの実装とは別に行われます。

例を使って、自動テストの利点を探ってみます。
n までの素数を取り出すためにエラトステネスのふるいを使った関数から始めましょう。
このアルゴリズムを検証する自動テストを作成します。
このテストは、リスト内のすべての項目が素数であるかどうか、すべてが重複していないか、すべてが n 以下であるかどうか、
そして k 個の素数が含まれているかどうかのチェックを行います。
では、100 までの素数をテストしてみましょう。100 未満の素数は全部で 25 個あるはずです。
"""

import math

def assertionTest(a, callback):
    result = callback(a)
    print(f"Chcecking againt {str(a)}, is it valid?... {result}")
    assert result
    return True

def sieveOfPrimes(n):

    # primeNumbers = []
    # for i in range(2, n):
    #     for j in range(2, i):
    #         if i % j == 0:
    #             break
    #     else:
    #         primeNumbers.append(i)
    # return primeNumbers

    cache = [True] * n
    for currentPrime in range(2, math.ceil(math.sqrt(n))):
        i = 2
        ip = i * currentPrime
        while ip < n:
            cache[ip] = False
            i += 1
            ip = i * currentPrime


    primeNumbers = []
    for index, predict in enumerate(cache):
        if predict:
            primeNumbers.append(index)
    # print(primeNumbers[2:])
    return primeNumbers[2:]

# kとnを受け取り、リストAを取り込み、A内のすべての要素が重複しておらず、かつn以下の素数であり、
# 合計でk個存在するかチェックする関数を返します。
# 返されるデータはクロージャー関数です。
def primeCheck(k, n):
    def isPrime(num):
        if num > 1:
            for i in range(2, math.floor(math.sqrt(num))):
                if (num % i) == 0:
                    return False
            return True
        return False

    def script(aList):
        # set()はリストを受け取り、重複していない要素のみを返します。
        if not len(set(aList)) == len(aList):
            return False
        if not len(aList) == k:
            return False

        for i in range(len(aList)):
            if aList[i] > n or not isPrime(aList[i]):
                return False
        return True

    return script

# True
assertionTest([2, 3, 5, 7, 11, 13],primeCheck(6, 15))
assertionTest(sieveOfPrimes(15),primeCheck(6, 15))
assertionTest(sieveOfPrimes(100),primeCheck(25, 100))

# False
assertionTest([2,3,5,7,11,13,15],primeCheck(6, 15)) # Error
assertionTest([2,3,5,7,11,12],primeCheck(6, 15)) # Error
assertionTest([2,3,5,7,11,19],primeCheck(6, 15)) # Error








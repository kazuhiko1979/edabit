"""
素数の和
easy
ある国は長く存続できたことに感謝を込め、国民に給付金を渡そうと考えました。そこで、建国から経過した年数 n までに含まれている、全ての素数を足した数を給付金にする予定です。自然数 n が与えられるので、給付金の額を返す sumOfAllPrimes という関数を作成してください。

関数の入出力例

入力のデータ型： integer n

出力のデータ型： integer

sumOfAllPrimes(1) --> 0
sumOfAllPrimes(2) --> 2
sumOfAllPrimes(3) --> 5
sumOfAllPrimes(100) --> 1060
sumOfAllPrimes(1000) --> 76127
"""

# def sumOfAllPrimes(number):

    # res = []
    #
    # for i in range(2, number+1):
    #     for j in range(2, i):
    #         if i % j == 0:
    #             break
    #             res.append(i)
    #     else:
    #         res.append(i)
    # return sum(res)


def sumOfAllPrimes(n):

    sumOfPrimes = 0 # 素数の合計

    # k番目の値が素数か調べます。
    for k in range(2, n + 1):
        if isPrime(k):
            sumOfPrimes += k

    return sumOfPrimes

# 素数か判定する関数
def isPrime(number):
    # 2からnumber-1までの値で割り切れる数があればfalseを返します。
    for i in range(2, number):
        if number % i == 0:
            return False
    # numberが１の場合はfalseを返します
    return number > 1


print(sumOfAllPrimes(1))
print(sumOfAllPrimes(2))
print(sumOfAllPrimes(3))
print(sumOfAllPrimes(4))
print(sumOfAllPrimes(100))
print(sumOfAllPrimes(1000))




"""
素数の個数
easy
Eric はとある組織に囚われの身となっており、ある条件を満たせば自由になれる約束をしていました。それは、整数 n が与えられたときに n 未満に何個素数があるか正確に答えることでした。整数 n が与えられるので、n 未満に含まれる素数の個数を返す、primesUpToNCount という関数を定義してください。

関数の入出力例

入力のデータ型： integer n

出力のデータ型： integer

primesUpToNCount(2) --> 0

primesUpToNCount(3) --> 1

primesUpToNCount(5) --> 2

primesUpToNCount(13) --> 5

primesUpToNCount(18) --> 7

primesUpToNCount(89) --> 23

primesUpToNCount(97) --> 24

primesUpToNCount(100) --> 25

primesUpToNCount(367) --> 72

primesUpToNCount(673) --> 121

primesUpToNCount(1000) --> 168

primesUpToNCount(3406) --> 478

primesUpToNCount(20034) --> 2266

for 文を 2 回使って解くこともできますが、計算量を少なくして解きたい場合はキャッシュ（エラストテネスのふるい）を使いましょう。
"""
import math

def primesUpToNCount(n):
    # primes sieves
    bigList = [0] * (n+1)
    print(bigList)
    primes = []
    i = 2
    while i < n:
        if bigList[i] == 0:
            j = 1

            while i*j <= n:
                bigList[i*j] = 1
                j += 1
            primes.append(i)
            print(primes)
        i+=1

    return len(primes)



    # O(n^2)


    # results = list(filter(lambda x: isPrime(x), range(n)))

    # results = [x for x in range(0, n) if isPrime(x)]

    # for x in range(0, n):
    #     if isPrime(x):
    #         results.append(x)

    # return len(results)



# def isPrime(num):
#
#     for x in range(2, num):
#         if num % x == 0:
#             return False
#     return num > 1


    # primes = [True] * n
    #
    # # 0と1を除去するため予め countには2を入れておきます。
    # count = 2
    # # math.sqrt : 平方根
    # for i in range(2, math.ceil(math.sqrt(n))):
    #
    #     p = 2
    #     while i * p < n:
    #         if primes[i*p]:
    #             count += 1
    #         primes[i*p] = False
    #         p +=1
    # return len(primes) - count




    # p = [i for i in range(n)]
    #
    # for i in p[3:]:
    #     if p[i] % 2 == 0:
    #         p[i] = 0
    #
    # root_n = n ** 0.5
    #
    # for i in range(3, n):
    #     if i > root_n:
    #         break
    #     if p[i] != 0:
    #         for j in range(i, n + 1, 2):
    #             if i * j > n:
    #                 break
    #             p[i * j] = 0
    # return len(sorted(list(set(p))[2:]))

# print(primesUpToNCount(2))
# print(primesUpToNCount(3))
# print(primesUpToNCount(5))
print(primesUpToNCount(13))
# print(primesUpToNCount(18))
# print(primesUpToNCount(89))
# print(primesUpToNCount(97))
# print(primesUpToNCount(100))
# print(primesUpToNCount(367))
# print(primesUpToNCount(673))
# print(primesUpToNCount(1000))
# print(primesUpToNCount(3406))
# print(primesUpToNCount(20034))





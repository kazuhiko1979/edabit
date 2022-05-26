# def countFlags(n):
#
#     count = 0
#     while n > 0:
#         count += 1
#         n = n & (n-1)
#     return count
#
#     # v1
#     # count = 0
#     # n_bin_length = len(bin(n))
#     #
#     # while n_bin_length > 2:
#     #     count += bin(n & 1).count("1")
#     #     n = bin(n >> 1)
#     #     n = int(n, 2)
#     #     n_bin_length = len(bin(n))
#     #     if n == 0:
#     #         return count
#     # return count
#
# print(countFlags(5)) #2
# print(countFlags(7)) #--> 3
# print(countFlags(11)) # --> 3
# print(countFlags(32))
# print(countFlags(203444343))
# print(countFlags(2147483647))

import math

# def frogPosition(leaves, jumps, start):
#
#     position = start + jumps
#     if position % leaves == 0:
#         return leaves
#     else:
#         return position % leaves
#
#     # return ((jumps+start-1 % leaves) + leaves) % leaves + 1
#
# print(frogPosition(4,3,1))
# print(frogPosition(4,6,2))
# print(frogPosition(4,-3,1))
# print(frogPosition(4,-5,1))

# count = 0
#
# def towerOfHanoi(discs):
#     if count != 0:
#         count = 0
#     global count
#     if discs > 1:
#         towerOfHanoi(discs-1)
#         count += 1
#         towerOfHanoi(discs-1)
#     else:
#         count += 1
#
#     return count

# def towerOfHanoi(discs):
#
#     return towerOfHanoiHelper(1, discs)
#
# def towerOfHanoiHelper(fn1, discs):
#     if discs <= 1:
#         return fn1
#     return towerOfHanoiHelper(2*fn1+1, discs-1)

# def towerOfHanoi(discs):
#     # ベースケース
#     if discs == 1:
#         return 1
#
#     # left -> right にn-1枚を動かす
#     leftToRight = towerOfHanoi(discs - 1)
#
#     # left -> middle に最後の円盤を動かす
#     leftToMiddle = 1
#
#     # right -> middle にn-1枚を動かす。値はleftToRightと同じ
#     rightToMiddle = leftToRight
#
#     return leftToRight + leftToMiddle + rightToMiddle
#
#
# print(towerOfHanoi(1))
# print(towerOfHanoi(2))
# print(towerOfHanoi(3))
# print(towerOfHanoi(5))

def recursiveArtihmetic(start, n, d):
    if n <= 1:
        return start

    return recursiveArtihmetic(start, n-1, d) + d

# print(recursiveArtihmetic(2, 10, 3))

def sumOf_even_and_add(lst):

    even = []
    add = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            add.append(i)
    return f'偶数合計: {sum(even)} 奇数合計: {sum(add)}'



def numberOfWay(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return numberOfWay(n-1) + numberOfWay(n-2)


# def kthElement(n,k):
#
#     return kthElementHelper(n, k, 0, "")
#
# def kthElementHelper(n, k, count, element):
#     if count == n:
#         return element[k-1]
#     if count == 0:
#         return kthElementHelper(n, k, 1, "0")
#     if count == 1:
#         return kthElementHelper(n, k, count+1, element + "1")
#
#     print(element[len(element)//2:len(element)])
#     return kthElementHelper(n, k, count + 1, element + element[(len(round(element/2)):len(element)]) + element[0:(len(element)//2)]

def kthElement(n, k) -> int:
    if n == 1:
        return 0

    if k % 2 == 0:
        if kthElement(n-1, k/2) == 0:
            return 1
        else:
            return 0
    else:
        if kthElement(n-1, (k+1)/2) == 0:
            return 0
        return 1


# def minTiles(n,m):
#     return minTilesHelper(n, m, 0)
#
# def minTilesHelper(n,m, tileCount):
#     if n == 0 or m == 0:
#         return tileCount
#
#     # nが奇数
#     if n % 2 != 0:
#         tileCount += m
#         n -= 1
#     # mが奇数
#     elif m % 2 != 0:
#         tileCount += n
#         m -= 1
#
#     # 共に偶数
#     else:
#         n /= 2
#         m /= 2
#     return minTilesHelper(n,m, tileCount)

def minTiles(n, m):

    # ベースケース
    if m == 0 or n == 0:
        return 0

    # 両辺とも2で割り切れる場合、f(n,m) = f(n/2, m/2)が成り立つ
    if n % 2 == 0 and m % 2 == 0:
        return minTiles(n/2, m/2)

    # nのみ奇数の場合、nから横一列分切り取ると両辺を2で割ることができる
    # したがって、f(n,m) = m + f(n-1/2, m/2)となります。
    elif n % 2 != 0 and m % 2 == 0:
        return m + minTiles((n-1)/2, m/2)

    # mのみが奇数の場合、mから縦一列分とると両辺を2で割ることができます。
    # したがって、f(n,m) = n + f(n/2, m-1/2)となります。
    elif n % 2 ==0 and m % 2 != 0:
        return n + minTiles(n/2, (m-1)/2)

    # n,mの両方が奇数の場合、nの1列分とmの1列分を切り取ると両辺を2で割ることができます。
    # f(n,m) = n + m - 1 + f((n-1)/2, (m-1)/2)
    else:
        return n + m - 1 + minTiles((n-1)/2, (m-1)/2)

def conbinationsOfParenthesis(num):

    if num <= 1:
        return 1
    ans = 0
    for i in range(0, num):
        ans += conbinationsOfParenthesis(i) * conbinationsOfParenthesis(num-i-1)
    return ans





# def conbinationsOfParenthesis(num):
#     generateParanthesisHelper(num, 0, 0, "", [])

# def conbinationsOfParenthesis(n):
#
#     combinationsOfParenthesisHelper(n, 0, 0, "", [])
#
# def combinationsOfParenthesisHelper(n, Open, close, s, ans):
#
#     if Open == n and close == n:
#         ans.append(s)
#         return ans
#
#     if Open < n:
#         combinationsOfParenthesisHelper(n, Open + 1, close, s + "{", ans)
#
#     if close < Open:
#         combinationsOfParenthesisHelper(n, Open, close + 1, s + "}", ans)

    # if Open == 0 and close == 0:
    #
    #     result = len(ans)
    #     return result

# print(conbinationsOfParenthesis(3))
# print(conbinationsOfParenthesis(5))
# print(conbinationsOfParenthesis(7))


# print(conbinationsOfParenthesis(3))

import math
from math import factorial

def getRoutes(row, col):
    if row == 1 or col == 1:
        return 1
    return getRoutes(row-1, col) + getRoutes(row, col-1)

if __name__ == '__main__':
    print(getRoutes(3, 6))
    print(getRoutes(6, 3))
    print(getRoutes(2, 84))

    # print(recursiveArtihmetic(2, 10, 3))
    # print(sumOf_even_and_add([10,13,14,15,20,27,30]))
    # print(numberOfWay(1))
    # print(numberOfWay(2))
    # print(numberOfWay(3))
    # print(numberOfWay(4))
    # print(numberOfWay(5))

    # print(kthElement(4,5))
    # print(kthElement(2,1))
    # print(kthElement(2,2))
    # print(kthElement(4,6))

    # print(minTiles(10,5))
    # print(generateParenthesis(1, 0, 0, "", []))
    # print(generateParenthesis(3, 0, 0,"",[]))
    # print(generateParenthesis(5, 0, 0, "", []))
    # print(generateParenthesis(7, 0, 0, "", []))
    # print(generateParenthesis(8, 0,0,"",[]))


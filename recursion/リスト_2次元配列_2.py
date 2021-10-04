# 2次元配列_2

"""
Amazon などのウェブサイトで、商品を購入する際、カート決済で、個々の州税、連邦税、輸入税、
クーポン割引などを計算する処理を、double 型を持つ配列を使って考えてみます。

メインの配列には、各商品を格納します。個々の製品を表す配列には、商品の価格を最初のスロットに格納し、
残りのスロットにはクーポン割引、各製品の州税、連邦税、輸入税を表す、% を格納します。
反復処理を行って、各商品の価格を計算し、商品の総額に加算します。
"""

def getTotalForProductList(product2dPriceList):
    finalTotal = 0
    for priceList in product2dPriceList:
        price = priceList[0]
        total = price
        # 最初の値の後に開始
        for multiplier in priceList[1:]:
            total += price * multiplier
        # finalTotalを足していきます。
        print("Total for current items is " + str(total))
        finalTotal += total
    return finalTotal


#　商品の配列 - 商品の価格、クーポン割引、各製品の州税、連邦税、輸入税を表す、% を格納
product1 = [100, 0.1, 0.02, 0.03, 0.02]
product2 = [50, -0.5, 0.1, 0.05, 0.02]
product3 = [34, 0.05, 0.2, 0.03, 0.1]
product4 = [10, -0.2, 0.3, 0.05, 0.03]


# # shopping cartは全てのアイテムを含んでいる、2次元配列
# shppingCartArray = [product1, product2, product3, product4]
# print(getTotalForProductList(shppingCartArray))

# 例題
# 二次元配列が与えられるので、最大値を返す、maxValueという関数を作成してください。

# [[1,1,2,3,2], [5,5,1,5,2], [3,5,2,3,1], [1,2,3,6,3]] -> 6
# [[0,9,1,4,5], [1,3,3,4,7], [11,12,34,81,12], [12,24,63,76,13]] -> 81
# [[-2,39,94,12,49], [11,35,84,21,32], [157,243,121,23,33], [11,43,65,84,29]] -> 243

def maxValue(array2d):

    max_value = []
    # for valueList in array2d:
    #     for value in valueList:
    #         max_value.append(value)
    # return max(max_value)

    curr = array2d[0][0]
    for array1d in array2d:
        for ele in array1d:
            if curr <= ele:
                curr = ele
    return curr

# print(maxValue([[1,1,2,3,2], [5,5,1,5,2], [3,5,2,3,1], [1,2,3,6,3]]))
# print(maxValue([[0,9,1,4,5], [1,3,3,4,7], [11,12,34,81,12], [12,24,63,76,13]]))
# print(maxValue([[-2,39,94,12,49], [11,35,84,21,32], [157,243,121,23,33], [11,43,65,84,29]]))

"""
ランダムな数字を含むバッグと、整数を受け取り、それぞれのバッグから
順番に数字を整数個分だけ取り出す処理を2次元配列を使って考えてみましょう
"""

import random

"""
鞄の中から選ぶには、ラウンドロビンというやり方を使いましょう。ラウンドロビンとは、
1つずつ周回して、終わったら最初からやり直すという意味です。
4つのバッグがある場合、bag1 -> bag2 -> bag3 -> bag4 -> bag1 -> bag2 ....のような処理が行われます。
"""
def chooseNFromBags2d(n, listOfBags):

    totalBags = len(listOfBags)
    chosenNumbers = []
    counter = 0
    while counter < n:
        # counter % numberOfBags によって、ラウンドロビンができます。バッグの中を循環します。
        currentBag = listOfBags[counter % totalBags]
        # 選択された数値を追加します。currentBagからランダムな値が選択されます。
        chosenNumbers.append(currentBag[random.randint(0, len(currentBag)-1)])
        # counterを1つずつ増加します。
        counter += 1
    return chosenNumbers

# bagOfNumbersはm x nの2次元配列です。m個のバッグ(totalBags)があり、それぞれのバッグがn個の
# 要素(numbersPerBag)を持っています。
def chooseNFromBags1d(n, bagOfNumbers, totalBags, numbersPerBag):
    chosenNumbers = []
    counter = 0
    while counter < n:
        # 現在のバッグの範囲を取得します。
        currentBagStart = (counter % totalBags) * numbersPerBag
        currentBagEnd = currentBagStart + numbersPerBag
        chosenNumbers.append(bagOfNumbers[random.randint(currentBagStart, currentBagEnd-1)])
        counter += 1
    return chosenNumbers

# それぞれのバッグは4つの数字を含んでいます。

# 2次元配列
luckyArrayOfBags = [[21, 5, 12, 25],[100, 88, 354, 643],[122, 145, 825, 4],[228, 674, 777, 77]]

# 1次元配列
unluckyBagOfNumbers = [292,39,78,978,668,6,66,666,662,876,276,782,879,869,478,1968]

print(chooseNFromBags2d(10, luckyArrayOfBags))
print(chooseNFromBags1d(10, unluckyBagOfNumbers, 4, 4))

#
# print(0 % 4)
# print(1 % 4)
# print(2 % 4)
# print(3 % 4)
# print(4 % 4)
# print(5 % 4)
# print(6 % 4)
# print(7 % 4)
# print(8 % 4)
# print(9 % 4)
# print(10 % 4)
# print(11 % 4)








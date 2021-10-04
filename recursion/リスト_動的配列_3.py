# import math
#
# def printArray(intArr):
#     outputString = "["
#     for currentInt in intArr:
#         outputString += str(currentInt) + " "
#     print(outputString + "]")
#
# # 初期配列を2つの項目に設定します。
# dArr = [2,3]
#
# print("Insert/Delete at the begining O(n)")
#
# printArray(dArr)
#
# # 配列の先頭に要素を追加します。O(n)
# # insert（値）メソッドを使います。
# dArr.insert(0,3)
# # スライス割り当てで特定のインデックスに追加することもできます。
# # dArr[start:end]の部分を右の配列と書き換えます。
# dArr[0:0] = [34]
# printArray(dArr)
#
# dArr[0:0] = [3, 43, 5243]
# printArray(dArr)
#
# # 最初の要素を削除します。
# # pop(インデックス）メソッドを使います。
# dArr.pop(0)
# printArray(dArr)
#
# # インデックス2の位置にある要素を削除します。
# dArr.pop(2)
# printArray(dArr)
#
# dArr[0:0] = [343, 343, 232, 12, 23, -23, 10]
# printArray(dArr)
#
# # 配列の途中要素を追加します。
# print("Insert / Delete at the middle O(n)")
# dArr.insert(math.floor(len(dArr) / 2), 4)
# printArray(dArr)
#
# # 配列の途中から、５つ先まで削除します。
# dArr[math.floor(len(dArr) / 2):math.floor(len(dArr) / 2) + 5] = []
# print(dArr)
#
# print("Insert / Delete at the middle O(1)")
#
# # 配列の最後に要素を追加します。
# # 1つの要素をプッシュします。
# dArr.append(4)
# dArr.append(50)
# printArray(dArr)
#
# # 配列の最後に複数要素を追加します。
# dArr.extend([6,3,4,54])
# printArray(dArr)
#
# # 配列の最後を削除します。
# # 1つの要素を削除します。
# dArr.pop()
# printArray(dArr)
#
# print("Pop 5 from end")
#
# # 後ろから5つの要素を削除します。
# for i in range(0, 5):
#     dArr.pop()
# printArray(dArr)


"""
問題1
2 つの整数を受け取って、その間にある整数の 3 乗を返します。
"""

# def cubeRange(a, b):
#     cubeList = []
#     for i in range(a, b + 1):
#         cubeList.append(i ** 3)
#     return cubeList
#
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i])
#
# print(cubeRange(1, 6))
# printList(cubeRange(3, 10))


"""
# 例題1
# a,bが与えられるので、aからbまでの中で2の倍数を空の動的配列に追加する関数、
evenRangeという関数を作成し、printListによって出力してください。
"""

# def evenRange(a, b):
#     evenList = []
#     for i in range(a, b+1):
#         if i % 2 == 0:
#             evenList.append(i)
#     return evenList
#
#
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i])
#
# printList(evenRange(1, 20))

"""
問題2

ある整数を受け取り、その数値まで文字列として表示します。
ただし、3 の倍数では fizz、5 の倍数では buzz、15 の倍数では 
fizzBuzz と表示します。
"""

def fizzBuzz(x):
    fizzBuzzList = []
    for i in range(1, x):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("fizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("buzz")
        else:
            fizzBuzzList.append("-" + str(i) + "-")
    return fizzBuzzList

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

# printList(fizzBuzz(45))

"""
# 例題
# 自然数nが与えられるので、1からnまでに含まれる素数を空の動的配列に追加する、
primeNumberを作成し、printListで出力してください。
"""

def primeNumber(x):
    primeNumberList = []
    for i in range(2, x):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primeNumberList.append(i)
    return primeNumberList


def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

# printList(primeNumber(100))


"""
問題3

郵便番号のリスト、郵便番号、範囲を受け取り、
リストの中から郵便番号の範囲内にあるものだけを返します。
"""

def zipcodeRange(listOfZipcodes, mainZip, zipRange):
    codesInRange = []
    for i in range(len(listOfZipcodes)):
        if abs(listOfZipcodes[i] - mainZip) <= zipRange:
            codesInRange.append(listOfZipcodes[i])
    return codesInRange

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

printList(zipcodeRange([50013, 94512, 90080, 90190, 90095, 54810, 85005], 90094, 200))












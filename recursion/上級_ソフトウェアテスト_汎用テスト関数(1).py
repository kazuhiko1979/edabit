"""
2 つのデータ値を受け取り、データをログに記録し、それらが等しいかどうかをアサーションする汎用のテスト関数を作成してみましょう。
データが等しくない場合はアサーションエラーが発生します。
"""

import decimal

# def equalAssertion(a, b):
#     equality = (a == b)
#     print(f"Comparing {str(a)} and {str(b)}..." + \
#           ("They are equal." if equality else "Error, they are NOT equal."))
#     # 等しくない場合はクラッシュします。
#     assert equality
#     return True
#
# def formatDecimal(num):
#     # 10進数モジュール四捨五入を可能にします。
#     result = decimal.Decimal(str(num)).quantize(decimal.Decimal('.01'),decimal.ROUND_HALF_UP) * 100
#     return result
#
#
# equalAssertion(formatDecimal(86.258), 8626)
# equalAssertion(formatDecimal(86.253), 8625)
# equalAssertion(formatDecimal(20.445), 2045)
# equalAssertion(formatDecimal(20.435), 2044)
# equalAssertion(formatDecimal(45.465), 4547)
# equalAssertion(formatDecimal(45.555), 4556)
# equalAssertion(formatDecimal(31.135), 3114)
# equalAssertion(formatDecimal(30.125), 3013)


"""
例として、2 つの配列を比較して、それらが等しいかどうかを判断してみましょう。
一方は要素の順序を考慮するラムダが含まれ、もう一方は順序は考慮しないラムダが含まれます。
"""

# def equalAssertion(a, b, callback = None):
#     equality = (a == b) if callback is None else callback(a, b)
#     print(f"Comparing {str(a)} and {str(b)}... " + ("They are equal." if equality else "Error, they are NOT equal."))
#     # 等しくない場合はクラッシュします。
#     assert equality
#     return True
#
# arr1 = [3,4,5,10,2,8,12]
# arr2 = [4,5,3,12,10,8,2]
# arr3 = [4,5,3,12,10,8,2]
#
# def orderedArrayEquality(a, b):
#     if len(a) != len(b):
#         return False
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             return False
#     return True
#
# def unorderedArrayEquality(a, b):
#     if len(a) != len(b):
#         return False
#     aHash = {}
#     bHash = {}
#
#     # カウントアルゴリズムを適用します。
#     for i in range(len(a)):
#         if a[i] in aHash:
#             aHash[a[i]] += 1
#         else:
#             aHash[a[i]] = 1
#
#         if b[i] in bHash:
#             bHash[b[i]] += 1
#         else:
#             bHash[b[i]] = 1
#
#     for key in aHash:
#         if key not in bHash:
#             return False
#         if aHash[key] != bHash[key]:
#             return False
#     return True
#
# # 順不同のチェック, pass
# equalAssertion(arr1, arr2, unorderedArrayEquality)
#
# # 順序を考慮したチェック, pass
# equalAssertion(arr2, arr3, orderedArrayEquality)
#
# # 順序を考慮したチェック, pass
# equalAssertion(arr1, arr2, orderedArrayEquality)

"""
文字列の配列を取り込んで、その配列を in-place で反転させる関数。

要素の順序は考慮してください。A[i] == B[i] を確認する反復ループで整合性を確認します。
ではどうやって、配列が in-place でソートされているかをチェックすればよいでしょうか？
"""

# import copy
# import math
#
# def equalAssertion(a, b, callback = None):
#
#     equality = (a == b) if callback is None else callback(a, b)
#
#     if equality:
#         print(f"Comparing {str(a)} and {str(b)}..." + "They are equal.")
#     else:
#         print(f"Comparing {str(a)} and {str(b)}..." + "Error, they are NOT equal.")
#     # 等しくなければクラッシュします。
#     assert equality
#     return True
#
# # 配列をin-placeで反転させる関数
# def reverseArr(arr):
#     middle = math.floor(len(arr) / 2)
#     for i in range(middle):
#         [arr[i], arr[len(arr)-1-i]] = [arr[len(arr)-1-i], arr[i]]
#
# # 要素の順番を考慮して整合性を確認する関数
# def reversedArrayEquality(a, b):
#     if len(a) != len(b):
#         return False
#     for i in range(len(a)):
#         if a[i] != b[len(a)-1-i]:
#             return False
#     return True
#
#
# strArr = ["FIAT", "Mercedes-Benz","CITROËN","BLUEBIRD","Alfa Romeo"]
# copyArr = copy.deepcopy(strArr)
# reverseArr(strArr)
# equalAssertion(strArr, copyArr, reversedArrayEquality)


"""
メールリストが与えられるので、重複していないメールのみを全て返す関数。
順序は関係ないので、ハッシュマップを使ってそれらが等しいかどうかをチェックしたり、
あるいはディープコピーを作成し、両方をソートをして A[i] == B[i] を行うことができます。
"""

# import copy
# import math
#
# def equalAssertion(a, b, callback = None):
#
#     equality = (a == b) if callback is None else callback(a, b)
#
#     if equality:
#         print(f"Comparing {str(a)} and {str(b)}..." + "They are equal.")
#     else:
#         print(f"Comparing {str(a)} and {str(b)}..." + "Error, they are NOT equal.")
#
#     assert equality
#     return True
#
# # 重複していないメールのみ全て返す関数
# def createSetList(arr):
#     arrUnique = list(set(arr))
#     return arrUnique
#
# def unorderedArrayEquality(a, b):
#     aHash = {}
#     bHash = {}
#
#     for i in range(len(a)):
#         if a[i] in aHash:
#             aHash[a[i]] += 1
#         else:
#             aHash[a[i]] = 1
#
#     for i in range(len(b)):
#         if b[i] in bHash:
#             bHash[b[i]] += 1
#         else:
#             bHash[b[i]] = 1
#
#     for key in aHash:
#         if key not in bHash:
#             return False
#     return True
#
#
# emailArr = ["aaa@bbb.com", "bbb@ccc.com", "ccc@ddd.com", "aaa@bbb.com", "ccc@bbb.com"]
#
# copyArr = copy.deepcopy(emailArr)
# setArr = createSetList(emailArr)
# equalAssertion(copyArr, setArr, unorderedArrayEquality)

import datetime

class Donation:
    def __init__(self, name, price, donationNumber, day, month, year):
        self.name = name
        self.price = price
        self.donationNumber = donationNumber
        self.donationDay = datetime.date(year, month, day)

    def __str__(self):
        return f'name:{self.name}, price:{self.price}, donationNumber {self.donationNumber}, day {self.donationDay}'

donationList = [
    Donation("Steve Jobs", 50000, 1, 21, 3, 2021),
    Donation("Bill Gates", 40000, 2, 2, 9, 2021),
    Donation("Mark Elliont Zuckerberg", 40000, 3, 29, 4, 2021),
    Donation("Jeffrey Preston Bezos", 50000, 4, 1, 2, 2021),
    Donation("Steve Jobs", 10000, 5, 19, 5, 2021),
]

def equalAssertion(a, b, callback = None):
    equality = (a == b) if callback is None else callback(a, b)
    if equality:
        print(f"Comparing {str(a)} and {str(b)}... They are equal")
        else:
        print("Error, they are NOT equal.")

        assert equality

# 一番高い寄付金を決める関数
def highestDonation(arr):
    hightest = max(donationList, key=(lambda x: x.price))
    return hightest

# 寄付金が同じ額か調べる関数
def checkSameDonation(d1, d2):
    return d1.price == d2.price

# 寄付金の金額で昇順にソートしたリスト
sortedList = list(sorted(donationList, key = lambda x: x.price))

highest = highestDonation(donationList)
equalAssertion(sortedList[-1], highest, checkSameDonation)










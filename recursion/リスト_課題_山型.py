"""
山型
medium
Bond はクラスの文化祭で行う劇で背景を制作することになり、現在は山を作っています。
各地点での山の高さの一覧 height が与えられるので、
山型になっているかどうか判断する isMountain という関数を定義してください。
山型の条件は以下の通りです。

- 配列のサイズが 3 以上であること。　
- 高さは初めは上がり続け、一度下がったら下がり続けること。（例：1,2,3,4,5,3,2,1）


関数の入出力例

入力のデータ型： integer[] height

出力のデータ型： bool

isMountain([1,2,3,2]) --> true

isMountain([1,2]) --> false

isMountain([2,1]) --> false

isMountain([1,2,2,2,2]) --> false

isMountain([1,2,3]) --> false

isMountain([4,3,2,1]) --> false

isMountain([1,2,2,2,3,2]) --> false

isMountain([3,2,2,2,1,1]) --> false

isMountain([10,20,30,400,500,10]) --> true

isMountain([100,200,100,400,500,100]) --> false

isMountain([100,200,300,200,100,300]) --> false

isMountain([100,50,100,200,300,400]) --> false


while 文を使い、昇順（最大値が更新され続ける期間）と
降順（最小値が更新され続ける期間）が 1 つずつあるか確認しましょう。


確認することを順番に記すと下記のようになります。

0 番目の要素は 1 番目より小さいか
昇順が終わったときに、要素が最後のインデックスではないか
降順が終わったときに、要素が最後のインデックスになっているか
"""

def isMountain(height):

    l = len(height)
    if l <= 0 or height[0] > height[1]: return False

    # 最大値・最小値・インデックスの初期値
    maxVal = -float('inf')
    minVal = float('inf')
    i = 0

    # 昇順が終わるまで処理を繰り返します
    while i < l and height[i] > maxVal:
        maxVal = height[i]
        i += 1

    # 昇順のみの配列の場合、falseを返します
    if i == l: return False

    # 降順が終わるまで処理を繰り返します
    while i < l and height[i] < minVal:
        minVal = height[i]
        i += 1

    # 配列の末尾まで降順が続いていなかったらfalseを返します
    return i == l



    # index = 0
    #
    # if height[0] > height[1]:
    #     return False
    #
    # # 昇順が終わったときに、要素が最後のインデックスではないか
    # while index < len(height):
    #     try:
    #         if height[index] < height[index+1]:
    #             index += 1
    #         else:
    #             break
    #     except IndexError:
    #         break
    #
    # # 末尾のindexの場合、降順がないため、false
    # if height[index] == len(height):
    #     return False
    #
    # # 降順が終わったときに、要素が最後のインデックスになっているか
    # while index < len(height):
    #     try:
    #         if height[index] > height[index+1]:
    #             index += 1
    #         else:
    #             break
    #     except IndexError:
    #         break
    #
    # # 末尾のindexと同じ場合、降順が成立（山型）が成立しているか判断
    # return index == len(height) - 1


print(isMountain([1,2,3,2]))
print(isMountain([1,2]))
print(isMountain([2,1]))
print(isMountain([1,2,2,2,2]))
print(isMountain([1,2,3]))
print(isMountain([4,3,2,1]))
print(isMountain([1,2,2,2,3,2]))
print(isMountain([3,2,2,2,1,1]))
print(isMountain([10,20,30,400,500,10]))
print(isMountain([100,200,100,400,500,100]))
print(isMountain([100,200,300,200,100,300]))
print(isMountain([100,50,100,200,300,400]))




# Original

# if height[0] > height[1]:
#     print("false")
#
# index = 0
#
# while index < len(height):
#     try:
#         if height[index] < height[index+1]:
#             index += 1
#         else:
#             break
#     except:
#         break
#
# # 末尾のindexの場合、降順がないため、false
# print(index)
# print(height[index])
#
# if height[index] == len(height):
#     print("false")
# while index < len(height):
#     try:
#         if height[index] > height[index+1]:
#             index += 1
#         else:
#             break
#     except:
#         break
#
# print(index)
# print(len(height)-1)
#
# if index == len(height)-1:
#     print("True")
# else:
#     print("false")



"""
シャトルラン
easy
E 高校の野球部は定期的に 20 メートルシャトルランを行なっており、1 日に複数回記録を取っており、
1 回でも記録が減少した選手にペナルティを与える部則がありました。
シャトルランの記録 records が与えられるので、ペナルティが与えられるか判定する、
hasPenalty という関数を定義してください。]
シャトルランは本来は 247 までしか存在しませんが、今回はいかなる自然数も対象とします。

関数の入出力例

入力のデータ型： integer[] records

出力のデータ型： bool

hasPenalty([1,2,3,4]) --> false

hasPenalty([4,3,2,1]) --> true

hasPenalty([4,3,3,2,1]) --> true

hasPenalty([150,130,130,82,51]) --> true

hasPenalty([100,200,200,200,300,400]) --> false

hasPenalty([80,80,80,80]) --> false

hasPenalty([80,90,60,70,80]) --> true

hasPenalty([150,140,58,67,1100]) --> true

hasPenalty([1,28,48,85,3]) --> true
"""


def hasPenalty(records):

    # 前の要素より減少した要素が現れた瞬間、trueを返します。
    for i in range(1, len(records)):
        if records[i-1] > records[i]:
            return True
    return False

    # over = 0
    # start = 0
    # index = 1
    #
    # while index < len(records):
    #     if records[start] <= records[index]:
    #         index += 1
    #         over += 1
    #         start += 1
    #     elif records[start] > records[index]:
    #         return True
    # return False


# def isover(num):
#
#     if num:
#         return False


print(hasPenalty([1,2,3,4]))
print(hasPenalty([4,3,2,1]))
print(hasPenalty([4,3,3,2,1]))
print(hasPenalty([150,130,130,82,51]))
print(hasPenalty([100,200,200,200,300,400]))
print(hasPenalty([80,80,80,80]))
print(hasPenalty([80,90,60,70,80]))
print(hasPenalty([150,140,58,67,1100]))
print(hasPenalty([1,28,48,85,3]))
print(hasPenalty([19,246,813,624]))



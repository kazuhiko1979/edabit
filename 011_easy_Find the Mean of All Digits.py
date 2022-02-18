"""
すべての桁の平均（Mean)を返す関数を作成します。
すべての桁の平均は、桁の合計/桁数です
（たとえば、512の桁の平均は（5 + 1 + 2）/ 3（桁数）= 8/3 = 2です）。
平均は常に整数になります。

例：
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6

"""

def mean(num):

    return sum(map(int, str(num))) // len(str(num))


    # dgt_lst = [int(x) for x in str(num)]
    # return sum(dgt_lst) // len(dgt_lst)

    # count = 0
    # total = 0
    # num = str(num)
    #
    # for i in num:
    #     i = int(i)
    #     total += i
    #     count += 1
    #
    # return total // count

print(mean(42))
print(mean(12345))
print(mean(666))
























# def mean(num):
#
#     # return sum(map(int, str(num))) / len(str(num))
#
#
#     """
#     イテレータとは一言でいうと、「要素を1つずつ取り出せるオブジェクト」です。
#     イテレータはイテレータオブジェクトという一つの型です。for文にかけられた場合、
#     リストはイテレータオブジェクト(見た目は自分のコピー)を生成しますが、後はほとんど何もしません。
#     「次の要素は？」ときかれて要素を提示しているのはイテレータオブジェクトです。
#     """
#
#
#     # dgt_lst = [int(x) for x in str(num)]
#     # return sum(dgt_lst) / len(dgt_lst)
#
#     # count = 0
#     # total = 0
#     # num = str(num)
#     #
#     # for i in num:
#     #     i = int(i)
#     #     total += i
#     #     count += 1
#     # return total // count
#
#
# print(mean(42))
# print(mean(666))
# print(mean(12345))

























# """
# Create a function that returns the mean of all digits.
#
# Examples
# mean(42) ➞ 3
#
# mean(12345) ➞ 3
#
# mean(666) ➞ 6
# Notes
# The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
# The mean will always be an integer.
# """
#
# import statistics
#
# def mean(num):
#
#     num = [int(i) for i in str(num)]
#     return statistics.mean(num)
#     #
#     # num = [int(i) for i in str(num)]
#     # return sum(num) / len(num)
#
#
# print(mean(42))
# print(mean(12345))
# print(mean(666))



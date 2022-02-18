"""
クラスを使い、与えられた数に収まる数を計算します。
クラスに対する、変数（self.ones、self.threes、self.nines）を作成します。

例えば・・・
引数5に対して、

1はいくつ含まれているか？
答え：１は5つ含まれている

3はいくつ含まれているか？
答え：３は１つ含まれている

9はいくつ含まれているか？
答え：9は含まれていません（ゼロ）

n1 = ones_threes_nines(5)

n1.ones ➞ 5
n1.threes ➞ 1
n1.nines ➞ 0
"""

class ones_threes_ninces:

    def __init__(self, num):
        self.ones = num
        self.threes = num // 3
        self.nines = num // 9


n1 = ones_threes_ninces(5)

print(n1.ones)
print(n1.threes)
print(n1.nines)



























# """
# Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class.
# You will make variables (self.ones, self.threes, self.nines) to do this.
#
# Examples
# n1 = ones_threes_nines(5)
# n1.nines ➞ 0
#
# n1.ones ➞ 5
#
# n1.1threes ➞
# Notes
# Do not use the math module.
# See version #2 of this series.
# """
#
# class ones_thress_nines:
#
#     def __init__(self, num):
#         self.ones = num
#         self.threes = num // 3
#         self.nines = num // 9

    # def __init__(self, num):
    #
    #     self.num = num
    #
    # @property
    # def ones(self):
    #     return self.num
    #
    # @property
    # def threes(self):
    #     return self.num // 3
    #
    # @property
    # def nines(self):
    #     return self.num // 9

# n1 = ones_thress_nines(5)
#
# # print(n1)
# print(n1.ones)
# print(n1.threes) # 5 // 3 = 1
# print(n1.nines)  # 5 // 9 = 0














"""
今日の課題：

半径rと高さh（cm）が与えられた円柱の質量（体積）を計算します。

【条件】
①出力はkgで指定し、小数点以下第2位を四捨五入する必要があります。
②計算：

cm³（立法センチメートル）をdm³（立法デシメートル）に変換します。
1dm³（１立法デシメートル）= 1L、1Lは1Kgです。

備考：
モジュール【math】のインポートをお勧めします。
"""

"""
円柱の体積：円面積＊高さ
円の面積：半径＊半径＊円周率
円周率：3.14159　→ π
"""
from math import pi

def weight(r, h):

    volume = round(r**2 * pi * h / 1000, 2)
    return volume

print(weight(4, 10))
print(weight(30, 60))
print(weight(15, 10))

































"""
Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

How to solve:

Calculate the volume of the cylinder.
Convert cm³ into dm³.
1dm³ = 1L, 1L is 1Kg.
Examples
weight(4, 10) ➞ 0.5

weight(30, 60) ➞ 169.65

weight(15, 10) ➞ 7.07
Notes
I recommend importing math.
"""

# from math import pi
#
# def weight(r, h):
#
#     return round(pi * r**2 * h / 1000, 2)
#
#     # volume = 3.14 * (r * r) * h
#     # print(volume) # 立法センチメートル →　グラム
#     # return round(volume / 1000, 2)
#
# print(weight(4, 10))
# print(weight(30, 60))
# print(weight(15, 10))








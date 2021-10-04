"""
10進数から16進数への書き換え
medium
Zayn は 16 進数しか使えない世界は飛ばされてしまったため、自動で 10 進数を 16 進数へ変えるプログラムを作ることにしました。正の 10 進数 decNumber が与えられるので、16 進数に書き換える decimalToHexadecimal という関数を作成してください。

関数の入出力例

入力のデータ型： integer decNumber

出力のデータ型： string

decimalToHexadecimal(532454) --> 81FE6
decimalToHexadecimal(90304) --> 160C0
decimalToHexadecimal(28394) --> 6EEA
decimalToHexadecimal(15) --> F
decimalToHexadecimal(74) --> 4A
"""

# def decimalToHexadecimal(target):
#
#     amari = []
#
#     # 割り算の商が０になるまで
#     while target != 0:
#         amari.append(target % 16)
#         target = target // 16
#
#     # 余りに10~15をA～Fに置換
#     for i in range(len(amari)):
#         if amari[i] == 10:
#             amari[i] = 'A'
#         elif amari[i] == 11:
#             amari[i] = 'B'
#         elif amari[i] == 12:
#             amari[i] = 'C'
#         elif amari[i] == 13:
#             amari[i] = 'D'
#         elif amari[i] == 14:
#             amari[i] = 'E'
#         elif amari[i] == 15:
#             amari[i] = 'F'
#
#     amari.reverse()
#     txt = ''.join([str(i) for i in amari])
#     return txt

import math

def decimalToHexadecimal(decNumber):
    hexadecimal = "0123456789ABCDEF"
    ans = ''
    currentHex = 0

    while decNumber > 0:
        currentHex = decNumber % 16
        ans = hexadecimal[currentHex] + ans
        decNumber = math.floor(decNumber / 16)

    return ans



print(decimalToHexadecimal(532454))
print(decimalToHexadecimal(90304))
print(decimalToHexadecimal(28394))
print(decimalToHexadecimal(15))
print(decimalToHexadecimal(74))
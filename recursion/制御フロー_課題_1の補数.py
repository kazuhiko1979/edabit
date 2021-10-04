"""
1の補数
easy
Chan は宿題で、2 進数で 1 の補数を求めるプログラム作成を課されました。2 進数 bits が与えられるので 1 の補数を返す、oneComplement という関数を作成してください。

関数の入出力例

入力のデータ型： string bits

出力のデータ型： string

oneComplement("00011100") --> 11100011
oneComplement("10010") --> 01101
oneComplement("001001") --> 110110
oneComplement("0111010") --> 1000101
oneComplement("1") --> 0
"""

def oneComplement(bits):

    # return ''.join((["1" if i == "0" else "0" for i in bits]))

    output = ''
    for i in range(len(bits)):
        output += '1' if bits[i] == '0' else '0'
    return output


print(oneComplement("00011100"))
print(oneComplement("10010"))
print(oneComplement("001001"))
print(oneComplement("0111010"))
print(oneComplement("1"))
print(oneComplement("0"))
print(oneComplement("000"))




#



# print(format(~int(string) & 0b1111, '04b'))


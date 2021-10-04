"""
Chan は宿題で、2 進数で 2 の補数を求めるプログラム作成を課されました。
2 進数 bits が与えられるので 2 の補数を返す、twosComplement という関数を作成してください。


oneComplement("00011100") --> 11100011
oneComplement("10010") --> 01101
oneComplement("001001") --> 110110
oneComplement("0111010") --> 1000101
oneComplement("1") --> 0
"""
# def twoComplmentHelper(output):
#
#     count = 1
#
#     output = [int(s) for s in output]
#
#     # 末尾が0の場合
#     if output[-1] == 0:
#         output[-1] += 1
#         output = ''.join(list(map(str, output)))
#         return output
#
#     # 末尾が1で繰り上げの場合
#     else:
#
#         for i in reversed(output):
#             if i != 0:
#                 count += 1
#             if i == 0:
#                 zero = '0 ' * (count-1)
#                 zero = zero.split()
#                 zero = list(map(int, zero))
#
#                 output[-count + 1:] = zero
#                 output[-count] += 1
#
#                 break
#
#         output = ''.join(list(map(str, output)))
#
#         if output.count('1') == len(output):
#
#             init_len = len(output)
#
#             output = list(output)
#             output.append('1')
#             zero = '0 ' * init_len
#             zero = zero.split()
#             zero = list(map(str, zero))
#             output[-init_len:] = zero
#
#             return ''.join(output)
#
#         return output
#
#
# def twosComplement(bits):
#
#     output = ''
#     for i in range(len(bits)):
#         output += '1' if bits[i] == '0' else '0'
#
#     return twoComplmentHelper(output)

def twosComplement(bits):

    twosComplement = onesComplement(bits)
    carryOut = False

    for i in reversed(range(0, len(twosComplement))):
        if twosComplement[i] == '0':
            twosComplement = twosComplement[:i] + '0' + twosComplement[i + 1:]
            carryOut = False
            break

        elif twosComplement[i] == '1':
            twosComplement = twosComplement[:i] + '0' + twosComplement[i + 1:]
            carryOut = True

    return '1' + twosComplement if carryOut else twosComplement

def onesComplement(bits):

    onesComplement = ''

    for bit in bits:
        if bit == '1':
            onesComplement += '0'
        else:
            onesComplement += '1'
    return onesComplement


print(twosComplement("00011100")) # 11100011
print(twosComplement("10010")) # 01101
print(twosComplement("001001")) # 110110
print(twosComplement("0111010"))
print(twosComplement("1"))
print(twosComplement("0"))
print(twosComplement("000"))

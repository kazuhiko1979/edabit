"""
You will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.

Worked Example
n = 4
4 is 0100 in binary. We are working in 32 bits so:
00000000000000000000000000000100 = 4
11111111111111111111111111111011 = 4294967291
return 4294967291
Examples
flipping_bits(2147483647) ➞ 2147483648

flipping_bits(1) ➞ 4294967294

flipping_bits(4) ➞ 4294967291
"""

def flipping_bits(n):

    n = bin(n).split('b')[1].zfill(32)
    return int(''.join(['1' if i == '0' else '0' for i in n]), 2)

    # return n ^ 0xFFFFFFFF



print(flipping_bits(4))
print(flipping_bits(1))
print(flipping_bits(0))
print(flipping_bits(802743475))
print(flipping_bits(35601423))
print(flipping_bits(123456))
print(flipping_bits(4))
















"""
Create a function that will take a HEX number and returns the binary equivalent (as a string).

Examples
to_binary(0xFF) ➞ "11111111"

to_binary(0xAA) ➞ "10101010"

to_binary(0xFA) ➞ "11111010"
Notes
The number will be always an 8-bit number.
"""


def to_binary(num):

    res = "{0:08b}".format(num, 16)
    return str(res)

print(to_binary(0xFF))
print(to_binary(0xAA))

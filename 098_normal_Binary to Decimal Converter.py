"""
Binary to Decimal Converter
You are given one input: A list containing eight 1's and/or 0's. Write a function that takes an 8 bit binary number and convert it to decimal.

Examples
binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]) ➞ 255

binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0]) ➞ 0

binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0]) ➞ 188
Notes
"""

def binary_to_decimal(lst):



  # return int(''.join(map(str, lst)), 2)


  # binary = ''.join(str(i) for i in lst)
  #
  # decimal = 0
  #
  # for digit in binary:
  #   decimal = decimal * 2 + int(digit)
  #
  # return decimal

print(binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]))
print(binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0]))
print(binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0]))
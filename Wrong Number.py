"""
Mubashir needs your help to find out a wrong number in a 2D list.

Imagine a 2D list of numbers given below:

lst = [
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]
You can notice that:

The end number of each row is the sum of each row's previous numbers.
The end number of each column is the sum of each column's previous numbers.
See below examples for a better understanding:

lst1 = [
  [2, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]

# 2 is incorrect in first row and first column.
# Replace it with 1.

lst2 = [
  [1, 2, 3, 7 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]

# 7 is incorrect in first row and fourth column.
# Replace it with 6.

lst3 = [
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,46]
]

# 46 is incorrect in fourth row and fourth column.
# Replace it with 45.
Examples
wrong_number(arr1) ➞ 1

wrong_number(arr2) ➞ 6

wrong_number(arr3) ➞ 45
"""

import numpy as np


def wrong_number(lst):

    lst1_t = np.transpose(lst)

    total = [sum(i[:3]) for i in lst1_t]
    lst_tmp = [j[-1] for j in lst1_t]

    for t, l in zip(total, lst_tmp):
          if t != l:
              index_m = total.index(t)
              result = lst1_t[index_m]


    top_num = result[-1] - sum(result[1:3])
    bottom_num = sum(result[0:3])

    if result[0] > top_num:
        return top_num
    elif result[-1] > bottom_num:
        return bottom_num

print(wrong_number([
[2, 2, 3, 6 ],
[4, 5, 6, 15],
[7, 8, 9, 24],
[12,15,18,45]
]))


print(wrong_number([
[1, 2, 3, 7 ],
[4, 5, 6, 15],
[7, 8, 9, 24],
[12,15,18,45]
]))

print(wrong_number([
[1, 2, 3, 6 ],
[4, 5, 6, 15],
[7, 8, 9, 24],
[12,15,18,46]
]))


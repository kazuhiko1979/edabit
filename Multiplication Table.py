"""
Your task, is to create N x N multiplication table, of size n provided in parameter.

For example, when n is 5, the multiplication table is:

1, 2, 3, 4, 5
2, 4, 6, 8, 10
3, 6, 9, 12, 15
4, 8, 12, 16, 20
5, 10, 15, 20, 25
This example will result in:

[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
Examples
multiplication_table(1) ➞ [[1]]

multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
"""
import numpy as np

def multiplication_table(n):

    res = [j*k for j in range(1, n + 1) for k in range(1, n + 1)]
    return np.array(res).reshape(-1, n).tolist()

print(multiplication_table(1))
print(multiplication_table(3))
print(multiplication_table(5))

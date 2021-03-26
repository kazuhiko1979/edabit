"""
A tetrahedron is a pyramid with a triangular base and three sides. A tetrahedral number is a number of items within a tetrahedron.

Create a function that takes an integer n and returns the nth tetrahedral number.

Alternative Text

Examples
tetra(2) ➞ 4
tetra(5) ➞ 35
tetra(6) ➞ 56

Formula for nth tetrahedral number:
Tn = (n * (n + 1) * (n + 2)) / 6
"""

def tetra(n):

    return int((n * (n + 1) * (n + 2)) / 6)

print(tetra(2))
print(tetra(5))
print(tetra(6))

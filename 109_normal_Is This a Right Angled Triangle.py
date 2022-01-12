"""
Is This a Right Angled Triangle?
Given three numbers, x, y and z, determine whether they are the edges of a right angled triangle.

Examples
right_triangle(3, 4, 5) ➞ True
# This is the classic example of a "nice" right angled triangle.

right_triangle(145, 105, 100) ➞ True
# This is a less famous example.

right_triangle(70, 130, 110) ➞ False
# This isn't a right angled triangle.
Notes
Notice the largest side of the triangle might not be the last one passed to the function.
All numbers will be integers (whole numbers).
"""

def right_triangle(x, y, z):

    

    # lst = [x, y, z]
    # lst = sorted(lst)
    #
    # for i in lst:
    #     if i <= 0:
    #         return False
    # return lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2



print(right_triangle(3, 4, 5))
print(right_triangle(145, 105, 100))
print(right_triangle(70, 130, 110))

print(right_triangle(0, 4, 4))
print(right_triangle(-3, 4, 5))


"""
Rectangle in Circle
Create a function that takes three numbers — the width and height of a rectangle, and the radius of a circle and returns True if the rectangle can fit inside the circle, False if it can't.

Examples
rectangle_in_circle(8, 6, 5) ➞ True

rectangle_in_circle(5, 9, 5) ➞ False

rectangle_in_circle(4, 7, 4) ➞ False
"""
import math


def rectangle_in_circle(w, h, radius):

    return (w ** 2 + h ** 2) ** 0.5 <= 2 * radius


    # a**2 + b**2 = c**2 --> triangle theorem, solve for c
    # c_squared = math.sqrt(w**2 + h**2)
    #
    # # c_squared is the diameter, so need to compare it to radius * 2
    # if c_squared <= radius *2:
    #     return True
    # else:
    #     return False


print(rectangle_in_circle(8, 6, 5))
print(rectangle_in_circle(5, 9, 5))
print(rectangle_in_circle(4, 7, 4))

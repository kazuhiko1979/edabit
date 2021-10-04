import math


def sine(x, y):
    return round(x * math.sin(math.radians(y)), 2)


def cosine(x, y):
    return round(x * math.cos(math.radians(y)), 2)


def tangent(x, y):
    return round(x * math.tan(math.radians(y)), 2)


print(sine(8, 27))
print(cosine(10, 4))
print(tangent(4, 39))


# print(math.sin(x))
# print(math.sin(math.radians(x)))
# print(math.sin(y))
# print(round(x * math.sin(math.radians(y)), 2))
# print(round(x * math.cos(math.radians(y)), 2))
# print(round(x * math.tan(math.radians(y)), 2))






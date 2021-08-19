def g(i):
    return i


def multiplyOfc(a, b):
    if b <= 0:
        return 1

    return g(a) * multiplyOfc(a, b - 1)


print(multiplyOfc(2, 5))
# print(multiplyOfc(3, 5))
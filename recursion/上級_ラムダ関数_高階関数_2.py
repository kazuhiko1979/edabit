def summation(g, a, b):
    if b < a:
        return 0
    return g(b) + summation(g, a, b-1)

# 10までの総和
# 1 + 2 + 3 + 4 + .... 10 = 55
identify = lambda i: i
# print(summation(identify, 1, 10))

# 10 * 100 の計算
# print(summation((lambda i:10), 1, 100))

def pPi(g, a, b):
    if b < a:
        return 1
    return g(b) * pPi(g, a, b-1)

# 10の階乗(10!)
print(pPi(identify, 1, 10))

# 5^10の計算
print(pPi((lambda i:5), 1, 10))


def summation(g, a, b):
    if b < a:
        return 0
    return g(b) + summation(g, a, b-1)

# 1から25までの2乗の総和
identify = lambda i: i*i
print(summation(identify, 1, 25))

# 1から10までの3i*(i+3)の総和
identify2 = lambda i: 3 * i * (i + 3)
print(summation(identify2, 1, 10))

# 1からmまでの2j*(j-1)の総和 m=20
identify3 = lambda j: 2 * j * (j-1)
m = 20
print(summation(identify3, 1, m))

# 1から6まで7-kの階乗
identify4 = lambda k: 7 - k
print(pPi(identify4, 1, 6))

# 3から9までのi^2+3の階乗
identify5 = lambda i: i * i + 3
print(pPi(identify5, 3, 9))










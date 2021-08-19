"""
Modify the inefficient code in the Code tab so it can pass the tests.

Examples
mod(base, exp, k) ➞ (base**(2**exp)) % k

mod(10, 1, 99 ) ➞ 1

mod(3, 2, 15 ) ➞ 6

mod(123, 20, 1234 ) ➞ 391
Notes
Try using loops.
"""

import time


def mod(base, exp, k):

    tic = time.perf_counter()

    # print(base ** (2**exp) % k)
    # print('t = {:.9f} sec'.format(time.perf_counter() - tic))
    #
    # tic = time.perf_counter()

    # return pow(base, pow(2, exp)) % k

    """
    pow(base, exp[, mod])
    base の exp 乗を返します; mod があれば、base の exp 乗に対する mod の剰余を返します 
    (pow(base, exp) % mod より効率よく計算されます)。
    二引数の形式 pow(base, exp) は、冪乗演算子を使った base**exp と等価です。
    """
    print('t = {:.9f} sec'.format(time.perf_counter() - tic))
    return pow(base, pow(2, exp), k)

    # return pow(base, pow(2, exp), k)




print(mod(10, 1, 99))
print(mod(3, 2, 15))
print(mod(123, 20, 1234))
print(mod(3, 5, 15))
print(mod(10, 5, 99))
print(mod(11, 23, 23))
print(mod(11, 1000, 23))
print(mod(5432, 234625, 4321))
print(mod(146145432, 5423345, 542))

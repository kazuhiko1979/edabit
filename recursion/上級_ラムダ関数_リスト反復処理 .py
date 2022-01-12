"""
リスト反復処理
リストとラムダ式を使用して、リスト内の各要素に関数を適用することができます。
これは、リスト全体に対して反復処理を適用するのと似ています。それでは例を見てみましょう。
"""

def forEach(f, arr):
    for i in arr:
        f(i)

forEach((lambda num: print(num)), [2, 3, 4, 5])

# 通常のfor loop
def simpleLoop():
    l = [3, 4, 5, 6, 6, 10]
    counter = 0
    for i in l:
        counter += i * i
    return counter

print(simpleLoop())

def loopDifferent():
    l = [3, 4, 5, 6, 6, 10]

    counter = 0

    def forEach(f, arr):
        for ele in arr:
            f(ele)

    def counterFunc(x):
        nonlocal counter
        counter += x * x

    forEach(counterFunc, l)

    return counter

print(loopDifferent())

def loopDifferentLibrary():
    l = [3, 4, 5, 6, 6, 10]
    counter = 0

    def counterFunc(x):
        nonlocal counter
        counter += x * x

    [counterFunc(i) for i in l]
    return counter

print(loopDifferentLibrary())





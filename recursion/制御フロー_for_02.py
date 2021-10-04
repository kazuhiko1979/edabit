# 総和
def summationForLoopIteration(n):

    total = 0

    for i in range(n + 1):
        total += i

    return total

print(summationForLoopIteration(10))

# Pythonのfor文には通常含まれる3つ目の条件式がないため、今回while文を使用します。
# while文はこの後の項で学習します

def divideBy2CountIteration(n):

    counter = 0

    while n > 1:
        n = n / 2
        counter = counter + 1

    return counter

print(divideBy2CountIteration(64))


def divideByCountIteration(divisior, n):

    counter = 0

    while n > 1:
        n = n / divisior
        counter = counter + 1

    return counter

print(divideByCountIteration(2, 64))
print(divideByCountIteration(4, 64))

"フィボナッチ関数（計算量O(n))"
# 再帰
def fibonacciNumberTailHelper(fn1, fn2, n):

    if n < 1:
        return fn1
    return fibonacciNumberTailHelper(fn2, fn1+fn2, n-1)


def fibonacciNumberTail(n):
    # helper関数のおかげで、この関数は1つのパラメータしか受け取りません。
    # 0と1からスタートします
    return fibonacciNumberTailHelper(0, 1, n)


# 反復
def fibonacciNumberForLoopIteration(n):
    fn1 = 0
    fn2 = 1

    for i in range(n):
        prevFn1 = fn1
        fn1 = fn2
        fn2 = prevFn1 + fn2

    return fn1

print(fibonacciNumberForLoopIteration(20))
print(fibonacciNumberTail(20))





















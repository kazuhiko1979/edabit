"""
Jack は魔法使いからもらった豆を裏庭に植えて昼寝をしました。昼寝から目覚めて裏庭を確認するとその豆は巨木へと成長し、雲の上にある巨人の城にたどりつくまでの大きさになっていました。豆を観察すると、以下の条件で 1 秒ずつ成長することがわかりました。

f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2) (n ≥ 2)

整数 n が与えられるので、n 秒後の木の高さを求める、fibonacci という関数を作成してください。

関数の入出力例

入力のデータ型： integer n

出力のデータ型： integer

fibonacci(5) --> 5
fibonacci(9) --> 34
fibonacci(10) --> 55
fibonacci(19) --> 4181
"""
# def fibonacciHelper(a, b, n):
#
#     if n == 1:
#         return n
#     if n == 2:
#         return n
#
#     for _ in range(n - 1):
#         a, b = b, a + b
#     return b
#
#
# def fibonacci(n):
#
#     return fibonacciHelper(0, 1, n)

# Normal
def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# 再帰
def fibonacciTailHelper(a, b, n):

    if n == 0:
        return a
    return fibonacciTailHelper(b, a+b, n-1)


def fibonacciTail(n):

    return fibonacciTailHelper(0, 1, n)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(19))

print(fibonacciTail(1))
print(fibonacciTail(2))
print(fibonacciTail(3))
print(fibonacciTail(5))
print(fibonacciTail(9))
print(fibonacciTail(10))
print(fibonacciTail(19))

"""
def fib_fast(num):

    a = 0
    b = 1

    if num == 1:
        return a
    elif num == 2:
        return b
    else:
        for i in range(num - 1):
            a, b = b, a + b
    return b

print(fib_fast(10))

"""
# # 末尾再帰を使って、n番目のフィボナッチを返す関数を作成
def fibonacciNumberTailHelper(fn1, fn2, n):

    if n < 1:
        return fn1

    return fibonacciNumberTailHelper(fn2, fn1+fn2, n-1)


def fibonacciNumberTail(n):

    #　この関数が１つのパラメータを受け取れるように、ヘルパー関数を使います
    # そうすることによって、関数の再利用をより簡単に行うことができます。
    # 0と1からスタートします
    return fibonacciNumberTailHelper(0, 1, n)



print(fibonacciNumberTail(6))
print(fibonacciNumberTail(10))

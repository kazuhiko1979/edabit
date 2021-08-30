class a():
    x = 3
    y = 10

    def multiply(x):

        return x * y

    class b():
        x = 15

        def multiply(x):

            # yを検索します
            # yはローカルスコープで見つからず、
            # y = 10として親スコープで見つかりました。
            return x * a.y

def myFun():
    x = 33
    print(x)

    print(a.x)

    print(a.b.x)

    print(a.b.multiply(2))

myFun()









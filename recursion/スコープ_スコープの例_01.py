# グローバルスコープ

x = 34
y = 5 * 4

def myFun():
    # 関数のスコープ

    # yを出力します。まだローカルスコープではyは定義されていません。
    # yを検索します。
    # 最初に検索されるのはローカルスコープです。その次は親スコープに検索されます。
    # したがって20が出力されます

    print(y)

    # xを出力します。まだローカルスコープではxは定義されていません。
    # Pythonで同じ変数名がスコープの中に存在する場合、どちらかを判断する必要があります。
    # ローカスコープからグローバル変数にアクセスする際、globalキーワードを使います。
    global x
    print(x)

    # 現在のローカルスコープでxで宣言します
    x = 56

    # xを検索します
    # 最初に検索するのはローカルスコープです。
    # したがって56が出力されます。

    print(x)

myFun()


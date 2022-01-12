"""
非同期関数
先ほど説明したように、同期型コールバックとは、f によって呼び出され、f が結果を返す前に実行されるコールバックのことです。


一方、非同期型コールバックとは、f によって呼び出され、f が終了しデータを返した後でも、処理が終了していないコールバックのことです。
お分かりのように、これはコールバックが他のスレッド（thread）で実行されるように制御フローを分割します。
言語やライブラリによって、コードを他スレッドで実行するための関数が提供されています。
"""

from threading import Timer
# threading.Timerを使います。

def runAfterXMs(f, s):
    # PythonのTimer関数はコールバックを受け取り、xミリ秒後に実行します。
    # この関数は非同期関数です。この関数はコールバックをどこか
    # 別の場所に送り、残りの関数が実行を終了する間に実行します。
    print("running the function.....")
    Timer(s, f).start()

    return "This function has finished...."

x = 5

# 1秒後にコールバックを実行します。
# print(runAfterXMs(lambda : print("Hello World!!!"), 1))

# 関数が終わったことをどうやって把握すればよいでしょうか？
# データの流れを制御できなくなってしまったので、コールバックの戻り値を
# 取得することはできません。
print(runAfterXMs(lambda : x*40, 1))

# グローバルへアクセス
results = None

# コールバック関数の外でアクセスして状態を変更すると、
# 副作用が発生する可能性があります。
def accessGlobal():
    global results
    results = x*40
print(runAfterXMs(accessGlobal,1))

# Noneを出力します。
print(results)

# 少し待つと、結果を出力することができます。
Timer(4, lambda : print(results)).start()



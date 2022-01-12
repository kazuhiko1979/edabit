"""
高階関数(1)
ラムダ式で作成した呼び出し可能オブジェクトは、データとして利用することができます。また、先ほど見たように、関数としてその場で実行することができ、変数にも格納することができました。


また、呼び出し可能オブジェクトを入力として関数に渡すこともできます。これによって、関数内での他の処理に加えて、ラムダ関数を呼び出すことができるようになります。


一方、関数内でラムダ関数を作成して、出力として返すこともできます。これによって、保存可能かつ、プログラム実行時に動的に呼び出せるコードを生成することができます。


変数に格納され、入力として渡され、出力として返されるすべてのデータ型は第一級オブジェクト（first-class object）と呼ばれます。呼び出し可能オブジェクトは、定義上第一級オブジェクトであり、言語がそれをサポートしている場合は、第一級関数（first-class function）もサポートします。


このように、関数を入力として受け取り、関数を出力として返す関数は高階関数と呼ばれます。


では、いくつかの例を見てみましょう。呼び出し可能オブジェクトを作成すると、その参照が呼び出される関数の仮パラメータにコピーされるので、呼び出し可能オブジェクトにアクセスすることができます。
"""
# この関数は関数の参照を受け取り、ローカルスコープ内で呼び出します。
def functionInputTest(f):
    return f() + ".... called from another function!"

print(functionInputTest(lambda :"hello world"))

def fSquared(f, x):
    return f(x*x)

# f(a^2) = a^2 + 30
print(fSquared((lambda a: a + 30), 5))

# 呼び出し可能オブジェクトを変数内に格納します
callable1 = lambda p: "p is " + str(p)

print(fSquared(callable1, 10))
print(fSquared(callable1, 8))




















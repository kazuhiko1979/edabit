"""
無名関数
ラムダ関数とは、関数リテラル（function literal）としてその場で作成される関数のことです。
匿名関数（anonymous function）、無名関数としても知られています。

関数は通常、コードが実行される前、つまりコンパイル時に宣言され、定義されます。
関数は関数名にバインドされており、変数のように動作します。

この関数名の内部には、メモリ内のコードセグメント（またはテキストセグメント、テキストとも呼ばれる）上に存在する関数の最初の命令のメモリアドレスが格納されています。
関数のすべての命令は連続したメモリにブロックごとに隣り合う形で格納されており、コードセグメントと呼ばれる読み取り専用の特別なメモリの場所に存在します。
この関数名を使えば、命令を簡単に参照してコードのどこでも実行することができます。

関数を作成するもう一つの方法があります。ラムダ式（lambda expression）を使うと、リテラルとしてその場で関数を作成することができます。
ラムダ式とは、呼び出し可能関数オブジェクトの参照を返す式のことを指します。

プログラミング言語は実際に無名関数を使ってオブジェクトを生成し、ラムダ式の戻り値はこのオブジェクトの参照になります。
これらのオブジェクトは、関数と同じように呼び出すことができるので、呼び出し可能オブジェクト（callable object）としばしば呼ばれます。

では、ラムダ関数を作ってその場で呼び出してみましょう。
"""
# その場でリテラルデータ型を作成
print(4)
print(4+6)
print("Hello" + "World")

# では、ラムダ式を使ってその場で関数を作成してみましょう。呼び出し可能オブジェクトの参照が返されるので、データを返す呼び出しを行うことができます。
# 見ての通り、名前がないので匿名関数と呼ばれています
# lambda 入力: 式
print(lambda : "a new world")
print((lambda : "a new world")())

print(lambda : 4 + 5)
print((lambda : 4 + 5)())

# 匿名関数スコープ外の変数にアクセスします。
p = 40
print(lambda : p + 10)
print((lambda : p + 10)())
print((lambda: "P is " + str(p))() + " .....")

# 特定の入力を受け取る匿名関数を作成することができます。通常の関数と同じように、呼び出すときに入力を渡すことができます。
print("squaring..." + str((lambda x: x * x)(4)))

def multi(x):
    return "squaring..." + str(x * x)
print(multi(4))

# この匿名関数は、どこにも保存されておらず、渡されてもいないので、ガベージコレクタによって後に消去されます。メモリは命令を格納するために作成され、
# その後解放されます。
print((lambda x, y: x + y))
print((lambda x, y: x + y)(15, 35))

# 呼び出しが行われた後は、なくなってしまいます。もう一度、定義し直す必要があります。
# 今回は、変数に格納して呼び出してみましょう。呼び出し可能オブジェクトはオブジェクトなのですから。
myCallable = lambda x, y: x + y
print(myCallable(3, 5))
print(myCallable(10, 10))
print(myCallable(150, 5))
print(myCallable)





















"""
リスト反復処理 map/filter
関数とは、定義的には、2 つの集合、集合 x と集合 y の間の関係のことであり、
集合 x のそれぞれの要素は、集合 y の要素に 1 つずつ指定されています。
"""

# リストを取り、リストの各要素を 2 乗する関数にマッピングしてみましょう。

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

    # fでnonlocalが使用されて、親スコープ変数(counter)にアクセスすることができます。自由度はありますが、この方法でラムダを使うと副作用が出ることがあるので注意が必要です。
    # ここではfを毎度呼び出しています。fに変化があった場合、副作用が発生します。
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

    # また、リスト内包を使い、その中でラムダやローカル関数を実行することもできます。
    # ただし、通常はリスト内包を使用して他のリストを返したり作成したりすることに注意してください。リスト内包は、式で評価された値のリストを返します。[式 for *要素* in *リスト*] と 記述します。式の中では、リストの現在の要素を使用することができます。
    [counterFunc(i) for i in l]
    return counter

print(loopDifferentLibrary())


def myMap(f, arr):
    results = []
    for i in arr:
        results.append(f(i))
    return results

nums = [1, 2, 3, 4, 5, 6, 7]
print(nums)
print(myMap((lambda x: x * x),nums))

# mapで返すのはイテレータ
print(list(map(lambda x: x * x, nums)))

# 言語の中には、リスト内包（list comprehensions）と呼ばれる機能を提供しているものもあります。

print(range(0, 10))

# シンタックスは次のようになります。[計算ステートメント for value in リスト]
print([x * x for x in range(0, 10)])

# 値であるxは、if文によってさらに決定することができます。ifはステートメントを実行する前に実行され、
# 現在のリスト要素がこのifに渡されます。

# 偶数のみに実行します。
print([x * x for x in range(0, 10) if x % 2 == 0])

"""
filter 高階関数は、述語関数（boolean 値を返す関数）とリストを受け取り、それぞれのリスト項目に対して述語を実行して、どれを「フィルタリング」するか削除するかを決定します。
filter は、同じ順番で true を返した要素で構成される新しいリストを返します。
リストを取り込んで、偶数をすべてフィルタリングした例を見てみましょう。
この関数は、リストの奇数のみを返します。
"""

def myFilter(predicateF, arr):
    results = []
    for i in arr:
        if predicateF(i) == True:
            results.append(i)
    return results
#
list1 = [1,2,3,4,5,6,7,8,9,10]
print(myFilter((lambda x: x%2 != 0), list1))

# filterで返すのはイテレーター
print(list(filter(lambda x: x%2 != 0, list1)))




















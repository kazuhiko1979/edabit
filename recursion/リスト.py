# 文字列は文字のリストです。
str = "Hello World!"

# for i in range(0, len(str)):
#     print(str[i])


def printIntArray(intArr):
    # Pythonでは"for a in b"構文を使うことができます。
    # 配列bをループし、aが現在処理されている値になります。
    for value in intArr:
        print(value)

# Pythonでは、配列は単に"リスト"と呼ばれます。
# Pythonのリスト型は固定サイズではなく動的配列です。動的配列については次のセクションで学びます。

# 配列を初期化するには、単純に[]配列カッコを使います。配列内の各項目はカンマで区切られています。
# 初期化とか、配列の初期値を設定することを意味します。
arr1 = [40, 3, 22, -2, 4, 8]
# printIntArray(arr1)

# []演算子で配列のしての要素にアクセスすることができます。
# これによって、変数と同じように値を書き換えることが可能です。
arr1[3] = 34
arr1[1] = 40
# printIntArray(arr1)

def printArray(arr):
    for value in arr:
        # "end = " " を使用すると、改行せず、同じ行に出力することができます。
        print(value, end=" ")
    print()

doubleArr = [34.5, 34.4, 23, 54.3]
charArr = ['h', 'e', 'l', 'l', 'o']
stringArr = ["The race is starting.", "A dog just escaped", "The company ran out of business"]

printArray(doubleArr)
printArray(charArr)
printArray(stringArr)




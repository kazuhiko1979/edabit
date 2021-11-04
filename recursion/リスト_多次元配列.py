# 整数の3次元配列を作成します
array3d =  [[[3,4,3],[4,7,8]],
            [[1,3,5],[2,7,8]],
            [[1,2,3],[9,7,8]]]

# ランク３なので、データを取得するには、3つのインデックスが必要です。
print(array3d[2][1][0])

# 整数の4次元配列を作成します
array4d = [[[[3,3],[4,3],[9,3]],[[6,5],[8,3],[9,3]]],
           [[[3,3],[4,3],[9,3]],[[6,5],[8,3],[9,3]]],
           [[[3,3],[4,3],[9,3]],[[6,5],[8,3],[9,3]]]]

# ランク4なので。データを取得するには4つのインデックス演算子が必要です。
print(array4d[2][1][2][1])

# 出力
def print3dArray(rank3Array):
    for arr2d in rank3Array:
        print(end = "[")
        for arr in arr2d:
            print(end = "[-")
            for value in arr:
                print(value, end="-")
            print(end= "]")
        print(end="]")
    print(end="]")
print()

def print4dArray(rank4Array):
    for arr3d in rank4Array:
        print(end ="[")
        for arr2d in arr3d:
            print(end ="[")
            for arr in arr2d:
                print(end = "[-")
                for value in arr:
                    print(value, end ="-")
                print(end = "]")
            print(end="]")
        print(end="]")
    print()

# 3次元配列
array3d = [[[3,4,3],[4,7,8]],[[1,3,5],[2,7,8]],[[1,2,3],[9,7,8]]]
print("printing 3d array...")
print3dArray(array3d)

# 4次元配列
array4d = [[[[3,3],[4,3],[9,3]],[[6,5],[8,3],[9,3]]],[[[3,3],[4,3],[9,3]],[[6,5],[8,3],[9,3]]],[[[3,3],[4,3],[9,3]],[[6,5],[8,3],[9,3]]]]
print("printing 4d array...")
print4dArray(array4d)


# 図書館にある本棚の中の本から、お気に入りの名言のリストを探して表してみましょう。
# 4次元リストを返します。[[[[char, char, char, char]]]]
# 棚を含む配列、本の配列を含む棚、名言の配列を含む本、文字の配列を含む名言
def myLibraryQuotes():
    # 本棚1の本
    book1Quotes = [
        "Let all of life be an unfettered howl.",
        "Our lives were just beginning, our favorite moment was right now, our favorite songs were unwritten.",
        "You were born to stand out, stop trying to fit in.",
        "Do not wait for the last judgment. It comes every day.",
    ]
    book2Quotes = [
        "It is not a religion. It is a relationship.",
        "The choice is yours. Don't let your pronouncements destroy your destiny rather let them build your future up!",
        "Poetry is born; When the relationships begin to melt on the slow flame of the eyes.",
        "Fatherhood is sacred."
    ]

    book3Quotes = [
        "Marriage is a partnership; not a sole proprietorship.",
        "She was soft rock that suddenly turned hard.",
        "A human is the one, who would give up a thousand Cleopatras to be with the person he or she loves.",
        "You read between the wrong lines."
    ]

    bookshelf1 = [book1Quotes, book2Quotes, book3Quotes]

    # 本棚2の本
    book4Quotes = [
        "Everything you want in life is a relationship away.",
        "Life!Even though it's black and white, it's still fairly colorful.",
        "To question reason is to trust it.",
        "La prueba de ausencia no es prueba de ausencia",
        "Not how the world is, but that it is, is the mystery.",
    ]

    book5Quotes = [
        "Confuse them with your silence. Shock them with your results.",
        "All statistics have outliers.",
        "The moon fascinates us in her simplicity.",
        "Anything you're good at contributes to happiness."
    ]

    book6Quotes = [
        "Confuse them with your silence. Shock them with your results.",
        "All statistics have outliers.",
        "The moon fascinates us in her simplicity.",
        "Anything you're good at contributes to happiness."
    ]

    book7Quotes = [
        "Don't write to sell, write to tell.",
        "Slowly we became silent, and silence itself if an enemy to friendship.",
        "Without the sun I am cold.Without your smile I am lost.",
        "You are the softness of the morning dew!"
    ]

    bookshelf2 = [book4Quotes, book5Quotes, book6Quotes, book7Quotes]

    # 本棚3の本
    book8Quotes = [
        "The Heart wants what it wants - or else it does not care",
        "You have a beautiful laugh. Like the promise of tomorrow.",
        "You'll never be able to let him go. You'll always feel wrong about being with me."
    ]

    book9Quotes = [
        "The voice of Love seemed to call to me, but it was a wrong number.",
        "Do not allow me to forget you",
        "Education consists mainly of what we have unlearned."
    ]

    book10Quotes = [
        "LIFE - Death's Very Emissary",
        "To conquer fear, you must become fear.",
        "Meditation is the energy of the mind,"
    ]

    bookshelf3 = [book8Quotes, book9Quotes, book10Quotes]

    return [bookshelf1, bookshelf2, bookshelf3]

def libraryQuotePrinter(libraryArray):
    for shelf in libraryArray:
        for book in shelf:
            for quote in book:
                quoteParsed = '"'
                for character in quote:
                    quoteParsed += "-" + character
                quoteParsed += '"'
                print(quoteParsed)

library4dList = myLibraryQuotes()
libraryQuotePrinter(library4dList)


def fibonacciNumberStack(n, arrayOutput):
    outputStack = []
    # このローカルスコープ内のフィボナッチ関数、親のcallStackを更新します。
    if n == 0:
        outputStack.append(0)
        arrayOutput.append(outputStack)
        return 0
    elif n == 1:
        outputStack.append(1)
        arrayOutput.append(outputStack)
        return 1
    answer1 = fibonacciNumberStack(n-1, outputStack)
    answer2 = fibonacciNumberStack(n-2, outputStack)
    outputStack.append(answer1 + answer2)
    arrayOutput.append(outputStack)
    return answer1 + answer2

# 多次元配列を受け取り、フラット化された一次元配列を返します。
def flatten(multiarray):
    # 配列が1次元ならフラットされています。
    arr1d = []
    for value in multiarray:
        # 値がリストかどうかチェックします。
        if isinstance(value, list):
            arr1d += flatten(value)
        else:
            arr1d.append(value)
    return arr1d

# 配列は実際はPythonの動的配列（オブジェクト）です。
# ヒープ保存（任意のスコープからのアクセス）と値渡し（参照値）のルールが適用されます。
callStack = []
print(fibonacciNumberStack(5, callStack))
print(callStack)

# 多次元配列はフィボナッチのコールスタックを表します。
# n = 4 : [[[[[1], [0], 1], [1], 2], [[1], [0], 1], 3]]
# f4 = f3 + f2 = (f2 + f1) + (f1 + f0) = ((f1 + f0) + f1) + (f1 + f0) = 3

# 多次元配列を平坦化して1次元配列にします。
print(flatten(callStack))












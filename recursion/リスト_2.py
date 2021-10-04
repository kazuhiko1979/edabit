# 問題1
# 整数の配列を取り込んで、偶数が何個あるかを調べます。

def isEven(n):
    return n % 2 == 0

# 整数の配列を取り込んで、偶数が何個あるかを調べます。
def totalEven(listOfInts):
    count = 0
    for i in range(len(listOfInts)):
        count += 1 if isEven(listOfInts[i]) else 0

    return count

list1 = [3, 43, 5, 4, 2, 100, 6]

totalEvens = totalEven(list1)
# print(totalEvens)

# 例題1
# 整数によって構成される配列が与えられているので、配列内のすべての要素を足し合わせた数値を返す。
# sumArrayElementという関数を作成してください。
# [3,43,5,4,2,100,6] --> 163
# [1,2,3,4,5,6] --> 21
# [32,21,10,3,5,6] --> 77

def sumArrayElement(lst):

    return sum(lst)

    # sum = 0
    # for i in range(len(lst)):
    #     sum += lst[i]
    # return sum
#
# print(sumArrayElement([3,43,5,4,2,100,6]))
# print(sumArrayElement([1,2,3,4,5,6]))
# print(sumArrayElement([32,21,10,3,5,6]))

def maxValue(lst):

    maxVal = lst[0]
    for ele in lst:
        if maxVal <= ele:
            maxVal = ele
    return maxVal

    # max = lst[0]
    # index = 0
    #
    # for i in range(1, len(lst)):
    #     if lst[i] > max:
    #         max = lst[i]
    #         index = i
    # return lst[index]

# print(maxValue([3,43,5,4,2,100,6]))
# print(maxValue([1,2,3,4,5,6]))
# print(maxValue([32,21,10,3,5,6]))

# 問題2
# 文の配列と文字を受け取り、その文字を含む文が何個あるかを返します。アルファベットの大文字、小文字は区別しないとします。
# アルファベットの大文字、小文字は区別しないとする。

def totalFoundInSentence(sentence, c):

    # 反復処理を使います。
    count = 0
    # 配列の中にあるそれぞれの要素のそれぞれの文字について調べます。
    for i in range(len(sentence)):
        currentSentence = sentence[i]
        for j in range(len(currentSentence)):
            # lower関数で全て小文字にして、1文字ずつチェックします。
            if currentSentence[j].lower() == c:
                # カウンターを増加します。
                count += 1
                break
    return count

list2 = ["The wood", "Pecked peckers", "At the inn", "Tomorrowland"]
totalFound = totalFoundInSentence(list2, 'a')

# print(totalFound)

# 例題1
# 文字列によって構成される配列が与えられるので、配列内に存在する全ての文字数をカウントする、countCharという関数を作成してください。

# ["The wood", "Pecked peckers", "At the inn", "Tomorrowland"] -> 44
# ["He","fumbled","in","the,darkness","looking","for","the","light","switch"] -> 47
# ["I","am","never","at","home","on","Sundays"] -> 23

def countChar(lst):

    return len(''.join(lst))

# print(countChar(["The wood", "Pecked peckers", "At the inn", "Tomorrowland"]))
# print(countChar(["He","fumbled","in","the,darkness","looking","for","the","light","switch"]))
# print(countChar(["I","am","never","at","home","on","Sundays"]))


# 例題2
# 小文字によって構成される配列が与えられるので、n以降の文字（o,p,q,rなど）をカウントする、higherThanNという関数を作成してください。

# ["the wood", "pecked peckers", "at the inn", "tomorrowland"] -> 20
# ["he","fumbled","in","the","darkness","looking","for","the","light","switch"] -> 17
# ["he","is","never","at","home","on","weekends"] -> 11

def higherThanN(lst):

    count = 0
    for string in lst:
        for char in string:
            if ord(char) >= 110:
                count += 1
    return count

    # return len(''.join(sorted(''.join(lst))).split('m')[-1])


# print(higherThanN(["the wood", "pecked peckers", "at the inn", "tomorrowland"]))
# print(higherThanN(["he","fumbled","in","the","darkness","looking","for","the","light","switch"]))
# print(higherThanN(["he","is","never","at","home","on","weekends"]))

"""
配列はどんなデータ型でも基本的に格納できるので、オブジェクトも格納することもできます。
では、オブジェクトの配列を作ってみましょう。
車を表すデータ構造の配列を作っていきます。
Car クラスを作成し、Car オブジェクトを作成し、車を配列に格納します。
"""

class Car():
    # __init__はCarのコンストラクタです。
    # オブジェクト自体にアクセスします。
    # selfがヒープからオブジェクトを取得します。
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def printCarArray(carArray):
    # arrの長さまで反復処理を繰り返します。
    for i in range(0, len(carArray)):
        print(carArray[i].make + " - " + carArray[i].model + " - " + str(carArray[i].year))

# 反復処理のもう１つの書き方
def printCarArraySimple(carArray):
    # 反復処理を繰り返します。
    for car in carArray:
        print(car.make + " - " + car.model + " Year " + str(car.year))

cars = []
cars.append(Car("Toyota", "Camry", 2000))
cars.append(Car("BMW", "X1 Sports", 2019))
cars.append(Car("Nissan", "GT-R", 2020))

print("First model: " + cars[0].make + "-" + cars[0].model + "-" + str(cars[0].year))

# 関数を使ってすべての車を出力します。
printCarArray(cars)
print("Simple version...")
printCarArraySimple(cars)






























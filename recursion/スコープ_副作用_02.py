# グローバル変数として存在していないので、副作用はありません。

def changeGlobalCounter(x):
    # 今回はglobalCounterがローカルスコープ内にしか存在しません。
    globalCounter = x

# changeGlobalcounterは副作用がないため、squareにも副作用はありません
def square(x):
    changeGlobalCounter(-12)
    return x * x

# この関数のスコープないからどの変数にも影響を与えていないので、副作用はありません。
def incrementOne(x):
    return x + 1

# 副作用なしの関数
def counterProcess():
    counter = 0

    counter = incrementOne(counter)
    print(counter)

    counter = incrementOne(counter)
    print(counter)

    counter = incrementOne(counter)
    print(counter)

    square(10)

    counter = incrementOne(counter)
    print(counter)

    return counter


def myFun():

    finalCount = counterProcess()


myFun()








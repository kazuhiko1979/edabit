globalCounter = 0


# 副作用を持っています
# この関数はグローバル変数に影響を与えます。
def increamentGlobalCounter():
    global globalCounter
    globalCounter = globalCounter + 1


# 副作用を持っています。
# この関数はグローバル変数に影響を与えます。
def changeGlobalCounter(x):
    global globalCounter
    globalCounter = x


# 他の開発者がsquare関数を作成しました
# 副作用を持っています
# この関数はグローバル変数に影響を与えます

def square(x):
    changeGlobalCounter(-12)
    return x*x

def myFun():
    increamentGlobalCounter()
    print(globalCounter)

    increamentGlobalCounter()
    print(globalCounter)

    increamentGlobalCounter()
    print(globalCounter)

    # square関数によって、globalCounterの値が大きく変わります。
    square(10)

    increamentGlobalCounter()

    print(globalCounter)

myFun()
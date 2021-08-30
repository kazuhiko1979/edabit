def getPi():

    pi = 3.1415926535897932784626433
    # この関数がスタックからポップされると、変数piは存在しなくなります。
    return pi


def myFun():
    print(getPi())


myFun()


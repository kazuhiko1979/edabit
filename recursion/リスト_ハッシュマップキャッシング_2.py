"""
データのリストを検索する場合はどうなるでしょうか？
整数によって構成されるリスト L1、L2 を受け取って、
両方のリストの交点を返す関数を実装してみましょう。
交点とは両方のリストに含まれるすべての整数を指します。
1 つのやり方として、片方のリスト T のそれぞれの要素が、
もう片方の要素 S に存在していれば、それを result という配列に push するという方法があります。
"""
def linearSearhExist(haysStack, needles):
    for i in range(len(haysStack)):
        if haysStack[i] == needles:
            return True
    return False


def listIntersection(targetList, searchList):

    result = []

    for i in range(len(searchList)):
        if linearSearhExist(targetList, searchList[i]):
            result.append(searchList[i])
    return result

# print(listIntersection([1,2,3,4,5,6],[1,4,4,5,8,9,10,11]))

def listIntersection(targetList, searchList):
    hashMap = {}
    results = []

    for i in range(len(targetList)):
        hashMap[targetList[i]] = targetList[i]
    for j in range(len(searchList)):
        if searchList[j] in hashMap:
            results.append(searchList[j])
    return results





print(listIntersection([1,2,3,4,5,6],[1,4,4,5,8,9,10,11]))
print(listIntersection([3,4,5,10,2,20,4,5],[4,20,22,2,2,2,10,1,4]))
print(listIntersection([2,3,4,54,10,5,9,11],[3,10,23,10,0,5,9,2]))

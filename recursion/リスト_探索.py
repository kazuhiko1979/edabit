# 単語の配列の中から特定の単語を探索します。

def needleInHaystack(haystack, needle):
    # 針を見つけるために、個々の要素を見ていきます。
    # この検索は、O(n)の時間がかかります。
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return -1

def printAtIndex(index, words):
    if index >= 0 and index < len(words):
        print("Printing: ->" + words[index] + "<- at index: " + str(index))
    else:
        print("Index out of scope!")


# 文字列の配列を作成します。
words = ["Take", "Restaurant", "Family", "Running", "Tea", "Apples"]


printAtIndex(needleInHaystack(words, "Running"), words)
# "Apple"という文字列を配列の中から探します。
printAtIndex(needleInHaystack(words, "Apples"), words)
# "Train"という存在しない文字列を配列の中から探します。
printAtIndex(needleInHaystack(words, "Train"), words)


# 2つの配列のうちどちらが最も高い値を持つか判定します。
def maxInArray(arr):
    # 最初の要素に最大値を設定します。
    maxValue = arr[0]
    # arrの中で最大値を探索します。
    for value in arr[1:]:
        if value > maxValue:
            maxValue = value
    return maxValue

# arr1の最大値がarr2よりも大きいかどうかを返します。
def hasLargeMax(arrOp1, arrOp2):
    # arrOp1が空なら、Falseを返します。
    if not arrOp1:
        return False
    # arrOp2が空で、arrOp2が空でない場合はTrueを返します。
    if not arrOp2:
        return True

    # 最大値を取得します。
    arrOp1Max = maxInArray(arrOp1)
    arrOp2Max = maxInArray(arrOp2)
    return arrOp1Max > arrOp2Max

arr1 = [23,43,2432,5464,3425,656,232]
arr2 = [43,23,55,34]
arr3 = [23,6464,43,54,6988]

print(hasLargeMax(arr1, arr2))
print(hasLargeMax(arr1, arr3))

"""
配列内の要素を探索する時にかかる計算コストは、O(n) になります。
それはコンピュータが n 個の要素をチェックしなければいけないからです。
しかし、現実世界では、計算コストが O(1) になるケースが多くあります。配列内のデータのインデックスが最初からわかっていれば、ランダムアクセスのおかげで O(1) でデータを検索することができます。
例えば、あるクラスの学生を検索する場合、学生 ID がわかれば、すぐに特定のデータを検索することができます。
"""

class Student:
    def __init__(self, firstName, lastName, age, grade):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.grade = grade

# オブジェクトによる値渡しなので、実パラメータの状態が変化します。
# この場合、学生IDの状態が変更されます。
def setStudentIds(students):
    for i in range(len(students)):
        # メソッドチェーン
        # idをインデックス + 1に設定します。
        students[i].id = i + 1
        print("Student " + students[i].firstName + " has an id of " + str(students[i].id))

# idによってstudentを検索して、姓名を返します。
# この関数の計算量は0(1)です。
def searchForStudent(id, listOfStudents):
    # 現実世界では、idは0からではなく1からスタートするのでidから1引きます。
    correctId = id - 1
    # idがstudentの数より大きい時は、"Not Found!"を返します。
    if not (0 <= correctId and correctId <= len(listOfStudents) - 1):
        return "Not Found!"

    studentFound = listOfStudents[correctId]
    return studentFound.firstName + " " + studentFound.lastName

# idによってstudentを検索して、姓名を返します。
# この関数の計算量は0(n)です。
def searchForStudentLinear(id, listOfStudents):
    for i in range(len(listOfStudents)):
        if listOfStudents[i].id == id:
            studentFound = listOfStudents[i]
            return studentFound.firstName + " " + studentFound.lastName
    return "Not Found!"

# Studentオブジェクトの配列を生成します。
students = []

students.append(Student("Paula", "Cooper", 15, 10))
students.append(Student("Daniel", "Roger", 14, 10))
students.append(Student("Trevor", "Nishi", 14, 9))
students.append(Student("Kei", "Hideyoshi", 16, 11))

# idを設定します
setStudentIds(students)

# idが3の学生を探します。
print("Search for id of 3 constant time - " + searchForStudent(3, students))
print("Search for id of 3 constant time - " + searchForStudentLinear(3, students))

# idが10の学生を探します。
print("Search for id of 10 constant time - " + searchForStudent(10, students))
print("Search for id of 10 linear time - " + searchForStudentLinear(10, students))






























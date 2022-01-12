"""
ホワイトボックステスト
プログラムのテストには、ブラックボックステスト（外部）とホワイトボックステスト（内部）の 2 つの方法があります。

内部コンポーネントが完全に無視され、全体的な入力と出力にのみ焦点が当てられるテスト方法はブラックボックステストと呼ばれます。
ブラックボックステストはプログラム全体の目的に厳密に基づいてテスト基準を構築するため、内部要素は無視されます。
先ほどの chooseStudent 関数に対するテストは、まさにこれを行っていると言えるでしょう。
テストケースでは、最年少で最も背が高い学生が返されるかどうかのみに焦点が当てられていました。
"""

"""
ホワイトボックステストでは、
テスト基準はコードに関する知識に基づいて形成されます。

では先ほどの chooseStudent に関するコードを見てみましょう。
今回、オプションで最小ヒープアルゴリズムを使用し、リストをヒープ化して、最初の k 人の学生を選択するようにしました。
しかし、これは in-place アルゴリズムの入力の配列が変更され、副作用が発生します。
"""
#
# import random
#
# class Student:
#     def __init__(self, studentId, grade, name, age, height):
#         self.studentId = studentId
#         self.grade = grade
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def __str__(self):
#         return f"ID: {self.studentId}...{self.name}, grade:{self.grade}, age {self.age}, height {self.height}"
#
# studentList1 = [
#     Student(1000,9,"Matt Verdict", 14, 5.5),
#     Student(1001,9,"Amy Lam", 14, 5.5),
#     Student(1002,10,"Bryant Gonzales", 15, 5.9),
#     Student(1003,9,"Kimberly York", 15, 5.3),
#     Student(1004,11,"Christine Bryant", 15, 5.8),
#     Student(1005,10,"Mike Allen", 16, 6.2),
# ]
# # 最年少かつ最も高い生徒: [1000, 1001, 1002, 1004, 1003,1005]
#
# studentList2 = [
#     Student(1000,9,"Matt Verdict", 14, 5.5),
#     Student(1001,9,"Amy Lam", 13, 5.5),# 変更され、13歳
#     Student(1002,10,"Bryant Gonzales" 6.2),, 15, 5.9),
#     Student(1003,9,"Kimberly York", 15, 5.3),
#     Student(1004,11,"Christine Bryant", 15, 5.8),
#     Student(1005,10,"Mike Allen", 16,
# ]
# # 最年少かつ最も高い生徒: [1001, 1000, 1002, 1004, 1003,1005]
#
# def printStudents(students):
#     print("----Total students: "+str(len(students))+"----")
#     for student in students: print(student)
#     print("---END---")
#
# # 最年少かつ最も高い生徒をk人返します。kはオプションでデフォルトは1になります。
# def chooseStudent(studentList, k = 1):
#     # ラムダの比較
#     # s1がs2より若く、背が高いかどうかを返します。もし、同じならs1とs2のIDを比較します。
#     def studentCompare(s1, s2):
#         if s1.age == s2.age: return s1.studentId < s2.studentId if s1.height == s2.height else s1.height > s2.height
#         return s1.age < s2.age
#
#     # studentListをheapifyし、最初のk個の要素をpopします。
#     def heapify(l):
#         for index in reversed(range(0, len(l)//2)):
#             minHeap(l, index)
#
#     def swap(arr, i,j):
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp
#
#     def minHeap(l, index):
#         lengthL = len(l)
#         curr = index
#         flag = True
#         while flag:
#             left = curr * 2 + 1
#             right = curr * 2 + 2
#             smallest = curr
#
#             if lengthL > left and not studentCompare(l[smallest], l[left]): smallest = left
#             if lengthL > right and not studentCompare(l[smallest], l[right]): smallest = right
#
#             if smallest == curr: flag = False
#             else: swap(studentList, curr, smallest)
#
#             curr = smallest
#
#     # Heapify studentList
#     heapify(studentList)
#     results = []
#     for i in range(k):
#         # minを最後のノードとswapし、削除します。O(1)
#         swap(studentList, 0, len(studentList)-1)
#         results.append(studentList.pop())
#
#         if len(studentList) > 0: minHeap(studentList, 0)
#         else: break
#     return results
#
# printStudents(studentList1)
# print(chooseStudent(studentList1)[0].studentId == 1000)
# printStudents(studentList1) # 副作用。 一人が減って、idでソートされていた配列もheapifyされてバラバラになりました。
#
# printStudents(studentList2)
# print(chooseStudent(studentList2)[0].studentId == 1001)
# printStudents(studentList2) # 副作用。 一人が減って、idでソートされていた配列もheapifyされてバラバラになりました。
#
# studentList3 = [
#     Student(1000,9,"Matt Verdict", 11, 5.5),# 変更、11歳
#     Student(1001,9,"Amy Lam", 13, 5.5),
#     Student(1002,10,"Bryant Gonzales", 13, 5.5),# 変更、13歳
#     Student(1003,9,"Kimberly York", 15, 5.3),
#     Student(1004,11,"Christine Bryant", 15, 5.3), # 変更、5.3高さ
#     Student(1005,10,"Mike Allen", 16, 6.2),
# ]
# # 最年少かつ最も高い生徒: [1000, 1001, 1002, 1003, 1004, 1005]
#
# printStudents(studentList3)
# # リスト3から4人を出力します。
# printStudents(chooseStudent(studentList3,4))
# printStudents(studentList3) # 副作用。Christine BryantとMike Allenしか残っていません。


import random
import copy

class Student:
    def __init__(self, studentId, grade, name, age, height):
        self.studentId = studentId
        self.grade = grade
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "ID: {} grade: {} name: {} name: {} height: {}".format(self.studentId, self.grade, \
                                                                      self.name, self.age, self.height)
studentList1 = [
    Student(1000,9,"Matt Verdict", 14, 5.5),
    Student(1001,9,"Amy Lam", 14, 5.5),
    Student(1002,10,"Bryant Gonzales", 15, 5.9),
    Student(1003,9,"Kimberly York", 15, 5.3),
    Student(1004,11,"Christine Bryant", 15, 5.8),
    Student(1005,10,"Mike Allen", 16, 6.2),
]
# 最年少かつ最も高い生徒: [1000, 1001, 1002, 1004, 1003,1005]

studentList2 = [
    Student(1000,9,"Matt Verdict", 14, 5.5),
    Student(1001,9,"Amy Lam", 13, 5.5),# 変更され、13歳
    Student(1002,10,"Bryant Gonzales", 15, 5.9),
    Student(1003,9,"Kimberly York", 15, 5.3),
    Student(1004,11,"Christine Bryant", 15, 5.8),
    Student(1005,10,"Mike Allen", 16, 6.2),
]
# 最年少かつ最も高い生徒: [1001, 1000, 1002, 1004, 1003,1005]

def printStudents(students):
    print("---Total students: " + str(len(students)) + "---")
    for student in students:
        print(student)
    print("---END---")


# 2つの学生リストが等しいかどうかを返す述語関数
def areStudentListsEquals(studentList1, studentList2):
    if len(studentList1) != len(studentList2):
        return False
    for i in range(len(studentList1)):
        if studentList1[i].studentId != studentList2[i].studentId or \
            studentList1[i].grade != studentList2[i].grade or \
            studentList1[i].name != studentList2[i].name or \
            studentList1[i].age != studentList2[i].age or \
            studentList1[i].height != studentList2[i].height:
            return False
        return True

# 最年少かつ最も高い生徒をk人返します。kはオプションでデフォルトは1になります。
def chooseStudent(studentListMain, k = 1):
    # Deep copy
    studentList = copy.deepcopy(studentListMain)
    # ラムダの比較
    # s1がs2より若く、背が高いかどうかを返します。もし、同じならs1とs2のIDを比較します。
    def studentCompare(s1, s2):
        if s1.age == s2.age: return s1.studentId < s2.studentId if s1.height == s2.height else s1.height > s2.height
        return s1.age < s2.age

    # studentListをheapifyし、最初のk個の要素をpopします。
    def heapify(l):
        for index in reversed(range(0, len(l)//2)):
            minHeap(l, index)

    def swap(arr, i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def minHeap(l, index):
        lengthL = len(l)
        curr = index
        flag = True
        while flag:
            left = curr * 2 + 1
            right = curr * 2 + 2
            smallest = curr

            if lengthL > left and not studentCompare(l[smallest], l[left]): smallest = left
            if lengthL > right and not studentCompare(l[smallest], l[right]): smallest = right

            if smallest == curr: flag = False
            else: swap(studentList, curr, smallest)

            curr = smallest

    # Heapify studentList
    heapify(studentList)
    results = []
    for i in range(k):
        # minを最後のノードとswapし、削除します。O(1)
        swap(studentList, 0, len(studentList)-1)
        results.append(studentList.pop())

        if len(studentList) > 0: minHeap(studentList, 0)
        else: break
    return results


# studentListをコピーします。
copyStudentList1 = copy.deepcopy(studentList1)
print(chooseStudent(studentList1)[0].studentId == 1000)
print(areStudentListsEquals(studentList1, copyStudentList1))

copyStudentList2 = copy.deepcopy(studentList2)
print(chooseStudent(studentList2)[0].studentId == 1001)
print(areStudentListsEquals(studentList2, copyStudentList2))


studentList3 = [
    Student(1000,9,"Matt Verdict", 11, 5.5),# 変更、11歳
    Student(1001,9,"Amy Lam", 13, 5.5),
    Student(1002,10,"Bryant Gonzales", 13, 5.5),# 変更、13歳
    Student(1003,9,"Kimberly York", 15, 5.3),
    Student(1004,11,"Christine Bryant", 15, 5.3), # 変更、5.3高さ
    Student(1005,10,"Mike Allen", 16, 6.2),
]

printStudents(studentList3)

# リスト3から4人を出力します。
printStudents(chooseStudent(studentList3, 4))
printStudents(studentList3)


























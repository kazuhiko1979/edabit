"""
プログラムが全く実行されなかったり、出力値が正しくなかったり、断続的にしか正しい値を出力しないことはよく目にするでしょう。
特に最初の完成物から意図した結果を得られることはほとんどありません。

出力値の正誤以外に他の要件を満たす必要があるケースも存在します。
例えば、作成中のソフトウェアが 3D アニメーションのフレームを特定の時間内にレンダリングする必要があったり、
アジャイル環境でチーム開発を行う際には、各イテレーション（iteration）でプログラムが適切に動作するかどうかをチェックする必要があります。
"""

"""
テスト原則
条件を満たす特定の生徒を検索して、名前を出力するアルゴリズムを開発する例を考えてみましょう。
学年、名前、年齢、身長、ID 等を基準にして、生徒を検索することができますが、
要件（requirement）の内容にかかわらず、実際に最初にテストを構築することができます。

では仮に、年齢、身長、ID を検索基準と仮定し、最年少かつ最も背の高い学生を検索することにしてみましょう。
もし、同じ条件の学生が複数存在する場合は、若い ID を優先します。
テスト駆動開発（TDD）は、まず要件を見て、テストケースに変換し、
それに pass するためにコードを開発するという考え方に基づいています。要件とは、プログラムが持つべき機能と、
それがどのように動作するかを指し、今回の場合では、学生のリストをデータとして表現し、
最年少かつ最も背の高い学生の名前を取得することが要件となります。テストケースは、入出力関係のセットであり、
それらが一致した場合は真を返し、そうでない場合は偽を返します。

関数をコーディングする前に、TDD に従ってまずテストケースのセットを作成しましょう。
まずはリストからランダムな学生を返す関数でテストを行ってみます。
"""

import random

class Student:
    def __init__(self, studentId, grade, name, age, height):
        self.studentId = studentId
        self.grade = grade
        self.name = name
        self.age = age
        self.height = height

studentList1 = [
    Student(1000, 9, "Matt Verdict", 14, 5.5),
    Student(1001, 0, "Amy Lam", 14, 5.5),
    Student(1002, 10, "Bryant Gonzales", 15, 5.9),
    Student(1003, 9, "Kimbery York", 15, 5.3),
    Student(1004, 11, "Christine Bryant", 15, 5.8),
    Student(1005, 10, "Mike Allen", 16, 6.2),
]

studentList2 = [
    Student(1000, 9, "Matt Verdict", 14, 5.5),
    Student(1001, 0, "Amy Lam", 14, 5.5),
    Student(1002, 10, "Bryant Gonzales", 15, 5.9),
    Student(1003, 9, "Kimbery York", 15, 5.3),
    Student(1004, 11, "Christine Bryant", 15, 5.8),
    Student(1005, 10, "Mike Allen", 16, 6.2),
]

# ランダムな学生を返します。
def chooseStudent(studnetList):
    return studnetList[random.randint(0, len(studnetList) - 1)]

# テストケース。Falseが出力された時は間違った出力になります。
print(chooseStudent(studentList1).studentId == 1000)
print(chooseStudent(studentList2).studentId == 1001)


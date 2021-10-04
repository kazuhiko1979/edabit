# 2次元配列_3

"""
最後に、独自のデータ構造「Student」と「Classrooms」を使って、
2 次元配列を使って学校のシミュレーションをしてみましょう。
学校は教室の配列になります。それぞれの教室には、生徒の配列が状態の一部として含まれています。
"""

class Student:
    def __init__(self, studentId, firtstName, lastName, gradeLevel):
        self.studentId = studentId
        self.firstName = firtstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel

    def getFullName(self):
        return self.firstName + " " + self.lastName

class Classroom:
    def __init__(self, students, courseName, period, roomNumber, teacher):
        self.students = students
        self.courseName = courseName
        self.period = period
        self.roomNumber = roomNumber
        self.teacher = teacher

    def getClassIdentity(self):
        return self.courseName + " room " + str(self.roomNumber) + \
        " during period " + str(self.period) + " managed by " + self.teacher

    def getNumberOfStudents(self):
        return len(self.students)

def printSchoolSchedule(classrooms):
    for classroom in classrooms:
        print(classroom.getClassIdentity())
        studentString = ""
        for student in classroom.students[:classroom.getNumberOfStudents()-1]:
            studentString += student.getFullName() + ","
        studentString += classroom.students[classroom.getNumberOfStudents()-1].getFullName()
        print("Student list: " + studentString)


classroom1 = Classroom([Student("AC-343424","Vincent", "Lynch",10),
                        Student("AC-343434","Violet", "Marshall",10),
                        Student("AC-343428","Aubree", "Lambert",10),
                        Student("AC-343454","Danny", "Robertson",10)],
                       "Algebra II", 2, 23, "Emily Theodore")

classroom2 = Classroom([Student("AC-340014","Kent", "Carter",11),
                        Student("AC-340024","Isaiah", "Chambers",11),
                        Student("AC-340018","Leta", "Ferguson",11)],
                       "English", 5, 104, "Daniel Pherb")

classroom3 = Classroom([Student("AC-330010","Glenda", "Soto",12),
                        Student("AC-330035","Johnny", "Robertson",12),
                        Student("AC-330020","Ava", "Hansen",12),
                        Student("AC-340084","Nathaniel", "Romero",11)],
                       "Biology", 5, 36, "Maki Watanabe")


school = [classroom1, classroom2, classroom3]
printSchoolSchedule(school)
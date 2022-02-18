"""
学生番号と名前を保持する辞書データから名前を取得する関数を作成します。
アルファベット順で学生名リストを作成してください。

辞書型のkey, value, itemsに注目！

例：
print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))

# }) ➞ ["Becky", "John", "Steve"]
"""

def get_student_names(students):

    # names = []
    # for student in students.values():
    #     names.append(student)
    # return sorted(names)

    # names = []
    # for student in students:
    #     names.append(students[student])
    # return sorted(names)

    return sorted([student for key, student in students.items()])


print(get_student_names({
    "Student 1": "Steve",
    "Student 2": "Becky",
    "Student 3": "John"
}))































# """
# Create a function that takes a dictionary of student names and returns
# a list of student names in alphabetical order.
#
# Examples
# get_student_names({
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# }) ➞ ["Becky", "John", "Steve"]
#
# """
#
# def get_student_names(students):
# #
# #     pass
#
#
#     # dic / values
#     # names = []
#     # for student in students.values():
#     #     names.append(student)
#     # return sorted(names)
#
#
#
#     # dic / values
#     names = []
#
#     for student in students:
#         # print(student)
#         # names.append(students[student])
#     return sorted(names)
#
#
#     # return sorted([name for key, name in students.items()])
#
# #
# print(get_student_names({
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# }))
# #
# # print(get_student_names({
# # 	"Student 1":"Jacek",
# # 	"Student 2":"Ewa",
# # 	"Student 3":"Zygmunt",
# # 	"Student 4":"Tomek"
# # }))
#
#



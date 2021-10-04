"""
Create a function that takes a dictionary of student names and returns
a list of student names in alphabetical order.

Examples
get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}) ➞ ["Becky", "John", "Steve"]
Notes
Don't forget to return your result.
"""

def get_student_names(students):

    return sorted([value for key, value in students.items()])


print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))

print(get_student_names({
	"Student 1":"Jacek",
	"Student 2":"Ewa",
	"Student 3":"Zygmunt",
	"Student 4":"Tomek"
}))





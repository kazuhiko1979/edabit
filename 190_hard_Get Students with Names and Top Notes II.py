"""
Get Students with Names and Top Notes II
Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]}, { "name": "Mich", "notes": [1, 3, 5]}] and returns a list of dictionaries like [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}].

If a student has no notes (an empty list), return top_note: 0.

Examples
get_name_and_top_note([{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}])  ➞ [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}]

get_name_and_top_note([{ "name": "Paul", "notes": []}, {"name": "Victoria", "notes": [3, 4, 2, 1]}])  ➞ [{ "name": "Paul", "top_note": 0 }, {"name": "Victoria", "top_note": 4}]
"""
# get_name_and_top_note=lambda students:[{'name':student['name'],'top_note':max([0]+student.get('notes'))} for student in students]

# v3
def get_name_and_top_note(students):

	return [{'name': student['name'], 'top_note':max(student.get('notes') + [0])} for student in students]

# v2
# def get_name_and_top_note(students):
#
# 	for student in students:
# 		student["top_note"] = max(student["notes"] + [0])
# 		student.pop("notes")
# 	return students

# v1
# def get_name_and_top_note(students):
#
# 	for student in students:
# 		student["top_note"] = student.pop("notes")
# 		if student["top_note"]:
# 			if max(student["top_note"]):
# 				student["top_note"] = max(student["top_note"])
# 		else:
# 			student["top_note"] = 0
#
# 	return students

print(get_name_and_top_note([{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}]))
print(get_name_and_top_note([{ "name": "Paul", "notes": []}, {"name": "Victoria", "notes": [3, 4, 2, 1]}]))

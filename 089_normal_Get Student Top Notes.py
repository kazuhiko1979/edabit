"""
Get Student Top Notes
Create a function that takes a list of student dictionaries and returns a list of their top notes. If the student does not have notes then let's assume their top note is equal to 0.

Examples
get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]) ➞ [5, 5, 4]
"""

def get_student_top_notes(students):

    # return [max(i['notes'] + [0]) for i in students]

    return [max(d["notes"]) if d["notes"] else 0 for d in students]


    # res = []
    #
    # for i in students:
    #     if not i["notes"] == []:
    #         res.append(max(i["notes"]))
    #     else:
    #         res.append(0)
    # return res

# get_student_top_notes = lambda s:[max(x['notes'], default=0) for x in s]


print(get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]))


print(get_student_top_notes([{'id': 1, 'name': 'Rochelle', 'notes': [0, 0, 3, 3, 5]}, {'id': 2, 'name': 'Robert', 'notes': []}, {'id': 3, 'name': 'Hans', 'notes': [2, 4, 5]}, {'id': 4, 'name': 'Joel', 'notes': [2, 5]}, {'id': 5, 'name': 'Eric', 'notes': [3, 5]}, {'id': 6, 'name': 'Cary', 'notes': [1, 2, 0, 0]}, {'id': 7, 'name': 'Cary', 'notes': [3, 2, 1]}, {'id': 8, 'name': 'Dennis', 'notes': [0, 0, 4]}, {'id': 9, 'name': 'Lexi', 'notes': [0, 1, 2, 1, 5]}, {'id': 10, 'name': 'Alfie', 'notes': [0, 1, 3, 4, 3]}]))


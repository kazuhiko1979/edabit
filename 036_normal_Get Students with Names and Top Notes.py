"""
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
"""

def top_note(student):

    # return {"name": student["name"], "top_note": max(student["notes"])}

    student["top_note"] = max(student["notes"])
    student.pop("notes")
    return student


    # name_note = [x for x in student.values()][0]
    # max_notes = max([i for i in student.values()][1])
    #
    # key = ["name", "top_note"]
    # value = [name_note, max_notes]
    #
    # student = dict(zip(key, value))
    # return student


    # student.popitem()
    # student.update({"top_note":max_notes})
    # return student

print(top_note({"name": "Jacek", "notes":[5, 4, 3]}))
print(top_note({"name": "Ewa", "notes":[3,3,3]}))
print(top_note({"name": "Zygmund", "notes":[1,2,3]}))
print(top_note({"name": "Alex", "notes":[1,4,6]}))




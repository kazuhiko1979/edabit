"""
Hall Monitor 2
A floor plan is arranged as follows:

You may freely move between rooms 1 and 2.
You may freely move between rooms 3 and 4.
However, you can enter the hallway to move between rooms 2 and 4.
Floor Plan

Create a function that validates whether the route taken between rooms is possible. The hallway will be given as the letter "H".

Examples
possible_path([1, 2, "H", 4, 3]) ➞ True

possible_path(["H", 1, 2]) ➞ False

possible_path([4, 3, 4, "H", 4, "H"]) ➞ True
Notes
A route may begin or end in any room (including the hallway).
All inputs are either numbers 1-4 or the letter "H".
No rooms will repeat.
"""

rooms = (1, 2, "H", 4, 3)

def possible_path(lst):

	steps = dict(zip([i for i in range(len(lst))], lst))

	step =[rooms.index(value) for key, value in steps.items() if value in rooms]

	try:
		for i in range(0, len(step)):
			if step[i] - step[i+1] == 1 or step[i] - step[i+1] == -1:
				continue
			else:
				return False
	except:
		return True



print(possible_path(["H", 1, 2]))
print(possible_path([1, 2, "H", 4, 3]))
print(possible_path([4, 3, 4, "H", 4, "H"]))


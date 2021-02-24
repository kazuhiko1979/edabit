"""
A floor plan is arranged as follows:

Four rooms, which all lead into the hallway.
It's impossible to move between rooms without first going into the hallway.
Room

Create a function that validates whether the path between rooms is possible. The hallway will be given as the letter "H".

Examples
possible_path([1, "H", 2, "H", 3, "H", 4]) ➞ True

possible_path(["H", 3, "H"]) ➞ True

possible_path([1, 2, "H", 3]) ➞ False
Notes
A route may begin or end in a hallway.
All inputs are either numbers 1-4, or the letter "H".
No rooms will repeat.
"""


def possible_path(lst):

    # rooms = (1, 2, 3, 4)
    #
    # for i in range(1, len(lst)):
    #     if lst[i] in rooms and lst[i - 1] in rooms:
    #         return False
    # return True

    return all(type(a) != type(b) for a, b in zip(lst, lst[1:]))


print(possible_path([1, "H", 2, "H", 3, "H", 4]))
print(possible_path(["H", 3, "H"]))
print(possible_path([1, 2, "H", 3]))
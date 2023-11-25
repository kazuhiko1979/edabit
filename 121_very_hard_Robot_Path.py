"""
Robot Path 🤖
Mubashir created a simple robot that is navigated by a series of North, East, South, and West [n, e, s, w] commands. Each command moves the robot one step in the given direction. The robot is designed for only two destinations:

Destination No. 1: e, n, e, e, n
Destination No. 2: w, n, w, n, w, w, n
Create a function that takes a list of commands and returns True if the robot reaches any of the destinations, False otherwise.

Examples
robot_path(["s", "e", "e", "n", "n", "e", "n"]) ➞ True
# Robot will end up at destination no. 1

robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]) ➞ False
# Robot will be lost somewhere

robot_path(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"]) ➞ True
"""

def robot_path(commands):

    dest = [(3, 2), (-4, 3)]
    x = commands.count('e') - commands.count('w')
    y = commands.count('n') - commands.count('s')
    return (x, y) in dest

    # movements = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}
    # position = [0, 0]
    #
    # destinations = [
    #     [3, 2],
    #     [-4, 3]
    # ]
    #
    # for move in commands:
    #     x, y = movements[move]
    #     position[0] += x
    #     position[1] += y
    #
    # return any(position == dest for dest in destinations)

    # upAndDown = 0
    # leftRight = 0
    #
    # goal_1 = {"up": 2, "right": 3}
    # goal_2 = {"up": 3, "left": -4}
    #
    # for i in commands:
    #     if i == "n":
    #         upAndDown += 1
    #     if i == "s":
    #         upAndDown -= 1
    #     if i == "e":
    #         leftRight += 1
    #     if i == "w":
    #         leftRight -= 1
    #
    # if ((goal_1["up"] == upAndDown) & (goal_1["right"] == leftRight)) or \
    #     ((goal_2["up"] == upAndDown) & (goal_2["left"] == leftRight)):
    #     return True
    # else:
    #     return False

print(robot_path(["s", "e", "e", "n", "n", "e", "n"]))
print(robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]))
print(robot_path(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"]))










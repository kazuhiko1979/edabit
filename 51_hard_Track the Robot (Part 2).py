"""
Track the Robot (Part 2)
This robot roams around a 2D grid. It starts at (0, 0) facing North. After each time it moves, the robot rotates 90 degrees clockwise. Given the amount the robot has moved each time, you have to calculate the robot's final position.

To illustrate, if the robot is given the movements 20, 30, 10, 40 then it will move:

20 steps North, now at (0, 20)
30 steps East, now at (30, 20)
10 steps South. now at (30, 10)
40 steps West, now at (-10, 10)
...and will end up at coordinates (-10, 10).

Examples
track_robot(20, 30, 10, 40) ➞ [-10, 10]

track_robot() ➞ [0, 0]
# No movement means the robot stays at (0, 0).

track_robot(-10, 20, 10) ➞ [20, -20]
# The amount to move can be negative.
Notes
Each movement is an integer (whole number).
"""

def track_robot(*steps):

    # ver = sum(steps[::4]) - sum(steps[2::4])
    # hor = sum(steps[1::4]) - sum(steps[3::4])
    #
    # return [ver, hor]


    # N, E, S, W = sum(steps[::4]), sum(steps[1::4]), sum(steps[2::4]), sum(steps[3::4])
    # return [E - W, N - S]


    x = 0
    y = 0

    steps = list(steps)

    for i in range(0, len(steps)):
        if i % 4 == 0:
            y += steps[i]
        elif i % 4 == 1:
            x += steps[i]
        elif i % 4 == 2:
            y -= steps[i]
        else:
            x -= steps[i]
    return [x, y]



    # my answer

    # steps = list(steps)
    #
    # x = 0
    # y = 0
    # key = 1
    #
    # if not steps:
    #     return [0, 0]
    #
    # y += steps[0]
    #
    # try:
    #     for i in range(1, len(steps)+1):
    #         if i % 2 != 0:
    #             if key == 1:
    #                 x += steps[i]
    #                 key = 0
    #             elif key == 0:
    #                 x -= steps[i]
    #                 key = 1
    #         if i % 2 == 0:
    #             if key == 1:
    #                 y += steps[i]
    #                 key = 1
    #             elif key == 0:
    #                 y -= steps[i]
    #                 key = 0
    # except:
    #     return [x, y]

print(track_robot(20, 30, 10, 40))
print(track_robot(10, -10, -10, 10))
print(track_robot())
print(track_robot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(track_robot(1, 0, 2, 0, 3, 0, 4, 0, 5, 0))
print(track_robot(0, 1, 0, 2, 0, 3, 0, 4, 0, 5))
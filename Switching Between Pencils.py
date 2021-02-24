"""
When coloring a striped pattern, you may start by coloring each square sequentially, meaning you spend time needing to switch coloring pencils.

Create a function where given a list of colors cols, return how long it takes to color the whole pattern. Note the following times:

It takes 1 second to switch between pencils.
It takes 2 seconds to color a square.
See the example below for clarification.

color_pattern_times(["Red", "Blue", "Red", "Blue", "Red"]) ➞ 14

# There are 5 colors so it takes 2 seconds to color each one (2 x 5 = 10).
# You need to switch the pencils 4 times and it takes 1 second to switch (1 x 4 = 4).
# 10 + 4 = 14
Examples
color_pattern_times(["Blue"]) ➞ 2
color_pattern_times(["Red", "Yellow", "Green", "Blue"]) ➞ 11
color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]) ➞ 13
Notes
Only change coloring pencils if the next color is different to the color before it.
Return a number in seconds.
"""


def color_pattern_times(cols):

    time = 2
    current_item = 0
    next_item_num = 1

    if len(cols) == 1:
        return time
    if len(cols) == 0:
        return 0

    while next_item_num < len(cols):
        if cols[current_item] == cols[next_item_num]:
            time += 2
            current_item += 1
            next_item_num += 1
        else:
            time += 3
            current_item += 1
            next_item_num += 1

    return time


print(color_pattern_times(["Blue"]))
print(color_pattern_times(["Red", "Yellow", "Green", "Blue"]))
print(color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))
print(color_pattern_times([]))

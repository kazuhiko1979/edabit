"""
Write a function that returns the dice with the correct amount of eyes in a single string.

6 can be written as:

O-O
O-O
O-O
Or:

O-O/O-O/O-O  // with slashes and dashes
And 1:

---/-O-/---
Your function will have to return the dice as shown in the image. Look at the examples and the Tests tab what is asked. Multiple dice are separated by a comma and space.

Examples
dice(3) ➞ "O--/-O-/--O"

dice(8) ➞ "O-O/O-O/O-O, O--/---/--O"

dice(6) ➞ "O-O/O-O/O-O"
Notes
The input is always a positive number, return an empty string when 0 is given.
"""


def dice(num):

    dice = {
        1: ["---/-O-/---"],
        2: ["O--/---/--O"],
        3: ["O--/-O-/--O"],
        4: ["O-O/---/O-O"],
        5: ["O-O/-O-/O-O"],
        6: ["O-O/O-O/O-O"]
    }

    q, mod = divmod(num, 6)

    tmp_res = [str(i) for i in str(q)]
    res = [int("".join(tmp_res))]

    if mod == 0:
        c = sum([[s] * n for s, n in zip(dice[6], res)], [])
        str_c = ", ".join(c)
        return str_c
    else:
        c = sum([[s] * n for s, n in zip(dice[6], res)], [])
        str_c = ", ".join(c + dice[mod])
        return str_c


print(dice(3))
print(dice(11))
print(dice(8))
print(dice(1))
print(dice(20))
print(dice(63))
print(dice(6))
print(dice(9))
print(dice(18))











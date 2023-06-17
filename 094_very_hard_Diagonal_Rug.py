"""
Diagonal Rug
Create a function that takes in size and direction and generates a diagonal rug.

The size is the n parameter, and all rugs are square n x n. The direction is whether the diagonal part begins on the left or the right side.

Examples
generate_rug(4, "left") ➞ [
  [0, 1, 2, 3],
  [1, 0, 1, 2],
  [2, 1, 0, 1],
  [3, 2, 1, 0]
]

generate_rug(5, "right") ➞ [
  [4, 3, 2, 1, 0],
  [3, 2, 1, 0, 1],
  [2, 1, 0, 1, 2],
  [1, 0, 1, 2, 3],
  [0, 1, 2, 3, 4]
]

generate_rug(1, "left") ➞ [
  [0]
]

generate_rug(2, "right") ➞ [
  [1, 0],
  [0, 1]
]
Notes
n > 0
A 1 x 1 rug is trivially [[0]] (same for left and right).
"""

def generate_rug(n, direction):
    rug = []
    for i in range(n):
        row = []
        for j in range(n):
            if direction == "left":
                value = abs(i - j)
            else:
                value = abs(n - i - j - 1)
            row.append(value)
        rug.append(row)
    return rug



    # rug = []
    # if direction == "left":
    #     for i in range(n):
    #         row = []
    #         for j in range(n):
    #             value = abs(i - j)
    #             row.append(value)
    #         rug.append(row)
    # else:
    #     for i in reversed(range(n)):
    #         row = []
    #         for j in range(n):
    #             value = abs(i - j)
    #             row.append(value)
    #         rug.append(row)
	#
    # return rug


print(generate_rug(4, "left"))
print(generate_rug(5, "right"))
print(generate_rug(6, "left"))
print(generate_rug(1, "left"))
print(generate_rug(2, "right"))


"""
Check Rubik's Cubes
Matt wants to make Rubik Cubes. These Rubiks should be in the shape of a full cube, and it shouldn't have any missing parts.

This is a full cube:

Full

This is not a full cube:

Full

And he asks his friend to draw some patterns. When his friend gives him these Rubik's Cube patterns, he realizes that some of them are wrong or missing. Help him identify them!

The small cubes that make up the Rubik's Cube will be denoted by "O".

Return "Full" if the Rubik Cube is full and no part is missing.
Return "Non-Full" if the Rubik Cube is non-full and no part is missing.
Return "Missing {number of missing parts}" if the Rubik Cube has missing parts.
Examples
identify(
  ["O", "O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Full"

# This is 3x3 full Rubik's Cube.
# So we should return "Full"
identify(
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Non-Full"

# This is a 2x3 Rubik's Cube.
# It's not full, so we should return "Non-Full".
identify(
  ["O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Missing 1"

# This is almost a 3x3 Rubik's Cube with one missing part.
# We should return "Missing 1".
Notes
Every cubic (small part of a Rubik's Cube) will be denoted by "O". There won't be any other type.
Don't forget to return by paying attention to capital letters.
"""
import numpy as np

def identify(*cube):

    # v3
    l = [len(x) for x in cube]
    return ('Non-Full', 'Full')[len(l) == l[0]] if len(set(l)) < 2 else "Missing {}".format(abs(len(l)**2 - sum(l)))

    # v2
    # m = len(cube)
    # n = max(len(row) for row in cube)
    # missing = sum(n-len(row) for row in cube)
    #
    # if missing:
    #     return "Missing" + str(missing)
    # return "Full" if m == n else "Non-Full"



    # v1
    # horizon = [len(x) for x in cube]
    # vertical = [len(y) for y in np.array(cube).T.tolist()]
    #
    # full = max(horizon) * len(horizon)
    # original_num = len([j for i in cube for j in i if j == "O"])
    #
    # if len(set(horizon)) and len(set(vertical)) == 1 and set(horizon) == set(vertical):
    #     return "Full"
    # elif full != original_num:
    #     return 'Missing {}'.format(full - original_num)
    # else:
    #     return 'Non-Full'

print(identify(
  ["O", "O"],
  ["O", "O"],
  ["O", "O", "O"]
))

print(identify(
	["O", "O"],
	["O", "O", "O"]
))

print(identify(
  ["O", "O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
))

print(identify(
	["O", "O", "O", "O"],
	["O", "O", "O", "O"],
	["O", "O", "O", "O"],
	["O", "O", "O", "O"]
))

print(identify(
	["O", "O", "O", "O"],
	["O", "O", "O", "O"],
	["O", "O", "O"],
	["O", "O", "O", "O"]
))

print(identify(
	["O", "O", "O", "O"],
	["O", "O", "O", "O"]
))

print(identify(
	["O", "O"],
	["O", "O"]
))

print(identify(
	["O", "O"],
	["O"]
))




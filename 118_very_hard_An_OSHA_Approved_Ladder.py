"""
An OSHA Approved Ladder?
Due to a huge scandal about the Laddersons Ladder Factory creating faulty ladders, the Occupational Safety and Health Administration require your help in determining whether a ladder is safe enough for use in the work place! It is vital that a ladder passes all criterea:

The ladder must be at least 5 characters wide.
The ladder mustn't have more than a 2 character gap between rungs.
Rungs must be evenly spaced apart.
Rungs should not be broken (i.e. no gaps).
Given a ladder (drawn as a list of strings) return True if it passes all of OSHA's criterea.

Examples
is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]) ➞ True
is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]) ➞ False

# Uneven spaces between rungs.
is_ladder_safe([
  "#  #",
  "####",
  "#  #",
  "#  #",
  "####",
  "#  #",
  "#  #",
  "####",
  "#  #"
]) ➞ False

# Ladder is too narrow, should be at least 5 characters wide.
is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]), ➞ False

# Gap between rungs is too wide, should be less than 3.
is_ladder_safe([
  "#   #",
  "#  ##",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]) ➞ False

# The top rung is broken.
Notes
There will be a one character space with no rung at the top and bottom of every ladder.
The height of the ladder is not needed for solving this problem.
"""
import re

def is_ladder_safe(ldr):

	ldr = ldr[1:-1]
	rung = [x for x in range(len(ldr)) if ldr[x] == len(ldr[0]) * '#']

	if not rung:
		return False

	diff = rung[1] - rung[0]
	return (all(y - x == diff for x, y in zip(rung, rung[1:])) and
			diff <= 3 and diff * len(rung) >= len(ldr) and len(ldr[0]) >= 5)

print(is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]))


print(is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]))


print(is_ladder_safe([
  "#   #",
  "#  ##",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]))



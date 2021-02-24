"""
Given a list of strings (depicting a skyline of several buildings), return in meters the height of the tallest building. Each line in the list represents 20m.

Examples
tallest_building_height([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "140m"

# Tallest building is 7 characters
# 7 x 20m = 140m

tallest_building_height([
  "               ",
  "               ",
  "               ",
  "       #    ###",
  "      # #   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "80m"

# Tallest building is 4 characters
# 4 x 20m = 80m

tallest_building_height([
  "                              ",
  "                         ###  ",
  "                         ###  ",
  "###                    #####  ",
  "###      #             #####  ",
  "###     ###            #####  ",
  "######  ###            #######",
  "######  ######  ###    #######",
  "###################    #######",
  "###############################",
  "###############################"
]) ➞ "200m"

# Tallest building is 10 characters
# 10 x 20m = 200m
Notes
There may be some open sky above buildings (can't just find the length of the list).
There may be multiple tallest buildings (see example #2).
"""
from typing import List


def tallest_building_height(lst):

    #
    # ht = 0
    # for line in lst:
    #     if "#" in line:
    #         ht += 1
    # return str(ht*20)+"m"

    return str(20*sum("#" in line for line in lst)) + 'm'


print(tallest_building_height(([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
])))

print(tallest_building_height([
  "               ",
  "               ",
  "               ",
  "       #    ###",
  "      # #   ###",
  "###   ###   ###",
  "###   ###   ###"
]))



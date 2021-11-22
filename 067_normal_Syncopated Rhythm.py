"""
Syncopation means an emphasis on a weak beat of a bar of music;
most commonly, beats 2 and 4 (and all other even-numbered beats if applicable).

You will be given a string representing beats, where hashtags # represent emphasized beats.
Create a function that returns if the line of music contains any syncopation, and False otherwise.

Examples
has_syncopation(".#.#.#.#") ➞ True
# There are Hash signs in the second, fourth, sixth and
# eighth positions of the string.

has_syncopation("#.#...#.") ➞ False
# There are no Hash signs in the second, fourth, sixth or
# eighth positions of the string.

has_syncopation("#.#.###.") ➞ True
# There are Hash signs in the sixth positions of the string.
Notes
All other unemphasized beats will be represented as a dot.
"""

def has_syncopation(s):

    return '#' in s[1::2]

    # return "#" in [s[i] for i in range(0, len(s)) if i % 2 != 0]



    # res = []
    # for i in range(0, len(s)):
    #     if i % 2 != 0:
    #        res.append(s[i])
    #
    # if "#" in res:
    #     return True
    # return False

print(has_syncopation(".#.#.#.#"))
print(has_syncopation("#.#...#."))
print(has_syncopation("#.#.###."))
print(has_syncopation(".."))
print(has_syncopation(""))
print(has_syncopation("##"))
print(has_syncopation("####...."))
print(has_syncopation("#"))
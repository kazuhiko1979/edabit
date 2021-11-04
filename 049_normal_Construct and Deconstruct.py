"""
Given a string, create a function that outputs a list, building and deconstructing the string letter by letter. See the examples below for some helpful guidance.

Examples
construct_deconstruct("Hello") ➞ [
  "H",
  "He",
  "Hel",
  "Hell",
  "Hello",
  "Hell",
  "Hel",
  "He",
  "H"
]

construct_deconstruct("edabit") ➞ [
  "e",
  "ed",
  "eda",
  "edab",
  "edabi",
  "edabit",
  "edabi",
  "edab",
  "eda",
  "ed",
  "e"
]

construct_deconstruct("the sun") ➞ [
  "t",
  "th",
  "the",
  "the ",
  "the s",
  "the su",
  "the sun",
  "the su",
  "the s",
  "the ",
  "the",
  "th",
  "t"
]
"""

def construct_deconstruct(s):

    half = [s[:i] for i in range(1, len(s)+1)]
    return half + half[:-1][::-1]

    # res = []
    #
    # for i in range(1, len(s)+1):
    #     res.append(s[0:i])
    #
    # for x in range(len(s)-1, 0, -1):
    #     res.append(s[0:x])
    # return res

print(construct_deconstruct("Hello"))



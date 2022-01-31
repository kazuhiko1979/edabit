"""
FSA: Individual Instructions
Create a function that, when given a list of individual finite-state automaton instructions, generates an FSA in the form described in this challenge. Each instruction will be a list of three elements: The first element will be the current state, the second element will be the input to which the instruction pertains, and the third element will be the new state.

For example, the instruction ["S0", 1, "S1"] indicates that, if the current state is "S0", upon receiving a 1 as input, the new state will be "S1". A deconstruction of the FSA from this challenge can be seen below:

Examples
divisible = [
  ["S0", 0, "S0"], ["S0", 1, "S1"],
  ["S1", 0, "S2"], ["S1", 1, "S0"],
  ["S2", 0, "S1"], ["S2", 1, "S2"]
]

combine(divisible) ➞ {
  "S0": ["S0", "S1"],
  "S1": ["S2", "S0"],
  "S2": ["S1", "S2"]
}
Notes
Every FSA will use a binary alphabet.
All states will be of the form Sn, where n is an integer, e.g. S2.
"""

def combine(lst):

    return {a[0]: [a[2], b[2]] for a, b in zip(lst[::2], lst[1::2])}



    # res = {}
    # for i in lst:
    #     if i[0] in res:
    #         res[i[0]].append(i[2])
    #     else:
    #         res[i[0]] = [i[2]]
    # return res

print(combine([
  ["S0", 0, "S0"], ["S0", 1, "S1"],
  ["S1", 0, "S2"], ["S1", 1, "S0"],
  ["S2", 0, "S1"], ["S2", 1, "S2"]
]))











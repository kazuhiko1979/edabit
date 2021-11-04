"""
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
Worked Example
neutralise("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
Examples
neutralise("--++--", "++--++") ➞ "000000"

neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"

neutralise("-++-", "-+-+") ➞ "-+00"
Notes
The two strings will be the same length.
"""

def neutralise(s1, s2):

    # return ''.join([a if a == b else '0' for a, b in zip(s1, s2)])

# neutralise = lambda s1,s2: "".join(["0",x][x==y] for x, y in zip(s1, s2))

    # res = ""
    #
    # for i, x in zip(s1, s2):
    #     if i == "+" and x == "+":
    #         res += "+"
    #     elif i == "-" and x == "-":
    #         res += "-"
    #     elif i != x:
    #         res += "0"
    # return res

print(neutralise("--++--", "++--++"))
print(neutralise("-+-+-+", "-+-+-+"))


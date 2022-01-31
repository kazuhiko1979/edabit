"""
銃の打ち合い勝負です。 2つの文字列"Bang!"が与えられた場合、
どちらの人が最も速く銃を撃ったかを返します。 同じの場合は「引き分け」を返します。

例：
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1勝利"


showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2勝利"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "引き分け"

"""

def showdown(p1, p2):

    return "p1勝利" if p1.find("B") < p2.find("B") else "p2勝利" if p1.find("B") > p2.find("B") else "引き分け"

    # print(p1.find("B"))

    # if p1.find("B") < p2.find("B"):
    #     return "p1勝利"
    # elif p1.find("B") > p2.find("B"):
    #     return "p2勝利"
    # else:
    #     return "引き分け"

print(showdown(
  "   Bang!        ",
  "        Bang!   "
))


print(showdown(
  "               Bang! ",
  "             Bang!   "
))


print(showdown(
  "     Bang!   ",
  "     Bang!   "
))







































"""
Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".

Examples
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

# p1 draws his gun sooner than p2

showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"
Notes
Both strings are the same length.
"""

# def showdown(p1, p2):
#
#     # print(p1.find('B'))
#     # print(p2.find('B'))
#
#     return "p1" if p1.find("B") < p2.find("B") else "p2" if p1.find("B") > p2.find("B") else 'tie'
#
#
#     if p1.find("B") < p2.find("B"):
#         return "p1"
#     elif p1.find("B") > p2.find("B"):
#         return "p2"
#     else:
#         return "tie"
#
# print(showdown(
#   "   Bang!        ",
#   "        Bang!   "
# ))
#
# print(showdown(
#   "               Bang! ",
#   "             Bang!   "
# ))
#
# print(showdown(
#   "     Bang!   ",
#   "     Bang!   "
# ))



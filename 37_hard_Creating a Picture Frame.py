"""
Creating a Picture Frame
Create a function that takes the width, height and character and returns a picture frame as a 2D list.

Examples
get_frame(4, 5, "#") ➞ [
  ["####"],
  ["#  #"],
  ["#  #"],
  ["#  #"],
  ["####"]
]
# Frame is 4 characters wide and 5 characters tall.


get_frame(10, 3, "*") ➞ [
  ["**********"],
  ["*        *"],
  ["**********"]
]
# Frame is 10 characters and wide and 3 characters tall.


get_frame(2, 5, "0") ➞ "invalid"
# Frame's width is not more than 2.
Notes
Remember the gap.
Return "invalid" if width or height is 2 or less (can't put anything inside).
"""

def get_frame(w, h, ch):

    if w <= 2 or h <= 2:
        return 'invalid'
    return [[ch*w]] + [["{0}{1}{0}".format(ch, ' '*(w-2))] for i in range(h-2)] + [[ch*w]]

    # if w <= 2 or h <= 2:
    #     return 'invalid'
    # head = ch*w
    # side = ch + ' ' * (w-2) + ch
    # return [[i] for i in [head] + [side]*(h-2) + [head]]



    # res = []
    #
    # if not w < 3 and not h < 3:
    #     for i in range(0, h):
    #         if i == 0:
    #             res.append([ch * w])
    #             continue
    #         elif i == h-1:
    #             res.append([ch * w])
    #             continue
    #         else:
    #             pic = []
    #             for i in range(0, w):
    #                 if i == 0:
    #                     pic.append(ch)
    #                 elif i == w-1:
    #                     pic.append(ch)
    #                 else:
    #                     pic.append(" ")
    #             res.append([''.join(pic)])
    #     return res
    # return "invalid"

print(get_frame(4, 5, "#"))
print(get_frame(10, 3, "*"))
print(get_frame(3, 3, "0"))

print(get_frame(1, 6, "["))
print(get_frame(10, 2, "`"))
print(get_frame(5, 2, "F"))
print(get_frame(7, 2, "?"))
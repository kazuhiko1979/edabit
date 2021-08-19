"""
Create a function that takes a list of 4 tuples. Each tuple consists of two numbers representing the x coordinate and y coordinate of a point on the Cartesian plane. Return True if these 4 points form a rectangle, False if they don't. Rectangles can be upright or tilted.

Examples
is_rectangle([(-1, -2), (-1, 3), (1, -1), (-3, 2)]) ➞ True

is_rectangle([(-1, -2), (-1, -2), (1, -1), (-3, 2)]) ➞ False

is_rectangle([(7, 4), (1, -2), (1, 4), (7, -2)]) ➞ True
Notes
A rectangle is a quadrilateral (4-sided polygon) with 4 right angles (90 degrees).
"""
"""
bool isRectangle(double x1, double y1,
                 double x2, double y2,
                 double x3, double y3,
                 double x4, double y4)
{
  double cx,cy;
  double dd1,dd2,dd3,dd4;

  cx=(x1+x2+x3+x4)/4;
  cy=(y1+y2+y3+y4)/4;

  dd1=sqr(cx-x1)+sqr(cy-y1);
  dd2=sqr(cx-x2)+sqr(cy-y2);
  dd3=sqr(cx-x3)+sqr(cy-y3);
  dd4=sqr(cx-x4)+sqr(cy-y4);
  return dd1==dd2 && dd1==dd3 && dd1==dd4;
}
"""


def is_rectangle(lst):

    x1 = lst[0][0]
    y1 = lst[0][1]
    x2 = lst[1][0]
    y2 = lst[1][1]
    x3 = lst[2][0]
    y3 = lst[2][1]
    x4 = lst[3][0]
    y4 = lst[3][1]

    cx = (x1+x2+x3+x4)/4
    cy = (y1+y2+y3+y4)/4

    dd1 = pow((cx-x1), 2) + pow((cy-y1), 2)
    dd2 = pow((cx-x2), 2) + pow((cy-y2), 2)
    dd3 = pow((cx-x3), 2) + pow((cy-y3), 2)
    dd4 = pow((cx-x4), 2) + pow((cy-y4), 2)

    return dd1 == dd2 and dd1 == dd3 and dd1 == dd4

print(is_rectangle([(-1, -2), (-1, 3), (1, -1), (-3, 2)]))
print(is_rectangle([(-1, -2), (-1, -2), (1, -1), (-3, 2)]))
print(is_rectangle([(-3, 2), (8, -1), (7, 4), (-2, -3)]))
print(is_rectangle([(-3, 2), (8, -1), (7, 4), (-4, 7)]))
print(is_rectangle([(7, 4), (1, -2), (1, 4), (7, -2)]))
print(is_rectangle([(7, 4), (1, -2), (1, 3), (7, -1)]))

print(is_rectangle([(0, 8), (-1, 7), (7, -1), (8, 0)]))
# print(is_rectangle([(0, 8), (1, 9), (7, -1), (8, 0)]))








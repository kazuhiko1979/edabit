def S(va, vb):
    return (va[0] - vb[0], va[1] - vb[1])


def dot(sa, sb):  # Eventually replaced with numpy.dot
    return (sa[0] * sb[0] + sa[1] * sb[1])


def norm(s):  # Eventually replaced by numpy.linalg.norm
    return (s[0] ** 2 + s[1] ** 2) ** .5


def isperp(a, b):  # Test if lines/vectors are perpendicular
    return dot(a, b) == 0


def ispar(a, b):  # Test if lines/vectors are parallel
    x = dot(a, b)
    y = norm(a) * norm(b)
    return x == y or x == -y


def iseq(a, b):  # Test if lines/vectors are equal in length
    return norm(a) == norm(b)


def f(L):
    # Define the four sides
    s = []
    for i in range(4):
        s.append(S(L[i], L[(i + 1) % 4]))  # I refer often so shorter names may eventually

    guess = 'other'

    eqsides = 0  # These 6 lines eventually golfed using integer arithmetic by returning an int from iseq()

    if iseq(s[0], s[2]):
        eqsides += 1
    if iseq(s[1], s[3]):
        eqsides += 1

    if eqsides == 2:
        # Opposite sides are equal, so square, rhombus, rectangle or parallelogram
        if iseq(s[0], s[1]):  # Equal adjacent sides, so square or rhombus
            guess = 'square' if isperp(s[0], s[1]) else 'rhombus'
        else:  # rectangle or Parallelogram
            guess = 'rectangle' if isperp(s[0], s[1]) else 'parallelogram'

    elif ispar(s[0], s[2]) or ispar(s[1], s[3]):
        guess = 'trapezoid'
    elif iseq(s[0], s[1]) or iseq(s[1], s[2]):
        guess = 'kite'
    return guess

# 参照
# https://codegolf.stackexchange.com/questions/127895/classify-quadrilaterals-help-me-with-my-math-exam
# https://stackoverflow.com/questions/5922027/how-to-determine-if-a-point-is-within-a-quadrilateral
# https://www.onlinemath4all.com/how-to-check-if-the-given-four-points-form-a-rhombus.html




# test suite:
print(f([(0, 0), (1, 0), (1, 1), (0, 1)]))  # -> square 正方形
print(f([(0, 0), (1, 1), (-1, 3), (-2, 2)]))  # -> rectangle 長方形
print(f([(0, 0), (5, 0), (8, 4), (3, 4)]))  # -> rhombus ひし形
print(f([(0, 0), (5, 0), (6, 1), (1, 1)]))  # -> parallelogram 平行四辺形
print(f([(0, 0), (4, 0), (3, 1), (1, 1)]))  # -> trapezoid/trapezium 台形
print(f([(0, 0), (1, 1), (0, 3), (-1, 1)]))  # -> kite 凧
print(f([(0, 0), (2, 0), (4, 4), (0, 1)]))  # -> quadrilateral その他(other)
print(f([(0, 0), (8, 0), (10, 12), (2, 6)]))  # -> quadrilateral　その他(other)







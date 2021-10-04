"""
Every quadratic curve y = a x² + b x + c has a vertex point: the turning point where the curve stops heading down and starts going up.

Given the values a, b and c, you need to return the coordinates of the vertex. Return your answers rounded to 2 decimal places.

Examples
find_vertex(1, 0, 25)  ➞ [0, 25]
# The vertex of y=x²+25 is at (0, 25).

find_vertex(-1, 0, 25) ➞ [0, 25]
# The vertex of y=-x²+25 is at (0, 25).

find_vertex(1, 10, 4) ➞ [-5, -21]
# The vertex of y=x²+10x+4 is at (-5, -21).
"""
from decimal import Decimal, Context

def find_vertex(a, b, c):

    x = - (b / (2 * a))
    y = a * (x ** 2) + b * x + c
    return decimal_normalize(x, y)


def decimal_normalize(x, y):
    """数値fの小数点以下を正規化し、文字列で返す"""
    def _remove_exponent(d):
        return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
    x = Decimal.normalize(Decimal(x))
    y = Decimal.normalize(Decimal(y))
    x = _remove_exponent(x)
    y = _remove_exponent(y)

    return [float(x), float(y)]


print(find_vertex(-1, 0, 25))
print(find_vertex(1, 10, 25))
print(find_vertex(8, 4, 0))
print(find_vertex(4, -200, 1000))
print(find_vertex(1, 10, 4))



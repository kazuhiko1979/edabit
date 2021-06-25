"""
Create a function that returns the simplified version of a fraction.

Examples
simplify("4/6") ➞ "2/3"

simplify("10/11") ➞ "10/11"

simplify("100/400") ➞ "1/4"

simplify("8/4") ➞ "2"
Notes
A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor.
If improper fractions can be transformed into integers, do so in your code (see example #4).
"""


def simplify(txt):

    target = "/"
    idx = txt.find(target)
    x = int(txt[:idx])
    y = int(txt[:idx:-1][::-1])


    def gcd(x, y):
        if x < y:
            return gcd(y, x)
        elif y == 0:
            return x
        elif x == x // y * y:
            return y
        else:
            return gcd(x - y, y)

    d = gcd(x, y)

    x = x // d
    y = y // d

    if y == 1:
        return str(x)
    else:
        return '{}/{}'.format(x, y)

print(simplify("4/6"))
print(simplify("10/11"))
print(simplify("100/400"))
print(simplify("8/4"))




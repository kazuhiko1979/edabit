"""
Create a function that uses bisection search to compute the approximative value of the square root of a number.

Use any integer or float as an argument.
Use a delta variable of 0.01 to know when a result is valid (i.e. if the result squared is between n - delta and n + delta, it's considered valid).
Examples
bisec_sqrt(69) ➞ 8.307

bisec_sqrt(16) ➞ 4.0

bisec_sqrt(12984771) ➞ 3603.439

bisec_sqrt(12.21) ➞ 3.494
"""
def bisec_sqrt(n):

    v = n
    x = n

    for i in range(1, 100):
        x = x - (x * x - v) / (2.0 * x)

    return round(x, 3)

print(bisec_sqrt(69))
print(bisec_sqrt(12984771))
print(bisec_sqrt(12.21))

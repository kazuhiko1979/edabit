"""
In mathematics, the harmonic series is the divergent infinite series:

Alternative Text

Its name derives from the concept of overtones, or harmonics in music.

Create a function that, given a precision parameter n, returns the value of the partial sum of the harmonic series up to n terms.

Examples
harmonic(3) ➞ 1.833

harmonic(1) ➞ 1.0

harmonic(5) ➞ 2.283
Notes
Round the result to the third decimal place.
"""
def harmonic(n):

    return round(sum([1 / i for i in range(1, n+1)]), 3)

print(harmonic(3))
print(harmonic(1))
print(harmonic(5))
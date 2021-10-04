"""
Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

How to solve:

Calculate the volume of the cylinder.
Convert cm³ into dm³.
1dm³ = 1L, 1L is 1Kg.
Examples
weight(4, 10) ➞ 0.5

weight(30, 60) ➞ 169.65

weight(15, 10) ➞ 7.07
Notes
I recommend importing math.
"""
import numpy as np
import math

def weight(r, h):

    volume = math.pi*pow(r, 2) * h
    return np.round(volume / 1000, decimals=2)

print(weight(4, 10))
print(weight(30, 60))
print(weight(15, 10))








"""
Javelin Parabolic Throw
Write a function that takes initial speed (v in m/s) and throw angle (a in degrees) and returns the maximum height and maximum range reached by javelin as a string.

Examples
javelin_throw(36.7, 45) ➞ "Ymax=34m, Xmax=137m"

javelin_throw(51.3, 20) ➞ "Ymax=16m, Xmax=172m"

javelin_throw(100.1, 89) ➞ "Ymax=511m, Xmax=36m"
Notes
Javelin starts moving at h=0m.
Gravitational acceleration is g=9.81 m/s^2.
All results should be rounded to the nearest whole number.
"""
# v2
import math

def javelin_throw(v, a):

	g = 9.81
	yMax = round((v * math.sin(math.radians(a))) ** 2 / (2 * g))
	xMax = round((v ** 2 / g) * math.sin(math.radians(2 * a)))
	return "Ymax={}m, Xmax={}m".format(yMax, xMax)


# v1
# import math
#
# def javelin_throw(v, a):
#
# 	g = 9.81
#
# 	vx = v * math.cos(math.radians(a))
# 	vy = v * math.sin(math.radians(a))
#
# 	y_max = round(vy ** 2 / (2 * g))
# 	x_max = round(vx * (vy + math.sqrt(vy ** 2 * g * 0)) / g * 2)
#
# 	return "Ymax={}m, Xmax={}m".format(y_max, x_max)






print(javelin_throw(36.7, 45))
print(javelin_throw(51.3, 20))
print(javelin_throw(100.1, 89))
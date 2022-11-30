"""
Calculate the Volume of a Pyramid
Create a function that takes the length, width, height (in meters) and output unit and returns the volume of a pyramid to three decimal places in the correct unit.

Examples
pyramid_volume(4, 6, 20, "centimeters") ➞ "160000000.000 cubic centimeters"

pyramid_volume(1843, 1823, 923, "kilometers") ➞ "1.034 cubic kilometers"

pyramid_volume(18, 412, 93, "millimeters") ➞ "229896000000000.000 cubic millimeters"
Notes
The units used are limited to: millimeters, centimeters, meters and kilometers.
Ensure you return the answer and add the correct unit in the format cubic <unit>.
"""
# v3
def pyramid_volume(length, width, height, unit):

	units = {
			"meters": 1,
			"centimeters": 100 ** 3,
			"kilometers" : 1000 ** -3,
			"millimeters": 1000 ** 3
			 }

	return '{:.3f} cubic {}'.format(length*width*height/3 * units[unit], unit)



# v2
# def pyramid_volume(length, width, height, unit):
#
# 	units = {
# 			"meters": 1,
# 			"centimeters": 100 ** 3,
# 			"kilometers" : 1000 ** -3,
# 			"millimeters": 1000 ** 3
# 			 }
#
# 	result = length * width * height / 3 * units[unit]
# 	return '{:.3f} cubic {}'.format(result, unit)

# v1
# def pyramid_volume(length, width, height, unit):
#
# 	units = {"meters": 1,
# 			"centimeters": 1000000,
# 			"kilometers" : 0.000000001,
# 			"millimeters": 1000000000
# 			 }
#
# 	result = length * width * height / 3 * units[unit]
# 	return "{} {} {}".format(round(result, 3), "cubic", unit) \
# 		if unit == "kilometers" else "{} {} {}".format('{:.03f}'.format(result), "cubic", unit)


print(pyramid_volume(10, 14, 6, "meters"))
print(pyramid_volume(8, 12, 2, "centimeters"))
print(pyramid_volume(92, 1245, 1923, "kilometers"))
print(pyramid_volume(19, 254, 21, "millimeters"))
print(pyramid_volume(13.6, 62.2, 6, "meters"))
print(pyramid_volume(4230, 923, 1932, "kilometers"))




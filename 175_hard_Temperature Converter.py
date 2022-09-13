"""
Temperature Converter
Create a function that takes a list with temperature type, temperature, and a second temperature type. The temperature types can be Celsius, Fahrenheit, or Kelvin. Return the temperature type (in the list) converted into the second temperature type.

Examples
converter(["fahrenheit", 3] , "kelvin") ➞ 257.0

converter(["celsius", 10] , "fahrenheit") ➞ 50.0

converter(["celsius", 20] , "kelvin") ➞ 293.1
Notes
Round to one decimal place.
"""

def converter(a, b):

	if a[0] == "celsius" and b == "fahrenheit":
		return round(a[1] * 9 / 5 + 32, 1)
	if a[0] == "celsius" and b == "kelvin":
		return round(a[1] + 273.15, 1)

	if a[0] == "kelvin" and b == "fahrenheit":
		return round((a[1] - 273.15) * 9 / 5 + 32, 1)
	if a[0] == "kelvin" and b == "celsius":
		return round(a[1] - 273.15, 1)

	if a[0] == "fahrenheit" and b == "celsius":
		return round((a[1] - 32) * 5 / 9, 1)
	if a[0] == "fahrenheit" and b == "kelvin":
		return round((a[1] - 32) * 5 / 9 + 273.15, 1)


# print(converter(["celsius", 20], "kelvin"))
# print(converter(["celsius", 5], "kelvin"))
# print(converter(["celsius", 34], "fahrenheit"))
# print(converter(["celsius", -2], "fahrenheit"))
# print(converter(["kelvin", 18], "fahrenheit"))
print(converter(["kelvin", -10], "celsius"))
# print(converter(["fahrenheit", 7], "kelvin"))
# print(converter(["fahrenheit", 25], "celsius"))




# 数式
# (10°C×9÷5) + 32 ＝ 50°F

# 数式
# 20°C + 273.15 = 293.15 K

# 数式
# (18 K - 273.15) × 9 ÷ 5 + 32 = -427.3°F

# 数式
# -10 K - 273.15 = -283.1°C

# 数式
# (3°F - 32) × 5 ÷ 9 + 273.15 = 257.039 K

# 数式
# (25°F - 32) × 5 ÷ 9 = -3.889°C










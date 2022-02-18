"""
Series and Parallel Resistor Calculator
Create a function that takes a list of resistors and calculates the output of total resistance if the circuit is connected in parallel or in series.

Examples
resistance_calculator([10, 20, 30, 40, 50]) ➞ [4.38, 150]

resistance_calculator([25, 14, 65, 18]) ➞ [5.48, 122]

resistance_calculator([10, 10]) ➞ [5, 20]

resistance_calculator([0, 0, 0, 0]) ➞ [0, 0]

resistance_calculator([1.1, 2.1, 3.2, 4.3, 5.4, 6.5]) ➞ [0.44, 22.6]
Notes
Return parallel resistance as the first element and series resistance as second element of the list.
Round up the total resistance to two decimal places.
"""

def resistance_calculator(resistors):

	# return [round(0 if 0 in resistors else 1 / sum(1 / resistor for resistor in resistors), 2), round(sum(resistors), 2)]


	# try:
	# 	return [round(1/sum([1/resistor for resistor in resistors]), 2), round(sum(resistors), 2)]
	# except ZeroDivisionError:
	# 	return [0, sum(resistors)]

	total = 0

	if 0 in resistors:
		return [0, round(sum(resistors), 2)]
	else:
		for resistor in resistors:
			if resistor != 0:
				total += 1 / resistor
		return [round(1 / total, 2), round(sum(resistors),2)]

print(resistance_calculator([10, 20, 30, 40, 50]))
print(resistance_calculator([25, 14, 65, 18]))
print(resistance_calculator([0, 0, 0, 0]))
print(resistance_calculator([1.1, 2.1, 3.2, 4.3, 5.4, 6.5]))
print(resistance_calculator([332.963, 87.036]))
print(resistance_calculator([12345, 0]))
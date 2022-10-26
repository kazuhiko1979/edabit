"""
Musical Instrument Note Ranges
Musical instruments have a range of notes to play, some instruments having a much larger range than others.

Given the following ranges for the instrument, create a function that returns True if a given note is within a given instrument's range. Otherwise, return False.

Instrument	Range
Piccolo	D4-C7
Tuba	D1-F4
Guitar	E3-E6
Piano	A0-C8
Violin	G3-A7
Examples
instrument_range("Piccolo", "A3") ➞ False

instrument_range("Violin", "G6") ➞ True

instrument_range("Piano", "C8") ➞ True
Notes
Tests will only include natural notes (i.e. you will only deal with letters and numbers, no special characters).
The musical scale follows this pattern: ... A1, B1, C1, D1, E1, F1, G1, A2, B2 ...
You don't need to worry about invalid inputs.
"""
d = {
	'Piccolo': ['D4', 'C7'],
	'Tuba': ['D1', 'F4'],
	'Guitar': ['E3', 'E6'],
	'Piano': ['A0', 'C8'],
	'Violin': ['G3', 'A7']
	}

# v2
def instrument_range(instr, note):

	return d[instr][0][::-1] <= note[::-1] <= d[instr][1][::-1]


# v1
# alpha = ['A','B','C','D','E','F','G']
#
# inst = {
# 		'Piccolo': 'D4-C7',
# 		'Tuba': 'D1-F4',
# 		'Guitar': 'E3-E6',
# 		'Piano': 'A0-C8',
# 		'Violin': 'G3-A7'
# 		}
#
# def instrument_range(instr, note):
#
# 	start = inst[instr].split('-')[0]
# 	end = inst[instr].split('-')[1]
# 	code = [j + str(i) for i in range(0, 10) for j in alpha]
# 	note = [k for k, v in enumerate(code) if v == note][0]
#
# 	result = []
#
# 	for k, v in enumerate(code):
# 		if v == start:
# 			result.append(k)
# 		if v == end:
# 			result.append(k)
# 	return result[0] <= note <= result[1]

print(instrument_range("Piccolo", "A3"))
print(instrument_range("Violin", "G6"))
print(instrument_range("Piano", "C8"))

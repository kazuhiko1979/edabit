"""
Pyramidal Strings
In this challenge, you have to obtain a pyramidal version of a given string, transforming the string into a list containing a series of string slices that progressively increase or decrease steadily from the left to the right. Every slice containing two or more characters must have a space between every pair of characters, to permit a hypothetical vertical alignment. See the example below:

# REGULAR pyramidal version of "EDABIT"

[ "E",
 "D A",
"B I T" ]
Depending on the given _type, you have to obtain a regular pyramid starting from its vertex (_type === "REG") as in the example above, or a reversed pyramid starting from its base (_type === "REV") as in the example below:

# REVERSED pyramidal version of "EDABIT"

["E D A",
  "B I",
   "T"  ]
Every pyramid must follow the same steadily increment/decrement of its slices (or rows) by exactly one character (excluding spaces), so that not every string can be transformed in a pyramid! See the example below:

# Regular pyramidal version of "PYRAMID"

[ "P",
 "Y R",
"A M I" ]

# Letter "D" can't be placed in the pyramid
Given as parameters a string and a _type, implement a function that returns:

A string "Error!" if the pyramidal version can't be obtained from the given string.
A list containing the regular pyramidal version of the string if the given _type is equal to "REG".
A list containing the reversed pyramidal version of the string if the given _type is equal to "REV".
Examples
pyramidal_string("EDABIT", "REG") ➞ ["E", "D A", "B I T"]

pyramidal_string("EDABIT", "REV") ➞ ["E D A", "B I", "T"]

pyramidal_string("PYRAMID", "REG") ➞ "Error!"

pyramidal_string("!", "REV") ➞ ["!"]

pyramidal_string("", "REG") ➞ []
Notes
If the given string has just one character, the returned list will contain that single character. If the given string is empty, the returned list will be empty.
Remember to insert a space between every character inside the rows containing two or more characters.
The increment and the decrement of the rows in a pyramidal string are equal to one character more or less than the previous, depending on the given _type.
You have to find a discriminant rule to establish if a string can be transformed into a pyramid, without creating single exceptions for every given case. What is suggesting to you the shape of a pyramid seen frontally?
"""

def calculate_pyramid_levels(string_count):
    level = 0
    total_strings = 0

    while total_strings < string_count:
        level += 1
        total_strings += level

    return level

def is_valid_pyramid(levels, element_lengths):
    return len(set(element_lengths)) == levels and 0 not in element_lengths

def pyramidal_string(string, _type):
	pyramid_level = calculate_pyramid_levels(len(string))

	if not pyramid_level:
		return []

	if _type == "REG":
		start = 0
		result = []

		for level in range(1, pyramid_level + 1):
			end = start + level
			result.append(string[start:end])
			start = end

		if is_valid_pyramid(pyramid_level, [len(s) for s in result]):
			return [' '.join(word) for word in result]
		return "Error!"

	if _type == "REV":
		start = 0
		result = []

		for level in range(pyramid_level, 0, -1):
			end = start + level
			result.append(string[start:end])
			start = end
		if is_valid_pyramid(pyramid_level, [len(s) for s in result]):
			return [' '.join(word) for word in result]
		return "Error!"

print(pyramidal_string("", "REG"))
print(pyramidal_string("ZAPHODBEEBLEBROX", "REG"))
print(pyramidal_string("THEHITCHIKERGUIDETOTHEGALAXY", 'REG'))
print(pyramidal_string("HOTBLACKDESIATO", "REG"))
print(pyramidal_string("TRILLIAN", "REG"))
print(pyramidal_string("APERFECTLYNORMALBEAST", "REG"))
print(pyramidal_string("RESTAURANTATTHEENDOFTHEUNIVERSE", "REG"))

print(pyramidal_string("?", "REV"))
print(pyramidal_string("ARTHURDENT", "REV"))
print(pyramidal_string("DONTPANIC", "REV"))
print(pyramidal_string("MARVIN", "REV"))
print(pyramidal_string("42", "REV"))




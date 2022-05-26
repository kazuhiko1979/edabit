"""
Validating a Set in the Set Game
In the game Set, three cards form a set if each of the cards are identical or completely different for each of the four properties. All three cards must:

Have the same color or different colors.
Have the same number or different numbers.
Have the same shades or different shades.
Have the same shape or different shapes.
The four properties are:

Colors: red, purple, green
Numbers: 1, 2, 3
Shades: empty, lined, full
Shapes: squiggle, oval, diamond
Here, a set is represented by an array containing three cards. Each card is represented by an object of properties and values. Write a function that determines whether three cards constitute a valid set.

Here is an example of a set:

[
  { "color": "red", "number": 1, "shade": "empty", "shape": "squiggle" },
  { "color": "red", "number": 2, "shade": "lined", "shape": "diamond" },
  { "color": "red", "number": 3, "shade": "full", "shape": "oval" }
]

# "Same" properties: color
# "Different" properties: numbers, shading and shapes
The following is not a set:

[
  { "color": "red", "number": 1, "shade": "empty", "shape": "squiggle" },
  { "color": "red", "number": 2, "shade": "lined", "shape": "diamond" },
  { "color": "purple", "number": 3, "shade": "full", "shape": "oval" }
]

# Colors are not all identical, but not all different.
Examples
is_set([
  { "color": "green", "number": 1, "shade": "empty", "shape": "squiggle" },
  { "color": "green", "number": 2, "shade": "empty", "shape": "diamond" },
  { "color": "green", "number": 3, "shade": "empty", "shape": "oval" }
]) ➞ True

is_set([
  { "color": "purple", "number": 1, "shade": "full", "shape": "oval" },
  { "color": "green", "number": 1, "shade": "full", "shape": "oval" },
  { "color": "red", "number": 1, "shade": "full", "shape": "oval" }
]) ➞ True

is_set([
  { "color": "purple", "number": 3, "shade": "full", "shape": "oval" },
  { "color": "green", "number": 1, "shade": "full", "shape": "oval" },
  { "color": "red", "number": 3, "shade": "full", "shape": "oval" }
]) ➞ False
Notes
A set cannot have 2/3 cards having the same property. Either all must share that property, or none will share that particular property.
"""

def is_set(cards):

	# v3
	vals = [i for j in cards for i in j.values()]
	return False if any(vals.count(k) == 2 for k in vals) else True


	# V2
	# properties = ['color', 'number', 'shade', 'shape']
	# set_properties =  [len(set(card[p] for card in cards)) for p in properties]
	# return all(prop == 3 or prop == 1 for prop in set_properties)


	# v1
	# color = []
	# number = []
	# shade = []
	# shape = []
	#
	# for card in cards:
	# 	for key, val in card.items():
	# 		if key == 'color': color.append(val)
	# 		if key == 'number': number.append(val)
	# 		if key == 'shade': shade.append(val)
	# 		if key == 'shape': shape.append(val)
	#
	# if len(set(color)) == 1 or len(set(color)) == 3:
	# 	if len(set(number)) == 1 or len(set(number)) == 3:
	# 		if len(set(shade)) == 1 or len(set(shade)) == 3:
	# 			if len(set(shape)) == 1 or len(set(shape)) == 3:
	# 				return True
	# return False

print(is_set(
[{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"},
{"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"}]
))

print(is_set(
[{"color": "purple", "number": 3, "shade": "full", "shape": "oval"},
{"color": "green", "number": 1, "shade": "full", "shape": "oval"},
{"color": "red", "number": 3, "shade": "full", "shape": "oval"}]
))

print(is_set(
[{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
{"color": "red", "number": 2, "shade": "lined", "shape": "diamond"},
{"color": "purple", "number": 3, "shade": "full", "shape": "oval"}]
))

print(is_set(
[{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
{"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
{"color": "red", "number": 1, "shade": "lined", "shape": "oval"}]
))

print(is_set(
[{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"},
{"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
{"color": "red", "number": 1, "shade": "lined", "shape": "oval"}]
))

print(is_set(
[{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
{"color": "red", "number": 2, "shade": "lined", "shape": "diamond"},
{"color": "red", "number": 3, "shade": "full", "shape": "oval"}]
))

print(is_set(
[{"color": "green", "number": 1, "shade": "empty", "shape": "squiggle"},
{"color": "green", "number": 2, "shade": "empty", "shape": "diamond"},
{"color": "green", "number": 3, "shade": "empty", "shape": "oval"}]
))

print(is_set(
[{"color": "purple", "number": 1, "shade": "full", "shape": "oval"},
{"color": "green", "number": 1, "shade": "full", "shape": "oval"},
{"color": "red", "number": 1, "shade": "full", "shape": "oval"}]
))





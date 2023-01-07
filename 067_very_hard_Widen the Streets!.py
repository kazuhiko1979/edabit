"""
Widen the Streets!
Given a list of strings depicting a row of buildings, create a function which sets the gap between buildings as a given amount.

Examples
widen_streets([
  "###   ## #",
  "### # ## #",
  "### # ## #",
  "### # ## #",
  "### # ## #"
], 3) ➞
[
  "###       ##   #",
  "###   #   ##   #",
  "###   #   ##   #",
  "###   #   ##   #",
  "###   #   ##   #"
]

widen_streets([
  "## ### ###",
  "## ### ###",
  "## ### ###",
  "## ### ###"
], 2) ➞
[
  "##  ###  ###",
  "##  ###  ###",
  "##  ###  ###",
  "##  ###  ###"
]

widen_streets([
  "# # # # #"
], 2) ➞
[
  "#  #  #  #  #"
]
Notes
Buildings may be different sizes.
There will always be a starting gap size of one character.
"""
# v3
def widen_streets(lst, n):

	return [i.replace(" ", " *").replace(" ", " "*n).replace(" *", " ") for i in lst]

# v2
# def widen_streets(lst, n):
#
# 	# 縦にする
# 	lst = [list(x) for x in list(zip(*lst[::-1]))]
#
# 	a = []
# 	for x in lst:
# 		if x[0] == ' ':
# 			for i in range(n):
# 				a.append(x)
# 		else:
# 			a.append(x)
# 	# 横に戻す
# 	return [''.join(x) for x in list(zip(*a))][::-1]



# # v1 not working
# def widen_streets(lst, n):
#
# 	streets = [j.split() for i in lst for j in i.split(',')]
#
# 	result = []
#
# 	for street in streets:
# 		space = " " * n
# 		result.append(space.join(street))
# 	return result


print(widen_streets([
	"# # # # #"
], 2))

print(widen_streets([
  "###   ## #",
  "### # ## #",
  "### # ## #",
  "### # ## #",
  "### # ## #"
], 3))

print(widen_streets([
  "## ### ###",
  "## ### ###",
  "## ### ###",
  "## ### ###"
], 2))
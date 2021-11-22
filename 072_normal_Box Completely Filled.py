"""
Create a function that checks if the box is completely filled with the asterisk symbol *.

Examples
completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
]) ➞ True

completely_filled([
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
]) ➞ False

completely_filled([
  "###",
  "#*#",
  "###"
]) ➞ True

completely_filled([
  "##",
  "##"
]) ➞ True
Notes
Boxes of size n <= 2 are considered automatically filled (see example #4).
Empty space will always be a space character (" ").
"""

def completely_filled(lst):

    # return not any(' ' in i for i in lst)

    # return not ' ' in ''.join(lst)




    # bool = True
    #
    # for i in lst:
    #     if i[0] == "#" and i[-1] == "#":
    #         for j in i[1:-1]:
    #             if j == ' ':
    #                 bool = False
    #
    # return bool

    # if not bool:
    #     return False
    # else:
    #     return True

print(completely_filled([
		"#"
	]))

print(completely_filled([
		"##",
		"##"
	]))

print(completely_filled([
		"##",
		"##"
	]))

print(completely_filled([
		"######",
		"#****#",
		"#****#",
		"#****#",
		"#****#",
		"######"
	]))


print(completely_filled([
		"#####",
		"#***#",
		"#***#",
		"#***#",
		"#####"
	]))

print(completely_filled([
		"#####",
		"#* *#",
		"#***#",
		"#***#",
		"#####"
	]))

print(completely_filled([
		"######",
		"#* **#",
		"#****#",
		"#* **#",
		"#*** #",
		"######"
	]))

print(completely_filled([
		"######",
		"#* **#",
		"#* **#",
		"#* **#",
		"#* **#",
		"######"
	]))

"""
Simon Says
Simon asks you to perform operations on a list of numbers that only he tells you. You should ignore all other instructions given. Create a function which evaluates a list of commands (written in plain English) if the command begins with Simon says. Return the result as an integer.

Examples
simon_says([
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
]) ➞ 10

simon_says([
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
]) ➞ 24

simon_says([
  "Firstly, add 4",
  "Simeon says subtract 100"
]) ➞ 0
Notes
If no instructions are given by Simon, return 0.
For the sake of simplicity, there will be no command for dividing.
"""
# v2
def simon_says(lst):

	res = 0

	d = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/', ' by ': '', }
	for i in lst:
		if i.startswith("Simon says"):
			for txt, op in d.items():
				i = i.replace(txt, op)
			res = eval('{}{}'.format(res, i[11:]))
	return res


# v1
# def simon_says(lst):
#
# 	result = 0
#
# 	for i in list(lst):
#
# 		if "Simon" in i and "add" in i:
# 			result += int(i.split()[-1])
#
# 		if "Simon" in i and "multiply" in i:
# 			result *= int(i.split()[-1])
#
# 		if "Simon" in i and "subtract" in i:
# 			result -= int(i.split()[-1])
#
# 	return result


print(simon_says([
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
]))
#
print(simon_says([
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
]))
# #
# #
print(simon_says([
  "Firstly, add 4",
  "Simeon says subtract 100"
]))
#
print(simon_says(["Simeon says subtract 46", "Firstly, multiply by 3", "Simon says add 18", "Then subtract 50", "Next, multiply by 2", "Then add 17", "Simeon says multiply by 43", "Now add 13", "Now subtract 32", "Firstly, multiply by 35", "Simon says subtract 22", "Joshua says subtract 48", "Simon says subtract 45", "Simon says add 7", "Simon says add 25", "Simeon says add 13"]))
print(simon_says(["Firstly, multiply by 19", "Simon says add 6", "Next, add 29", "Simon says add 50", "Joshua says multiply by 27"]))
print(simon_says(["Now add 44", "Now multiply by 27", "Simon says multiply by 30", "Now subtract 4", "Then multiply by 45"]))

print(simon_says(["Now subtract 41", "Now add 30", "Simon says multiply by 46", "Firstly, subtract 37", "Now multiply by 6", "Then multiply by 19", "Simon says add 23", "Simon says subtract 28"]))

print(simon_says(["Now multiply by 46", "Simeon says subtract 15", "Then subtract 46", "Simon says subtract 18", "Next, multiply by 48", "Simeon says subtract 46", "Simeon says multiply by 24", "Next, add 38", "Now multiply by 14", "Simon says subtract 46", "Simon says multiply by 30"]))
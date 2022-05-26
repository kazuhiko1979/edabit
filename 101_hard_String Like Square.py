"""
String Like Square
Create a function that takes a number and returns a string like square.

Examples
create_square(-1) ➞ ""

create_square(0) ➞ ""

create_square(1) ➞ "#"

create_square(2) ➞ "##\n##"

create_square(3) ➞ "###\n# #\n###"

create_square(4) ➞ "####\n#  #\n#  #\n####"
"####
#  #
#  #
####"
"""
def create_square(length):

	# v3
	if length == None or length < 1:
		return ""
	elif length == 1:
		return "#"
	else:
		top = ["#" * length]
		bot = ["#" * length]
		mid = ["#" + " " * (length-2) + "#"] * (length-2)
		return '\n'.join(top+mid+bot)

		# return "#" * length + "\n" + ("#" + " " * (length-2) + '#\n') * (length-2) + "#" * length

	# v2
	# if length == None or length < 1:
	# 	return ""
	# if length == 1:
	# 	return "#"
	# square = "#" * length + "\n"
	# for i in range(1, length - 1):
	# 	square += "#" + (" " * (length -2)) + "#\n"
	# square += "#" * length
	# return square


	# V1
	# up = list("#" * length)
	# bottom = '#' * length
	#
	# interim_num = length - 2
	#
	# temp = []
	#
	# if length <= 0:
	# 	return ""
	# elif length == 1:
	# 	return "#"
	# else:
	# 	for key, val in enumerate(up):
	# 		if key != 0:
	# 			temp.append(" ")
	# 		else:
	# 			temp.append(val)
	# 	temp[-1] = "#"
	# 	interim = ''.join(temp)
	#
	# 	text = ""
	# 	for i in ''.join(up) + "\n", (interim + "\n") * interim_num + bottom:
	# 		text += i
	# 	return text

print(create_square(0))
print(create_square(1))
print(create_square(3))
print(create_square(4))
print(create_square(10))







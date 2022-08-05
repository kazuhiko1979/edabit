"""
ust Find the Vertex
Today Juan learned to graph quadratic equations, so he chose to speed up the process and avoid having to write a lot of steps in his notebook to find the vertex. Just help him locate the vertex.

Ok, I am going to give you some advantages. The first is that you will not have to perform so many steps. The equations will have an easy structure to avoid much complexity.

Here I will leave you a shorter explanation of how we can find the vertex.

We have the following equation:

-5x ^ 2 + 50x -120
Now we apply the formula to locate the vertex:

-b / (2 * a)
We divide our second term by 2 multiplied by the first term. Remember to use the negative sign in b. It would look like this:

-50 / (2 * -5) = 5
... The third term will be insufficient in the challenge, but I wanted to add it to see if it complicates you.

... Remember to return the result rounded to zero decimals.

Examples
find_vertex("-5x + 50x -120") ➞ 5

find_vertex("-6x + 36x -72") ➞ 3

find_vertex("7x +14x +28") ➞ -1
Notes
List comprehension and unpacking is useful in this challenge :)
"""

import re

# def find_vertex(x):
#
# 	a,b,c = re.findall(r'-?\d+', x)
# 	print(a,b,c)
#
# 	return -int(b) // (2*int(a))


# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
#
def find_vertex(txt, a=0, b=0):

	if a == 0 and b == 0:
		if type(txt) == list:
			for i in txt:
				if 'x' in i:
					a = i
					a = int(str(i[:-1]))
					txt.remove(i)
					return find_vertex(txt, a, b)
		else:
			txt = txt.split()
			return find_vertex(txt)
	else:
		if type(txt) == list:
			for i in txt:
				if 'x' in i:
					b = i
					b = int(str(i[:-1]))
					return calc_a_b(a, b)


def calc_a_b(a, b):

	return -int(b) // (2*int(a))

print(find_vertex("-5x + 50x -120"))
print(find_vertex("-6x + 36x -72"))
print(find_vertex("7x +14x +28"))
print(find_vertex('4x -20x +12'))
print(find_vertex('2x -18x -20'))
print(find_vertex('9x +81x -27'))
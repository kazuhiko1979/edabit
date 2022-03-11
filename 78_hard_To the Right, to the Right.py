"""
To the Right, to the Right!
Create a class that imitates a select screen. For simplicity, the cursor can only move right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the method to_the_right, which moves the cursor one element to the right.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"
menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"
Notes
The cursor should wrap back round to the start once it reaches the end.
"""

class Menu:
	def __init__(self, lst):
		self.lst = lst
		self.idx = 0

	def to_the_right(self):

		if self.idx == len(self.lst) - 1:
			self.idx = 0
		else:
			self.idx += 1

	def display(self):
		output = []
		for idx, i in enumerate(self.lst):
			if self.idx == idx:
				output.append([i])
			else:
				output.append(i)

		print(output)

menu = Menu([1, 2, 3])
menu.to_the_right()
menu.to_the_right()
menu.to_the_right()
menu.to_the_right()
menu.display()

menu2 = Menu(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
menu2.to_the_right()
menu2.to_the_right()
menu2.to_the_right()
menu2.to_the_right()
menu2.display()
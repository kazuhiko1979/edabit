"""
Block the Square in Tic Tac Toe
Create a function that returns a number which can block the player from reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2, bottomleft is 6, and bottomright is 8.

Create a function that takes two numbers a, b and returns another number.
This number should be the final one in a line to block the player from winning.
Examples
block_player(0, 3) ➞ 6

block_player(0, 4) ➞ 8

block_player(3, 5) ➞ 4
Notes
The values given will always have two filled squares in a line.
"""
import numpy as np

def block_player(a, b):

	board = np.array(range(9))
	board[a], board[b] = 9, 9
	board = board.reshape(3, 3)


	for r in board:
		if len(set(r)) == 2:
			return sorted(list(set(r)), reverse=True).pop()

	for c in board.T:
		if len(set(c)) == 2:
			return sorted(list(set(c)), reverse=True).pop()

	if len(set(np.diag(board))) == 2:
		return sorted(list(set(np.diag(board))), reverse=True).pop()

	if len(set(np.diag(np.fliplr(board)))) == 2:
		return sorted(list(set(np.diag(np.fliplr(board)))), reverse=True).pop()



print(block_player(0, 3))
print(block_player(0, 8))
print(block_player(4, 8))
print(block_player(2, 5))
print(block_player(1, 7))
print(block_player(0, 4))
print(block_player(3, 5))





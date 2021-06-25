"""
Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is
a win for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix,
and "E" represents an empty spot.

Examples
board([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]) ➞ "X"

board([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]) ➞ "O"

board([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]) ➞ "Draw"
Notes
Make sure that if O wins, you return the letter "O" and not the integer 0 (zero)
and if it's a draw, make sure you return the capitalised word "Draw".
If you return "X" or "O", make sure they're capitalised too.
"""

def tic_tac_toe(board):

    tate_0 = [board[i][0] for i in range(len(board))]
    tate_1 = [board[i][1] for i in range(len(board))]
    tate_2 = [board[i][2] for i in range(len(board))]

    naname_1 = [board[i][j] for i, j in enumerate(range(len(board)))]
    naname_2 = [board[i][j] for i, j in enumerate(reversed(range(len(board))))]

    board = board + [tate_0] + [tate_1] + [tate_2] + [naname_1] + [naname_2]

    for i in board:
        # 横
        if set(i) == {'X'}:
            return "Player 1 wins"
        if set(i) == {'O'}:
            return "Player 2 wins"
    else:
        return "It's a Tie"

print(tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]))

print(tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]))
#
print(tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]))
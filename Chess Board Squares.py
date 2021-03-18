"""
Create a function that takes a code of chess board square and return his color.
Examples
A1 ➞ black
E5 ➞ black
D1 ➞ white
"""
def chess_board(pole):

    l, n = list(pole)
    return "black" if ord(l) % 2 == int(n) % 2 else "white"


    # pole = pole.lower()
    # alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    #
    # pol_num = alpha_list.index(pole[0]) + 1
    #
    # if pol_num % 2 == 0 and int(pole[-1]) % 2 == 0:
    #         return "black"
    # if pol_num % 2 == 0 and int(pole[-1]) % 2 != 0:
    #         return "white"
    # if pol_num % 2 != 0 and int(pole[-1]) % 2 == 0:
    #         return "white"
    # if pol_num % 2 != 0 and int(pole[-1]) % 2 != 0:
    #         return "black"




print(chess_board("A1"))
print(chess_board("B1"))
print(chess_board("C1"))
print(chess_board("E1"))
print(chess_board("D1"))
print(chess_board("F5"))
print(chess_board("H8"))
print(chess_board("A8"))
print(chess_board("H7"))
print("+" * 10)
print(chess_board("A1"))
print(chess_board("A2"))
print(chess_board("A3"))
print(chess_board("A4"))
print(chess_board("A5"))
print(chess_board("A6"))
print(chess_board("A7"))
print(chess_board("A8"))

print("+" * 10)
print(chess_board("H1"))
print(chess_board("H2"))
print(chess_board("H3"))
print(chess_board("H4"))
print(chess_board("H5"))
print(chess_board("H6"))
print(chess_board("H7"))
print(chess_board("H8"))





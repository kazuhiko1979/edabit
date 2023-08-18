"""
Magic Square Check
Make a function that takes a 2D list and returns True if it is a Magic Square and False if it is not. A Magic Square is an arrangement of numbers in a square in such a way that the sum of each row, column, and diagonal is one constant number, the "magic constant".

Examples
is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) ➞ True

# Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
# Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
# Diagonals: 2+5+8 = 6+5+4 = 15
is_magic([[1, 2], [3, 4]]) ➞ False

# Rows: 1+2 = 3 != 3+4 = 7
# Columns: 1+3 = 4 != 2+4 = 6
# Diagonals: 1+4 = 2+3 = 5
Notes
For this challenge, I will only be testing with magic squares made with whole numbers ranging from 1 to n^2 where n in the length of a side of the square.
"""
def is_magic(square):

	if square == []:
		return True
	flatten = sorted([e for inner_list in square for e in inner_list])
	len_square = [len(r) for r in square]

	if len(set(len_square)) == 1:
		side_square = [x for x in range(1, (set(len_square).pop())**2 + 1)]
	else:
		return False

	if flatten != side_square:
		return False
	else:
		rows = set([sum(i) for i in square]).pop()
		columns = set([sum(i) for i in list(zip(*square))]).pop()
		top_left = sum([square[i][i] for i in range(len(square))])
		top_right = sum([square[i][len(square) - 1 - i] for i in range(len(square))])
		return len(set([rows, columns, top_left, top_right])) == 1


print(is_magic([]))
print(is_magic([[1]]))
print(is_magic([[2]]))
print(is_magic([[1, 2], [3, 4]]))
print(is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(is_magic([[4,3,8],[9,5,1],[2,7,6]]))
print(is_magic([[9,5,1],[4,3,8],[2,7,6]]))

print(is_magic([[5,15,16,2],[10,8,7,13],[6,12,11,9],[17,3,4,14]]))
print(is_magic([[1,15,14,4],[10,11,8,5],[7,6,9,12],[16,2,3,13]]))
print(is_magic([[4,15,14,1],[5,11,8,10],[12,6,9,7],[13,2,3,16]]))
print(is_magic([[1,15,4,14],[10,11,5,8],[7,6,12,9],[16,2,13,3]]))
print(is_magic([[1,15,14,4],[10,11,8,5],[7,6,9,12],[16,2,3,13],[1,7,7,1,0,3]]))
print(is_magic([[25,13,1,19,7],[16,9,22,15,3],[12,5,18,6,24],[8,21,14,2,20],[4,17,10,23,11]]))
print(is_magic([
[93, 108, 123, 138, 153, 168, 1, 16, 31, 46, 61, 76, 91],
[107, 122, 137, 152, 167, 13, 15, 30, 45, 60, 75, 90, 92],
[121, 136, 151, 166, 12, 14, 29, 44, 59, 74, 89, 104, 106],
[135, 150, 165, 11, 26, 28, 43, 58, 73, 88, 103, 105, 120],
[149, 164, 10, 25, 27, 42, 57, 72, 87, 102, 117, 119, 134],
[163, 9, 24, 39, 41, 56, 71, 86, 101, 116, 118, 133, 148],
[8, 23, 38, 40, 55, 70, 85, 100, 115, 130, 132, 147, 162],
[22, 37, 52, 54, 69, 84, 99, 114, 129, 131, 146, 161, 7],
[36, 51, 53, 68, 83, 98, 113, 128, 143, 145, 160, 6, 21],
[50, 65, 67, 82, 97, 112, 127, 142, 144, 159, 5, 20, 35],
[64, 66, 81, 96, 111, 126, 141, 156, 158, 4, 19, 34, 49],
[78, 80, 95, 110, 125, 140, 155, 157, 3, 18, 33, 48, 63],
[79, 94, 109, 124, 139, 154, 169, 2, 17, 32, 47, 62, 77]
]))
#
print(is_magic([
[93, 108, 123, 138, 153, 168, 1, 16, 31, 46, 61, 76, 91],
[107, 122, 137, 152, 167, 13, 15, 30, 45, 60, 75, 90, 92],
[121, 136, 151, 166, 12, 14, 29, 44, 59, 74, 89, 104, 106],
[135, 150, 165, 11, 26, 28, 43, 58, 73, 88, 103, 105, 120],
[149, 164, 10, 25, 27, 42, 57, 72, 87, 102, 117, 119, 134],
[163, 9, 24, 39, 41, 56, 71, 86, 101, 116, 118, 133, 148],
[8, 23, 38, 40, 55, 70, 85, 100, 115, 130, 132, 147, 162],
[22, 37, 52, 54, 69, 84, 99, 114, 129, 131, 146, 161, 7],
[36, 51, 53, 68, 83, 98, 113, 128, 143, 145, 160, 6, 21],
[50, 65, 67, 82, 97, 112, 127, 142, 144, 159, 5, 20, 35],
[64, 66, 81, 96, 111, 126, 141, 156, 158, 4, 19, 34, 49],
[78, 80, 95, 110, 125, 140, 155, 157, 3, 18, 33, 48, 63],
[77, 94, 109, 124, 139, 154, 169, 2, 17, 32, 47, 62, 79]
]))


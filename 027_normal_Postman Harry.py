import numpy as np

# po = [
#   [1, 2, 3, 4, 5],
#   [6, 7, 8, 9, 10],
#   [11, 12, 13, 14, 15]
# ]

def harry(po, r=0, c=0):
    if po == [[]]:
        return -1
    if r>=len(po) or c>=len(po[0]):
        return 0
    return po[r][c] + max(harry(po, r+1, c), harry(po, r, c+1))

    # po_T = np.array(po).T
    # if po == [[]]:
    #     return -1
    # return sum(po_T[0]) + sum(po[len(po)-1]) - po[len(po)-1][0]


print(harry([[]]))
print(harry([[5]]))
print(harry([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]))

print(harry([
	[9, 9, 9],
	[0, 0, 9],
	[0, 0, 9]
]))

print(harry([
	[5, 2],
	[5, 2],
	[5, 2],
	[5, 2]
]))

print(harry([
	[5, 6, 2, 5, 1],
	[7, 2, 4, 1, 2],
	[0, 7, 5, 2, 14],
	[9, 5, 12, 5, 9],
	[19, 5, 2, 6, 2]
]))

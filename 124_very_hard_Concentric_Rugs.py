"""
Concentric Rugs
Create a function that takes in parameter n and generates an n x n (where n is odd) concentric rug.

The center of a concentric rug is 0, and the rug "fans-out", as show in the examples below.

Examples
generate_rug(1) ➞ [
  [0]
]

generate_rug(3) ➞ [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]

generate_rug(5) ➞ [
  [2, 2, 2, 2, 2],
  [2, 1, 1, 1, 2],
  [2, 1, 0, 1, 2],
  [2, 1, 1, 1, 2],
  [2, 2, 2, 2, 2]
]

generate_rug(7) ➞ [
  [3, 3, 3, 3, 3, 3, 3],
  [3, 2, 2, 2, 2, 2, 3],
  [3, 2, 1, 1, 1, 2, 3],
  [3, 2, 1, 0, 1, 2, 3],
  [3, 2, 1, 1, 1, 2, 3],
  [3, 2, 2, 2, 2, 2, 3],
  [3, 3, 3, 3, 3, 3, 3]
]
Notes
n >= 0.
Always increment by 1 each "layer" outwards you travel.
"""

def generate_rug(n):
    if n == 1:
        return [[0]]

    rug = [[0 for _ in range(n)] for _ in range(n)]
    layers = n // 2

    for layer in range(layers):
        value = layers - layer
        for i in range(layer, n - layer):
            rug[layer][i] = value
            rug[n - 1 - layer][i] = value
            rug[i][layer] = value
            rug[i][n - 1 - layer] = value

    return rug



# def generate_rug(n):
#
# 	result = []
# 	master = [n // 2 for _ in range(n)]
# 	start = 1
# 	end = (len(master) - 2)
#
# 	result.append(master)
# 	operation = 'x - 1'
#
# 	while len(result) < n:
# 		if start < end and operation == 'x - 1':
# 			modified_n = [eval(operation) if start <= i <= end else x for i, x in enumerate(result[-1])]
# 			result.append(modified_n)
# 			start += 1
# 			end -= 1
# 		elif start == end:
# 			modified_n = [eval(operation) if start <= i <= end else x for i, x in enumerate(result[-1])]
# 			result.append(modified_n)
# 			operation = 'x + 1'
# 			modified_n = [eval(operation) if start <= i <= end else x for i, x in enumerate(result[-1])]
# 			result.append(modified_n)
# 			start -= 1
# 			end += 1
# 		elif start < end and operation == 'x + 1':
# 			modified_n = [eval(operation) if start <= i <= end else x for i, x in enumerate(result[-1])]
# 			result.append(modified_n)
# 			start -= 1
# 			end += 1
#
# 	return result

# print(generate_rug(1))
# print(generate_rug(3))
print(generate_rug(5))
print(generate_rug(7))
print(generate_rug(9))

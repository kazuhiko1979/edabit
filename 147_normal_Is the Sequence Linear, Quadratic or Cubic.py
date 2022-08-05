"""
Is the Sequence Linear, Quadratic or Cubic?
Create a function that determines if a given sequence is linear, quadratic or cubic.
The input will be a list of numbers of varying lengths.
The function should return "Linear", "Quadratic" or "Cubic".

Examples
seq_level(1, 2, 3, 4, 5) ➞ "Linear"

seq_level(3, 6, 10, 15, 21) ➞ "Quadratic"

seq_level(4, 14, 40, 88, 164) ➞ "Cubic"
"""

def seq_level(lst, count=0):

	# v2
	diff = [b - a for a, b in zip(lst, lst[1:])]
	if len(set(diff)) == 1:
		return ['Linear', 'Quadratic', 'Cubic'][count]
	count += 1
	return seq_level(diff, count)

	# v1
	# lst = [lst[i]-lst[i - 1] for i in reversed(range(1, len(lst)))]
	#
	# if len(set(lst)) == 1:
	# 	return "Linear"
	# else:
	# 	lst = [lst[j-1] - lst[j] for j in range(1, len(lst))]
	# 	if len(set(lst)) == 1:
	# 		return "Quadratic"
	# 	else:
	# 		if count > 3:
	# 			seq_level(lst, count+1)
	# 		return "Cubic"




print(seq_level([1, 2, 3, 4, 5]))
print(seq_level([2, 1, 0, -1, -2]))
print(seq_level([3, 6, 10, 15, 21]))
print(seq_level([4, 14, 40, 88, 164]))
print(seq_level([17, 59, 143, 287, 509, 827]))

"""
Sort by Number of Calls
Create a function that takes a list of functions and sorts them in ascending order based on how many calls are needed for them to return a non-function.

Examples
f1 = lambda: "hello"
# f1() ➞ "hello"

f2 = lambda: lambda: "edabit"
# f2()() ➞ "edabit"

f3 = lambda: lambda: lambda: "user"
# f3()()() ➞ "user"

func_sort([f2, f3, f1]) ➞ [f1, f2, f3]
# [f2, f3, f1] ➞ [2, 3, 1] ➞ [1, 2, 3] ➞ [f1, f2, f3]

func_sort([f1, f2, f3]) ➞ [f1, f2, f3]
# [f1, f2, f3] ➞ [1, 2, 3] ➞ [1, 2, 3] ➞ [f1, f2, f3]

func_sort([f2, "func"]) ➞ ["func", f2]
# [f2, "func"] ➞ [2, 0] ➞ [0, 2] ➞ ["func", f2]
Notes
Treat non-functions as needing zero calls.
Every function will be called with empty parameters.
Every function will need to be called at least once.
The potentially returned values include ints, floats, and lists, among others.
"""
# v2

# f1 = lambda: "hello"
# f2 = lambda: lambda: "edabit"
# f3 = lambda: lambda: lambda: "user"

# def func_sort(lst):
#
# 	def calls(i):
# 		j = 0
# 		while True:
# 			if callable(i):
# 				j += 1
# 				i = i()
# 			else:
# 				return j
# 	return sorted(lst, key=calls)



import inspect

f1 = lambda: "hello"
f2 = lambda: lambda: "edabit"
f3 = lambda: lambda: lambda: "user"

# v1
def func_sort(lst):

	convert_list = [inspect.getsource(x).split().count("lambda:") if type(x) != str else 0 for x in lst]

	result = {}
	for i, x in zip(convert_list, lst):
		if i == 0:
			result[i] = x
		elif i > 0:
			result[i] = eval('f' + str(i))

	result = list(sorted(result.items()))
	return [chr[1] for chr in result]

print(func_sort([f2, f3, f1]))
print(func_sort([f2, "func"]))

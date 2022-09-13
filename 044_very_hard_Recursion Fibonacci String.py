"""
Recursion: Fibonacci String
A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together as it progresses similarly to that of the Fibonacci series.

Examples
fib_str(3, ["j", "h"]) ➞ "j, h, hj"

fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"
Notes
All values for n will be at least 2.
It is expected from the challenge-takers to come up with a solution using the concept of recursion or the so-called recursive approach.
You can read more topics about recursion (see Resources tab) if you aren't familiar with it yet or hasn't fully understood the concept behind it before taking up this challenge or unless otherwise.
"""
# v3
def fib_str(n, f):
	if n == 2:
		return ', '.join(f)
	else:
		f = [i for i in f]
		f.append(f[-1] + f[-2])
		return fib_str(n-1, f)



# v2
# def fib_str(n, f, i=0):
# 	if i + 2 == n:
# 		return ', '.join(f)
# 	return fib_str(n, f+[f[i+1]+f[i]], i+1)


# v1
# import copy
#
# def fib_str(n, f, temp=[]):
#
# 	while n:
# 		n -= 1
# 		temp.append(f[0])
# 		f[0], f[1] = f[1], f[1] + f[0]
# 		return fib_str(n, f)
#
# 	result = copy.deepcopy(temp)
# 	temp.clear()
# 	return ', '.join(result)

print(fib_str(3, ["j", "h"]))
print(fib_str(5, ["e", "a"]))
print(fib_str(6, ["n", "k"]) )
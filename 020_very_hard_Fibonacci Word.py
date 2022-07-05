"""
Fibonacci Word
A Fibonacci Word is a specific sequence of binary digits (or symbols from any two-letter alphabet). The Fibonacci Word is formed by repeated concatenation in the same way that the Fibonacci numbers are formed by repeated addition.

Create a function that takes a number n as an argument and returns the first n elements of the Fibonacci Word sequence.

If n < 2, the function must return "invalid".

Examples
fibo_word(1) ➞ "invalid"

fibo_word(3) ➞ "b, a, ab"

fibo_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"
"""


def fibo_word(n):

	# v3
	if n < 2:
		return "invalid"
	if n == 2:
		return "b, a"
	return (fibo_word(n-1) + ', ' + ''.join(fibo_word(n-1).split(', ')[-2::][::-1]))


	# v2
	# arr = ["b", "a"]
	# while len(arr) < n:
	# 	arr.append(arr[-1] + arr[-2])
	# return ", ".join(arr) if n > 2 else "invalid"


	# v1
	# if n <= 2:
	# 	return "invalid"
	#
	# a, b = "a", "b"
	# fib_l = ""
	# while n:
	# 	n -= 1
	# 	fib_l += b + ', '
	# 	b, a = a, a + b
	# return fib_l[:-2]

print(fibo_word(1))
print(fibo_word(2))
print(fibo_word(3))
print(fibo_word(7))


# print(fib_word(10))

# print([fib_word(n) for n in range(1, 10)])

"""
Recursion: Exact Factorial Bounds
Create a recursive function that tests if a number is the exact upper bound of the factorial of n. If so, return a list that contains the exact factorial bound and n, or otherwise, the string "Not exact!".

Examples
is_exact(6) ➞ [6, 3]

is_exact(24) ➞ [24, 4]

is_exact(125) ➞ "Not exact!"

is_exact(720) ➞ [720, 6]

is_exact(1024) ➞ "Not exact!"

is_exact(40320) ➞ [40320, 8]
Notes
It is expected from the challenge-takers to come up with a solution using the concept of recursion or the so-called recursive approach.
You can read on more topics about recursion (see Resources tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.
There will be no exceptions to handle. All inputs are positive integers.
A non-rec
"""

def is_exact(n, check=1, count=1):

	if n == check:
		return [n, count]
	elif n < check:
		return "Not exact!"
	else:
		return is_exact(n, (count + 1) * check, count+1)


print(is_exact(6))
print(is_exact(24))
print(is_exact(125))
print(is_exact(720))
print(is_exact(1024))
print(is_exact(40320))



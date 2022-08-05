"""
Natural Emptiness
In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

0 = [ ] is the empty set
1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
n = n−1 ∪ [ n−1 ] = ...
Write a function that receives an integer n and produces the representing set.

Examples
rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]
Notes
Make sure to use list brackets [,].
Technically we should use set brackets {,} instead, but Python doesn't approve.
A neat feature of this representation is that n < m precisely if the set representing n is contained in the set representing m.
"""

def rep_set(n):

	# v2
	if not n:
		return []
	else:
		return rep_set(n-1) + [rep_set(n-1)]
	# v1
	# d = {}
	# d[0] = []
	# for x in range(1, n+1):
	# 	d[x] = [d[i] for i in range(x)]
	# return d[n]

print(rep_set(0))
print(rep_set(1))
print(rep_set(2))
print(rep_set(3))

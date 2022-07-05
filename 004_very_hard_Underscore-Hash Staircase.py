"""
Underscore-Hash Staircase
Create a function that will build a staircase using the underscore _ and hash # symbols. A positive value denotes the staircase's upward direction and downwards for a negative value.

Examples
staircase(3) ➞ "__#\n_##\n###"
__#
_##
###

staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######

staircase(2) ➞ "_#\n##"
_#
##

staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#
Notes
All inputs are either positive or negative values.
The string to be returned is adjoined with the newline character (\n).
"""

def starcase(n):

	if n < 0:
		return '\n'.join(starcase(-n).split('\n')[::-1])
	if n == 1:
		return '#'
	return '\n'.join(['_' + l for l in starcase(n-1).split('\n')]+['#' * n])


print(starcase(3))
print(starcase(7))
print(starcase(-8))
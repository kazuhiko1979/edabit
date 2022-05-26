"""
Lychrel Numbers
The following is the Lychrel test.

Start with any positive number. Add the number with the number formed by reversing its digits. Is the sum a palindrome?
If not, repeat the process.

For most numbers, a palindrome is produced after a few iterations (7 or fewer) of the process above.
Numbers that never reach a palindrome are called Lychrel numbers.
No number in base 10 has been proven to be a Lychrel number,
but numbers that don't produce palindromes after an unusually high number of iterations of the reverse-and-add process are said to be Lychrel candidates

Create a function that takes a number and returns True if it is a Lychrel candidate. If it isn't, return the number of reverse-and-add iterations it takes to produce a palindrome. For this challenge, the threshold for a Lychrel candidate is >=500 iterations.

Examples
lychrel(33) ➞ 0
# Already a palindrome.

lychrel(65) ➞ 1
# 65+56 -> 121

lychrel(348) ➞ 3
# 348+843 -> 1191+1911 -> 3102+2013 -> 5115

lychrel(295) ➞ True
"""

count = 0

def lychrel(num):

	return isPalindrome(num, count)

def isPalindrome(num, count):
	reverse_num = str(num)[::-1]
	try:
		if num == int(reverse_num):
			return count
		else:
			num = num + int(reverse_num)
			count += 1
			return isPalindrome(num, count)
	except RuntimeError:
		return True

print(lychrel(33))
print(lychrel(65))
print(lychrel(348))
print(lychrel(196))
print(lychrel(295))
print(lychrel(89))
print(lychrel(7582))

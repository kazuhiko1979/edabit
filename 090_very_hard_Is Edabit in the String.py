"""
Is Edabit in the String?
A string contains the word "edabit" if a subsequence of its characters spell "edabit".

Write a function that accepts a string and returns “YES” if the string contains a subsequence of the word edabit or "NO" if it does not.

Examples
edabit_in_string(“eddaaabt”) ➞ “NO”

edabit_in_string(“edwardisabletodoit”) ➞ “YES”

edabit_in_string(“abecdfghijklmnopqrstuvwxyz”) ➞ “NO”
"""
import copy

def edabit_in_string(txt):

	words = "edabit"
	master = copy.deepcopy(words)

	result = ''

	while master:
		for i in txt:
			if master[0] == i:
				master = master[1:]
				txt = txt[1:]
				result += i
				if words == result:
					return "YES"
			else:
				txt = txt[1:]

		return "NO"

print(edabit_in_string("eddaaabt")) # NO
print(edabit_in_string("edwardisabletodoit")) # YES
print(edabit_in_string("abecdfghijklmnopqrstuvwxyz")) # NO
print(edabit_in_string("edisthebestatthis")) # NO
print(edabit_in_string("teachandlearnbitbybit")) # YES
print(edabit_in_string("fjkdlkskkkkkdkkdkdedaaakkjkkdkkdklqiieuirooeizooziiciibiiiiifooiioiiuuyeyttgguoosooodiifiufiiodikkjkls")) # YES




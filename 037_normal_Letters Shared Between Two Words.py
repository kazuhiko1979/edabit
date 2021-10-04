"""
Create a function that returns the number of characters shared between two words.

Examples
shared_letters("apple", "meaty") ➞ 2
# Since "ea" is shared between "apple" and "meaty".

shared_letters("fan", "forsook") ➞ 1

shared_letters("spout", "shout") ➞ 4
"""
def shared_letters(txt1, txt2):
	return len(list(set(txt1) & set(txt2)))

print(shared_letters("apple", "meaty"))





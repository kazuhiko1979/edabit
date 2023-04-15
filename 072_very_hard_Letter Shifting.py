"""
Letter Shifting
Create a function that takes a string and shifts the letters to the right by an amount n but not the whitespace.

Examples
shift_letters("Boom", 2) ➞ "omBo"

shift_letters("This is a test",  4) ➞ "test Th i sisa"

shift_letters("A B C D E F G H", 5) ➞  "D E F G H A B C"
Notes
Keep the case as it is.
n can be larger than the total number of letters.
"""
# v2
def shift_letters(txt, n):
	t = txt.replace(' ', "")
	n = n % len(t)
	t = iter(t[-n:] + t[:-n])
	return "".join(c if c == " " else next(t) for c in txt)

# v1
# def shift_letters(txt, n):
#
# 	txt_count = [len(i) for i in txt.rsplit(' ')]
# 	count = abs(n)
# 	txt = ''.join(txt.rsplit(' '))
#
# 	while count > 0:
# 		temp = -1 % len(txt)
# 		txt = txt[temp:] + txt[:temp]
# 		count -= 1
#
# 	result = []
# 	for i in txt_count:
# 		word = txt[:i]
# 		result.append(word)
# 		txt = txt[i:]
# 	return ' '.join(result)

print(shift_letters("Boom", 2))
print(shift_letters("This is a test",  4))
print(shift_letters("A B C D E F G H", 5))
print(shift_letters("Made by Harith Shah", 15))
print(shift_letters("The most addictive way to learn", 19))
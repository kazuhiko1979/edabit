"""
String Incrementer
Write a function which increments a string to create a new string.

If the string ends with a number, the number should be incremented by 1.
If the string doesn't end with a number, 1 should be added to the new string.
If the number has leading zeros, the amount of digits should be considered.
Examples
increment_string("foo") ➞ "foo1"

increment_string("foobar0009") ➞ "foobar0010"

increment_string("foo099") ➞ "foo100"
"""
20230520 edit

def increment_string(txt):

	result = (''.join(c for c in txt if c.isalpha()) or None,
			   ''.join(c for c in txt if c.isdigit()) or None)

	if result[1]:
		number = str(int(result[1].lstrip('0')) + 1)
		return result[0] + number.zfill(len(result[1]))
	return result[0] + "1"

print(increment_string("foo"))
print(increment_string("foobar01002"))
print(increment_string("foobar0009"))
print(increment_string("foobar00599"))
print(increment_string("foo099"))
print(increment_string("foo09999"))



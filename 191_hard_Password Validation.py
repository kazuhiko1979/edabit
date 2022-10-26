"""
Password Validation
Create a function that validates a password to conform to the following rules:

Length between 6 and 24 characters.
At least one uppercase letter (A-Z).
At least one lowercase letter (a-z).
At least one digit (0-9).
Maximum of 2 repeated characters.
"aa" is OK 👍
"aaa" is NOT OK 👎
Supported special characters:
! @ # $ % ^ & * ( ) + = _ - { } [ ] : ; " ' ? < > , .
Examples
validate_password("P1zz@") ➞ False
// Too short.

validate_password("iLoveYou") ➞ False
// Missing a number.

validate_password("Fhg93@") ➞ True
// OK!
"""
# v3
from re import search as has


def validate_password(password):

	pattern = ['^.{6,24}$', '[a-z]', '[A-Z]', '[0-9]']
	included = all(has(regex, password) for regex in pattern)
	return included and not has(r'(.)\1\1', password)


# v2
# import re
#
# def validate_password(password):
#
# 	length = 6 <= len(password) <= 24
# 	uppercase = re.search(r'[A-Z]', password)
# 	lowercase = re.search(r'[a-z]', password)
# 	digits = re.search(r'\d', password)
# 	repeated = not re.search(r'(.)\1{2,}', password)
#
# 	conditions = (length, uppercase, lowercase, digits, repeated)
#
# 	return all(conditions)


# v1
# from collections import Counter
# import re
#
# def validate_password(password):
#
# 	max_repeated_char = max(Counter(password).values())
#
# 	pattern = '^(?=.*?[A-Z]{1,})(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{6,24}$'
#
# 	if max_repeated_char <= 2:
# 		if re.match(pattern, password):
# 			return True
# 		else:
# 			return False
# 	else:
# 		return False


print(validate_password("P1zz@"))
print(validate_password("P1zz@P1zz@P1zz@P1zz@P1zz@"))
print(validate_password("mypassword11"))
print(validate_password("MYPASSWORD11"))
print(validate_password("iLoveYou"))
print(validate_password("Repeeea7!"))
print()
print(validate_password("H4(k+x0"))
print(validate_password("Fhg93@"))
print(validate_password("aA0!@#$%^&*()+=_-{}[]:;"))
print(validate_password("zZ9'?<>,."))





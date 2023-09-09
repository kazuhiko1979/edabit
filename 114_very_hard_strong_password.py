"""
Strong Password
Create a function that determines the minimum number of characters needed to make a strong password.

A password is considered strong if it satisfies the following criteria:

Its length is at least 6.
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character: !@#$%^&*()-+
Types of characters in a form you can paste into your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
Examples
strong_password(“Ed1”) ➞ 3

strong_password(“#Edabit”) ➞ 1

strong_password("W1llth!spass?") ➞ 0
Notes
Try solving this without RegEx.
"""

def strong_password(password):

	ans = sum([
	sum(i.isdigit() for i in password) == 0,
	sum(i.islower() for i in password) == 0,
	sum(i.isupper() for i in password) == 0,
	sum(i in "!@#$%^&*()-+" for i in password) == 0
	])
	return max(ans, 6 - len(password))

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
#
# need_characters_of_password = numbers + lower_case + upper_case + special_characters
#
# def strong_password(password):
#
# 	num = find_need_password(numbers, password)
# 	lower = find_need_password(lower_case, password)
# 	upper = find_need_password(upper_case, password)
# 	special = find_need_password(special_characters, password)
#
# 	total_need_num = [num, lower, upper, special].count(False)
#
# 	return max(6 - len(password), total_need_num)
#
# def find_need_password(characters, password):
# 	return any(char in password for char in characters)

print(strong_password("#Edabit")) # 1
print(strong_password("Cr3ateAStr0ng1")) # 1
print(strong_password("CreateAStrongOne")) # 2
print(strong_password("willthispass")) # 3
print(strong_password("w1llth!spass?")) # 1
print(strong_password("W1llth!spass?")) # 0
print(strong_password("1sth!")) # 1
print(strong_password("sth!")) # 2
print(strong_password("bd")) # 4
print(strong_password("d")) # 5
print(strong_password("[?")) # 4
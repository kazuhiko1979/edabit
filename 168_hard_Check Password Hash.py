"""
Check Password Hash
Write a function that takes a username and password and checks the list user_pass_db for a match. The list stores the passwords as a hash using the SHA1 algorithm. Return True for a match and False otherwise.

Examples
user_pass_db = [{"username" : "myUsername", "pass_hash" : "5413ee24723bba2c5a6ba2d0196c78b3ee4628d1"}]

check_pass("myUsername", "myPassword") ➞ True

check_pass("myUsername", "wrongPassword") ➞ False
"""
import hashlib

user_pass_db = [{"username" : "tony", "pass_hash" : "11725d3f4588325f1c90c50348624dcc55978f39"},
	{"username" : "jason", "pass_hash" : "5a6d719f958b1a610712f8e342ef0a4dd4b80a35"},
	{"username" : "lola", "pass_hash" : "7dda6e1b3988b488b0821e24732ca42d6b72f0ce"},
	{"username" : "dan", "pass_hash" : "ec09d3b165aeabf77f5c9436c2d644b6e2f31ba9"}]

def check_pass(username, password):

	# v2
	h = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
	return {'username': username, 'pass_hash': h} in user_pass_db


	# v1
	# h = hashlib.sha1(password.encode())
	# h = h.hexdigest()
	#
	# for items in user_pass_db:
	# 	if items["username"] == username:
	# 		if items["pass_hash"] == h:
	# 			return True
	# 		else:
	# 			return False
	# return False

print(check_pass("lola","jimbob"))
print(check_pass("tony","hexagon"))
print(check_pass("jason", "tyrannosaurus"))
print(check_pass("dan", "FranklinPierce123"))
print(check_pass("somebot", "admin123"))
print(check_pass("lola","wrongpass"))






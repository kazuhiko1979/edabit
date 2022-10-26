"""
Anna Likes Daniel
Anna is a strange girl. She likes certain boys, but not others. You have to figure out why she likes some, and not the others.

Examples
anna_likes("David") ➞ False

anna_likes("Samuel") ➞ True

anna_likes("Gary") ➞ False
Notes
All names / inputs are valid.
Anna likes her own name.
"""
import re

def anna_likes(name):

	return len(re.findall("[aeiouAEIOU]", name)) * 2 == len(name)

	# not work
	# pattern = "a$|[an]"
	# # print(len(name))
	# # 4文字でregにマッチ判断
	# if len(name) == 4:
	# 	if re.findall(pattern, name):
	# 		return name
	# 	else:
	# 		return name
	# # 4文字以外で
	# else:
	# 	if re.search(pattern, name):
	# 		return name
	# 	else:
	# 		return False


print(anna_likes("Daniel"))
print(anna_likes("Paul"))
print(anna_likes("Joshua"))
print(anna_likes("Geogle"))
print(anna_likes("Eric"))


print()
# False
print(anna_likes("David"))



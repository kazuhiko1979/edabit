"""
Valid JavaScript Comments
In JavaScript, there are two types of comments:

Single-line comments start with //
Multi-line or inline comments start with /* and end with */
The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add, there can be no single-line comments in between multi-line comments in between the /* and */.

Create a function that returns True if comments are properly formatted, and False otherwise.

Examples
comments_correct("//////") ➞ True
# 3 single-line comments: ["//", "//", "//"]

comments_correct("/**//**////**/") ➞ True
# 3 multi-line comments + 1 single-line comment:
# ["/*", "*/", "/*", "*/", "//", "/*", "*/"]

comments_correct("///*/**/") ➞ False
# The first /* is missing a */

comments_correct("/////") ➞ False
# The 5th / is single, not a double //
"""
# v3
def comments_correct(txt):

	txt = txt.replace('/**/', '')
	txt = txt.replace('//', '')

	if len(txt) == 0:
		return True
	else:
		return False




# v2
# def comments_correct(txt):
# 	while txt:
# 		if txt[0:2] == '//':
# 			txt = txt[2:]
# 		elif txt[0:4] == '/**/':
# 			txt = txt[4:]
# 		else:
# 			return False
# 	return True


# v1
# def comments_correct(txt):
#
# 	if len(txt) % 2 != 0:
# 		return False
#
# 	temp = ""
# 	single, multi = [], []
#
# 	for i in txt:
# 		temp += i
# 		if temp == "//":
# 			single.append(temp)
# 			temp = ""
# 		elif temp == "/*":
# 			multi.append(temp)
# 			temp = ""
# 		elif temp == "*/":
# 			if multi[-1] == "/*":
# 				multi.append(temp)
# 				temp = ""
# 			else:
# 				return False
#
# 	return len(multi) % 2 == 0


print(comments_correct("//////"))
print(comments_correct("/**//**////**/"))
print(comments_correct("/**//**//**//**/"))
print(comments_correct("///**///"))
print(comments_correct("/**//////**//**////**/////"))
print(comments_correct("//"))
print(comments_correct("/**/"))
print(comments_correct("///*/**/"))
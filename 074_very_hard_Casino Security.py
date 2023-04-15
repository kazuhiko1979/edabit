"""
Casino Security
You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.

If there is no guard between thief and money, return "ALARM!"
If the money is protected, return "Safe"
String Components
x - Empty Space
T - Thief
G - Guard
$ - Money
Examples
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
Notes
Money at the extremes are safe.
"""

# V3
def security(txt):

	txt = txt.replace("x", "")
	return ["Safe", "ALARM!"]["T$" in txt or "$T" in txt]


# V2
def security(txt):

	txt = txt.replace("x", "")
	return ["Safe", "ALARM!"]["T$" in txt or "$T" in txt]


# def security(txt):
#
# 	try:
# 		top_index_of_dollar = list(txt).index('$')
# 		bottom_index_of_dollar = list(txt)[::-1].index('$')
# 	except ValueError:
# 		return "Safe"
#
# 	def security_help(list_txt, index_of_dollar):
#
# 		index_guard, index_thief = None, None
# 		for i in range(index_of_dollar, -1, -1):
# 			if list_txt[i] == 'G':
# 				index_guard = i
# 			if list_txt[i] == 'T':
# 				index_thief = i
#
# 		if not index_thief and type(index_thief) == 'NoneType':
# 			return "Safe"
#
# 		if not index_guard and type(index_guard) == 'NoneType':
# 			if index_thief:
# 				return False
# 		if not index_guard:
# 			if not index_thief:
# 				return True
# 		if index_guard:
# 			if index_thief:
# 				if index_guard > index_thief:
# 					return True
# 				else:
# 					return False
# 		if index_guard:
# 			if not index_thief or type(index_thief) == 'NoneType':
# 				return True
# 			else:
# 				return False
#
# 	if security_help(txt, top_index_of_dollar):
# 		if security_help(txt[::-1], bottom_index_of_dollar):
# 			return "Safe"
# 	return "ALARM!"


print(security("xxTxxx$xxxTxxxGxxT"))
print(security("xGxx$xxGxxxTTT"))
print(security("TxGxx$xxx$xxxGxxT"))
print(security("GxxxTxxGxxTxx$xx$xxTxxG"))
print(security("xxGTxx$xx$xxxxxxG"))
print(security("xxTxxxxxxxx$xGxxxxxxT"))
print(security("xx$xxGxxxx$xxxxxxxxxxT"))

print(security("xxxTxxxxT"))
print(security("xxGxxxGGG"))
print(security("x$xx$x$x$xx"))







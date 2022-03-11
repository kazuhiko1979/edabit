"""
Validate the Relationships Between Integers in a String
You will be given a string consisting of a list of integers and their relationships to their neighboring integers. For instance:

"-15<-10<=0=0<5"
Test to see that all the relationships between the integers in the string are true. If they are, return True. If they are not, return False.

Examples
validate_relationships("5>-1<0=0<-5>5=5") ➞ False
# This is False because 0 is not less than -5.

validate_relationships("-15<-10<=0=0<5") ➞ True

validate_relationships("0=807<1000<=1000>9990<-3605<=20") ➞ False
# This is False because 0 is not equal to 807.
Notes
This is a modifcation of Helen Yu's "Correct Signs" challenge.
As the examples above show, there could be negative numbers in the string.
The numbers will only be separated by: =, <, >, >=, <=
Tests will not contain any spaces.
"""

def validate_relationships(txt):

	return eval(txt.replace("=", "==").replace("<==", "<=").replace(">==", ">="))


	# temp = ""
	#
	# for i in txt:
	# 	if i == "=" and temp[-1] not in "<>":
	# 		temp += "=="
	# 	else:
	# 		temp += i
	#
	# return eval(temp)



	# # temp = ["=" if txt[i] == "=" and txt[i-1].isdigit() and i != len(txt) else txt[i] for i in range(0, len(txt))]
	#
	# temp = []
	#
	# for i in range(0, len(txt)):
	# 	temp.append(txt[i])
	# 	if txt[i] == "=" and txt[i-1].isdigit() and i != len(txt):
	# 		temp.append("=")
	#
	# x = ''.join(temp)
	# return eval(x)
	#
	# # temp = []
	# #
	# # for i in range(0, len(txt)):
	# # 	temp.append(txt[i])
	# # 	if txt[i] == "=":
	# # 		if txt[i-1].isdigit():
	# # 			if i != len(txt):
	# # 				temp.append("=")
	# #
	# x = ''.join(temp)
	# return eval(x)

# return 5>-1 and -1<0 and 0==0 and 0<-5 and -5>5 and 5==5
# return -15<-10 and -10<=0 and 0==0 and 0<5

print(validate_relationships("5>-1<0=0<-5>5=5"))
print(validate_relationships("-15<-10<=0=0<5"))
print(validate_relationships("0=807<1000<=1000>9990<-3605<=20"))
print(validate_relationships("3<=3<11>-109"))

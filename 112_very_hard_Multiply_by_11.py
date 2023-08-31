"""
Multiply by 11
Given a positive number as a string, multiply the number by 11 and also return it as a string. However, there is a catch:

You are NOT ALLOWED to simply cast the number into an integer!

Now, how is this challenge even possible? Despite this, there is still a way to solve it, and it involves thinking about how someone might multiply by 11 in their head. See the tips below for guidance.

Examples
multiply_by_11("11") ➞ "121"

multiply_by_11("111111111") ➞ "1222222221"

multiply_by_11("9473745364784876253253263723") ➞ "104211199012633638785785900953"
Tip
There is a simple trick to multiplying any two-digit number by 11 in your head:

Add the two digits together
Place the sum between the two digits!
Note if the total goes over, carry the sum on to the next digit
# 23 * 11
# Add together 2 and 3 to make 5
# Place 5 between the two digits to make 253
# 77 * 11
# Add together 7 and 7 to make 14
# Place 4 between the two digits to make 747
# Carry the 1 to make 847
Notes
See this resource to find out how this process can be utilized for numbers of any length!
This challenge was heavily inspired by Mubashir Hassan's challenge on adding two numbers together!
"""

def multiply_by_11(n):

	temp = [int(i[0]) + int(i[1]) for i in zip(n, n[1:])]
	temp.insert(0, int(list(n)[0]))
	temp.append(int(list(n)[-1]))

	result = []
	flag = False
	nine = False

	for x in temp[::-1]:
		if len(str(x)) == 1 :
			if x == 9:
				if flag:
					x = 10
					result.append(int(str(x)[-1]))
					flag = True
					nine = True
				else:
					result.append(x)
					flag = False
			else:
				if not nine and not flag:
					result.append(x)
				if flag:
					result.append(x+1)
					nine = False
					flag = False

		elif len(str(x)) > 1:
			if flag:
				num = int(str(x)) + 1
				result.append(int(str(num)[-1]))
			elif not flag:
				num = int(str(x))
				result.append(int(str(num)[-1]))
				flag = True

	number = [str(value) for value in reversed(result)]

	if number[0] == '0':
		number.insert(0, '1')
	return ''.join(number)

print(multiply_by_11('113434'))
print(multiply_by_11('111111111'))
print(multiply_by_11('12345678987654321'))
print(multiply_by_11('9473745364784876253253263723'))
print(multiply_by_11('57798475537262775664949793178544410084322125871112100873888108368764143479609636230947305905435344501732127613092539526132478297050231140298675968743242036743911849895415821806568888540371506471898980622461341526051319836717892341981184041251420949699402992990039646759030590473730159880164726562551837027321585062972130328324427060636687637549685519707281109006818275101108700527287692750795014581999611840743604415714313247263830886107561336757943548272922950996455097654414521769924004347236729944'))

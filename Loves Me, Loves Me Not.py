"""
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"
Notes
Remember to return a string.
The first phrase is always "Loves me".

"""
# def loves_me(n):
	# returnList = []
	# for i in range(n):
	# 		if i % 2 == 0:
	# 				returnList.append("Loves me")
	# 		else:
	# 				returnList.append("Loves me not")
	# returnList[-1] = returnList[-1].upper()
	# finalList = ', '.join(str(a) for a in returnList)
	# return finalList


def loves_me(n):

    temp = []

    for i in range(n):

        if i % 2 == 0:
            temp.append("Loves me")
        else:
            temp.append("Loves me not")

    temp[-1] = temp[-1].upper()
    result = ', '.join(i for i in temp)
    return result

print(loves_me(2))
print(loves_me(3))



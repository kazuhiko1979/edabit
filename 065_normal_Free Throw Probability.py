"""
What's the probability of someone making a certain amount of free throws in a row given their free throw success percentage? If Sally makes 50% of her free shot throws. Then Sally's probability of making 5 in a row would be 3%.

Examples
free_throws("75%", 5) ➞ "24%"

free_throws("25%", 3) ➞ "2%"

free_throws("90%", 30) ➞ "4%"
Notes
The success rate is a string.
The function should return a string with the percent sign.
Round your answer to the nearest whole number.
"""

def free_throws(success, row):

    return '{}%'.format(round((int(success[:-1]) / 100) ** row * 100))

    # success = int(success.strip("%")) / 100
    # return str(round(success ** row * 100)) + "%"


print(free_throws("75%", 5))
print(free_throws("25%", 3))
print(free_throws("90%", 30))
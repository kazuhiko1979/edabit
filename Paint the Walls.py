"""
Given a predetermined rate from a dictionary, write the function that will return the time it takes for a certain amount of people to paint a certain amount of walls. Return the minutes as an integer. No rounding is necessary.

Example
// It takes 22 minutes for 10 people to paint 10 walls.
// How many minutes does it take 14 people to paint 14 walls?

let rate = {
  people: 10,
  walls: 10,
  minutes: 22
}

time(rate, people, walls) ➞ 22
"""

rate1 = {
	'people': 4,
	 'walls': 9,
	 'minutes': 63
}

def time(dct, people, walls):

    A = dct.get('walls')
    x = dct.get('people')
    t = dct.get('minutes')
    n = A / (x * t)
    # print(n)
    import math
    time = math.ceil(walls / (people * n))
    return time

print(time(rate1, 7, 4))







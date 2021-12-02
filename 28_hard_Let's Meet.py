"""
From point A, an object is moving towards point B at constant velocity va (in km/hr). From point B, another object is moving towards point A at constant velocity vb (in km/hr). Knowing this and the distance between point A and B (in km), write a function that returns how much time passes until both objects meet.

Format the output like this:

"2h 23min 34s"
Examples
lets_meet(100, 10, 30) ➞ "2h 30min 0s"

lets_meet(280, 70, 80) ➞ "1h 52min 0s"

lets_meet(90, 75, 65) ➞ "0h 38min 34s"
Notes
Seconds should be rounded down to the nearest whole number.
"""
import math

def lets_meet(distance, va, vb):

    t = int(3600*distance/(va+vb))

    return '{}h {}min {}s'.format(t//3600, (t%3600)//60, t%60)

    # second = (distance / (va + vb)) * 3600
    # m, s = divmod(second, 60)
    # h, m = divmod(m, 60)
    # return '{}h {}min {}s'.format(int(h), int(m), int(s))

    # hours = math.floor(distance / (va + vb))
    # minutes = math.floor(distance / (va + vb) * 60) - hours * 60
    # seconds = math.floor(60 * (distance / (va + vb) * 60 - minutes)) - hours * 3600
    #
    # return "{}h {}min {}s".format(hours, minutes, seconds)



print(lets_meet(100, 10, 30))
print(lets_meet(90, 75, 65))
print(lets_meet(33, 15, 20))

"""
Manipulating Randomness
There was supposed to be a challenge here, but the only things present are random tests. Pass them anyways.

Examples
import random

manipulate() == random.randrange(1000) ➞ True

manipulate() == random.randrange(2024) ➞ True

manipulate() == random.randrange(60049) ➞ True
"""
import random

class Messing:
    def __eq__(self, other):
        return True

def manipulate():
    return Messing()
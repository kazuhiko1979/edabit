"""
Create a function that produces a random number that
contains all numbers from one to five, without any duplicates.
"""
import random


def numbers():

    lst = ['1', '2', '3', '4', '5']
    lst = random.sample(lst, k=5)

    return int(''.join(lst))

print(numbers())



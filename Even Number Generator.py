"""
Using list comprehensions, create a function that
finds all even numbers from 1 to the given number.
"""


def find_even_nums(num):

    list = []

    for i in range(1, num+1):
        if i % 2 == 0:
            list.insert(0, i)
            list.sort()
    return list


print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))
# print(find_even_nums(100))
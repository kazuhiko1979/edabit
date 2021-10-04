"""
Create a function similar to Processings "map" function (check the Resources tab), in which a value and its range is taken and remapped to a new range.

The function takes 5 numbers:

Value: value
Range: low1 and high1
Range: low2 and high2
Examples
remap(7, 2, 12, 0, 100) ➞ 50

remap(17, 5, 55, 100, 30) ➞ 83.2

remap(50, 1, 51, 0, 100) ➞ 98
Notes
Test input will always be numbers.
If the input range is 0, return 0.
"""
# sample_list = list(range(5))
# print(sample_list)
#
# def multi(x):
#     y = x * 2
#     return y
#
# print(list(map(multi, sample_list)))

def remap(value, low1, high1, low2, high2):
    if high1 - low1 == 0:
        return 0
    k = (high1 - value) / (high1 - low1)
    return high2 - (high2 - low2) * k

print(remap(7, 2, 12, 0, 100))



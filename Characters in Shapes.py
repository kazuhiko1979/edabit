"""
Create a function to calculate how many characters in total are needed to make up the shape.
You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).
"""
"""
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9

count_characters([
  "22222222",
  "22222222",
]) ➞ 16

count_characters([
  "------------------"
]) ➞ 18

count_characters([]) ➞ 0
count_characters(["", ""]) ➞ 0
"""

def count_characters(lst):
    lst = sum(len(i) for i in lst)
    return lst

    # total = 0
    # for i in lst:
    #     total += len(i)
    # return total

print(count_characters([
  "###",
  "###",
  "###"
]))

print(count_characters([
  "22222222",
  "22222222",
]))

print(count_characters([
  "------------------"
]))

print(count_characters([]))
print(count_characters(["", ""]))



"""
A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

Examples
tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2
"""
def tallest_skyscrapper(lst):

    lst_count = len(lst)

    for value in lst:
        if 1 not in value:
            lst_count -= 1
        else:
            break
    return lst_count


print(tallest_skyscrapper([
	[0, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	[1, 1, 1, 1]
]))

print(tallest_skyscrapper([
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))

print(tallest_skyscrapper([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]))

print(tallest_skyscrapper([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1]
]))


# Create a function that takes a list containing only numbers and return the first element.
# Examples
# get_first_value([1, 2, 3]) ➞ 1
# get_first_value([80, 5, 100]) ➞ 80
# get_first_value([-500, 0, 50]) ➞ -500
from typing import List


def get_first_value(result: List[int]) -> int:

    return result[0]


if __name__ == '__main__':
    print(get_first_value([1, 2, 3]))

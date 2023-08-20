"""
Consecutive Ascending Numbers
Write a function that will return True if a given string (divided and grouped into a size) will contain a set of consecutive ascending numbers, otherwise, return False.

Examples
is_ascending("123124125") ➞ True
# Contains a set of consecutive ascending numbers
# if grouped into 3's : 123, 124, 125

is_ascending("101112131415") ➞ True
# Contains a set of consecutive ascending numbers
# if grouped into 2's : 10, 11, 12, 13, 14, 15

is_ascending("32332432536") ➞ False
# Regardless of the grouping size, the numbers can't be consecutive.

is_ascending("326325324323") ➞ False
# Though the numbers (if grouped into 3's) are consecutive but descending.

is_ascending("666667") ➞ True
# Consecutive numbers: 666 and 667.
Notes
A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.
"""
def is_ascending(s):
    n = len(s)
    for size in range(1, n // 2 + 1):
        prev_num = int(s[:size])
        i = size
        while i < n:
            current_num = int(s[i:i+size])
            if current_num - prev_num != 1:
                break
            i += size
            prev_num = current_num
        if i == n:
            return True
    return False

# Test cases
print(is_ascending("123124125"))  # True
print(is_ascending("101112131415"))  # True
print(is_ascending("32332432536"))  # False
print(is_ascending("326325324323"))  # False
print(is_ascending("666667"))  # True

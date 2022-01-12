"""
Bitwise Operator to Check Odd, Regular Expression to Check Even
Create two functions:

The first is is_odd() to check if a given number is odd using bitwise operator.
The second is is_even() to check if a given input is even using regular expressions.
Use of % operator is disallowed.

Examples
is_odd(3) ➞ "Yes"
# Use Bitwise Operator

is_odd(58) ➞ "No"
# Use Bitwise Operator

is_even("0") ➞ "Yes"
# Use Regular Expression

is_even("-99") ➞ "No"
# Use Regular Expression
Notes
Input will only be integers (positive/negative/zero).
For the second function, input will be numbers in string.
"""

import re

is_odd = lambda n:('No', 'Yes')[n&1]
is_even = lambda n:'Yes' if re.search('[02468]$', n) else 'No'

#
# def is_odd(n):
#     return 'Yes' if n ^ 1 == n - 1 else 'No'
#
# def is_even(n):
#     return 'Yes' if bool(re.match('-?\d*[02468]', n)) else 'No'

print(is_odd(-7))
print(is_even('111'))
print(is_even('520'))



